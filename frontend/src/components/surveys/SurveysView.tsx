"use client"

import { useReducer, useEffect, useCallback, useRef, useMemo, useState } from "react"
import { useSearchParams, useRouter } from "next/navigation"
import BandSpectrumStrip from "./BandSpectrumStrip"
import ControlBar from "./ControlBar"
import FilterSheet from "./FilterSheet"
import SurveyCard from "./SurveyCard"
import SurveyPeek from "./SurveyPeek"
import ChartView from "./ChartView"
import {
  STATUS_COLORS,
  BAND_LABELS_LONG,
  BAND_COLORS,
  DEFAULT_STATUSES,
  parseBandParam,
  parsePlotTypeParam,
  parseStatusesParam,
  type Survey,
  type BandId,
  type AxisKey,
  type PlotType,
  type ExplorerAction,
} from "./constants"
import { parseAxisParam } from "./plotting"

// Bands that have a meaningful wavelength center — auto-switch xAxis on select
const WAVELENGTH_BANDS = new Set<BandId>(["radio", "sub_mm", "infrared", "optical", "uv", "xray", "gamma"])

// ── State / Reducer ────────────────────────────────────────────────────────────

interface ExplorerState {
  view: "directory" | "chart"
  band: BandId
  checkedStatuses: string[]
  selectedOperators: string[]
  xAxis: AxisKey
  yAxis: AxisKey
  hoverSlug: string | null
  focusSlug: string | null
  modalSlug: string | null // drives SurveyPeek selectedSlug
  search: string
  plotType: PlotType
}

function makeInitial(params: URLSearchParams): ExplorerState {
  const statusesParam = params.get("statuses")
  const rawView = params.get("view")
  let view: "directory" | "chart" = "directory"
  if (rawView === "chart" || rawView === "explorer") {
    view = "chart"
  } else if (rawView === "directory" || rawView === "list") {
    view = "directory"
  }

  return {
    view,
    band: parseBandParam(params.get("band"), "all"),
    checkedStatuses: parseStatusesParam(statusesParam),
    selectedOperators: params.get("operators")?.split(",").filter(Boolean) || [],
    xAxis: parseAxisParam(params.get("xaxis"), "wavelength_center_um"),
    yAxis: parseAxisParam(params.get("yaxis"), "z_max"),
    focusSlug: null,
    hoverSlug: null,
    modalSlug: null,
    search: params.get("q") || "",
    plotType: parsePlotTypeParam(params.get("plottype"), "wavelength_redshift"),
  }
}

function reducer(state: ExplorerState, action: ExplorerAction): ExplorerState {
  switch (action.type) {
    case "SET_VIEW": return { ...state, view: action.view }
    case "SET_BAND": return {
      ...state,
      band: action.band,
      xAxis: WAVELENGTH_BANDS.has(action.band) ? "wavelength_center_um" : state.xAxis,
    }
    case "TOGGLE_STATUS": {
      const has = state.checkedStatuses.includes(action.status)
      return { ...state, checkedStatuses: has ? state.checkedStatuses.filter(s => s !== action.status) : [...state.checkedStatuses, action.status] }
    }
    case "TOGGLE_OPERATOR": {
      const has = state.selectedOperators.includes(action.operator)
      return { ...state, selectedOperators: has ? state.selectedOperators.filter(o => o !== action.operator) : [...state.selectedOperators, action.operator] }
    }
    case "SET_OPERATORS":    return { ...state, selectedOperators: action.operators }
    case "SET_X_AXIS":       return { ...state, xAxis: action.axis }
    case "SET_Y_AXIS":       return { ...state, yAxis: action.axis }
    case "SET_HOVER":        return { ...state, hoverSlug: action.slug }
    case "SET_FOCUS":        return { ...state, focusSlug: action.slug, hoverSlug: action.slug }
    case "SET_MODAL":        return { ...state, modalSlug: action.slug }
    case "SET_SEARCH":       return { ...state, search: action.search }
    case "SET_PLOT_TYPE":    return { ...state, plotType: action.plotType }
    case "RESET_FILTERS":    return {
      ...state,
      band: "all",
      checkedStatuses: [...DEFAULT_STATUSES],
      selectedOperators: [],
      search: "",
    }
    default:                 return state
  }
}

// ── Main component ─────────────────────────────────────────────────────────────

export default function SurveysView({ surveys }: { surveys: Survey[] }) {
  const searchParams = useSearchParams()
  const router = useRouter()

  const [state, dispatch] = useReducer(reducer, searchParams, makeInitial)
  const [filterSheetOpen, setFilterSheetOpen] = useState(false)

  // Skip URL sync on initial mount to prevent spurious soft navigation
  const isMountedRef = useRef(false)

  // URL sync — only syncs durable filter state, not transient hover/focus.
  useEffect(() => {
    if (!isMountedRef.current) {
      isMountedRef.current = true
      return
    }
    const p = new URLSearchParams()
    const sortedCheckedStatuses = [...state.checkedStatuses].sort()
    const sortedDefaultStatuses = [...DEFAULT_STATUSES].sort()
    if (state.view !== "directory") p.set("view", state.view)
    if (state.band !== "all") p.set("band", state.band)
    if (sortedCheckedStatuses.join(",") !== sortedDefaultStatuses.join(","))
      p.set("statuses", sortedCheckedStatuses.join(","))
    if (state.selectedOperators.length) p.set("operators", state.selectedOperators.join(","))
    if (state.xAxis !== "wavelength_center_um") p.set("xaxis", state.xAxis)
    if (state.yAxis !== "z_max") p.set("yaxis", state.yAxis)
    if (state.search) p.set("q", state.search)
    if (state.plotType !== "wavelength_redshift") p.set("plottype", state.plotType)

    const qs = p.toString()
    const current = typeof window !== "undefined"
      ? new URLSearchParams(window.location.search).toString()
      : ""
    if (qs !== current) {
      router.replace(qs ? `?${qs}` : window.location.pathname, { scroll: false })
    }
  }, [state.view, state.band, state.checkedStatuses,
    state.selectedOperators, state.xAxis, state.yAxis, state.search, state.plotType, router])

  const allOperators = useMemo(
    () => [...new Set(surveys.map(s => s.operator).filter((o): o is string => Boolean(o)))].sort(),
    [surveys]
  )

  // Status+operator filtered (no band filter) — used for counts and PlotB
  const statusOpSurveys = useMemo(() => surveys.filter(s => {
    const statusOk = state.checkedStatuses.includes(s.status)
    const opOk = !state.selectedOperators.length || (!!s.operator && state.selectedOperators.includes(s.operator))
    return statusOk && opOk
  }), [surveys, state.checkedStatuses, state.selectedOperators])

  // Band counts derived from status+op filtered surveys (astrometric maps to multi)
  const bandCounts = useMemo(() => {
    const counts: Record<string, number> = {}
    for (const s of statusOpSurveys) {
      const key = s.wavelength_band === "astrometric" ? "multi" : s.wavelength_band
      counts[key] = (counts[key] ?? 0) + 1
    }
    return counts
  }, [statusOpSurveys])

  // Full filter: band + status + operator + search — used for PlotA and list/directory
  const filteredSurveys = useMemo(() => statusOpSurveys.filter(s => {
    const bandOk = state.band === "all"
      || s.wavelength_band === state.band
      || (state.band === "multi" && s.wavelength_band === "astrometric")

    const query = state.search.trim().toLowerCase()
    const searchOk = !query
      || s.name.toLowerCase().includes(query)
      || s.full_name.toLowerCase().includes(query)
      || (s.operator && s.operator.toLowerCase().includes(query))
      || s.primary_science_goals.toLowerCase().includes(query)

    return bandOk && searchOk
  }), [statusOpSurveys, state.band, state.search])

  const modalSurvey = useMemo(
    () => surveys.find(s => s.slug === state.modalSlug) ?? null,
    [surveys, state.modalSlug]
  )

  const handleOpenPeek = useCallback((slug: string) => {
    dispatch({ type: "SET_MODAL", slug })
  }, [])

  const handleResetFilters = () => {
    dispatch({ type: "RESET_FILTERS" })
  }

  // Count filters active (if anything differs from default list)
  const activeFilterCount = useMemo(() => {
    let count = 0
    if (state.band !== "all") count++
    if (state.selectedOperators.length > 0) count += state.selectedOperators.length
    
    // Status differs from DEFAULT_STATUSES?
    const hasDefaultStatuses = state.checkedStatuses.length === DEFAULT_STATUSES.length &&
      state.checkedStatuses.every(s => DEFAULT_STATUSES.includes(s))
    if (!hasDefaultStatuses) count++

    return count
  }, [state.band, state.checkedStatuses, state.selectedOperators])

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: "1rem", width: "100%" }}>
      {/* 1. Band Spectrum Strip (Primary hero band filter) */}
      <BandSpectrumStrip
        band={state.band}
        bandCounts={bandCounts}
        totalCount={statusOpSurveys.length}
        dispatch={dispatch}
      />

      {/* 2. Control Bar (Directory/Chart segmented control, debounced search, Filters trigger button) */}
      <ControlBar
        view={state.view}
        search={state.search}
        activeFilterCount={activeFilterCount}
        dispatch={dispatch}
        onOpenFilters={() => setFilterSheetOpen(true)}
      />

      {/* 3. Render Active View */}
      {state.view === "directory" ? (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(320px, 1fr))",
            gap: "1rem",
            width: "100%",
          }}
        >
          {filteredSurveys.map(s => (
            <SurveyCard
              key={s.slug}
              survey={s}
              onOpen={handleOpenPeek}
            />
          ))}
          {filteredSurveys.length === 0 && (
            <div style={{ color: "#64748b", textAlign: "center", padding: "4rem 1rem", background: "#1e293b", border: "1px solid #334155", borderRadius: "8px" }}>
              <div style={{ fontSize: "1.5rem", marginBottom: "0.5rem" }}>🔭</div>
              <div style={{ fontSize: "0.875rem", marginBottom: "1rem" }}>No surveys match your active filters.</div>
              <button
                onClick={handleResetFilters}
                style={{
                  background: "#3b82f6", color: "#fff", border: "none",
                  borderRadius: "6px", padding: "0.45rem 1rem", cursor: "pointer",
                  fontSize: "0.82rem", fontWeight: 600
                }}
              >
                Reset Filters
              </button>
            </div>
          )}
        </div>
      ) : (
        <ChartView
          surveys={filteredSurveys}
          band={state.band}
          xAxis={state.xAxis}
          yAxis={state.yAxis}
          hoverSlug={state.hoverSlug}
          selectedSlug={state.modalSlug}
          dispatch={dispatch}
          onSelect={handleOpenPeek}
        />
      )}

      {/* 4. Filter Sheet Popover/Dropdown/Bottom-sheet */}
      <FilterSheet
        open={filterSheetOpen}
        checkedStatuses={state.checkedStatuses}
        selectedOperators={state.selectedOperators}
        allOperators={allOperators}
        dispatch={dispatch}
        onReset={handleResetFilters}
        onClose={() => setFilterSheetOpen(false)}
      />

      {/* 5. Survey Detail Peek Panel/Bottom-sheet */}
      <SurveyPeek
        survey={modalSurvey}
        onClose={() => dispatch({ type: "SET_MODAL", slug: null })}
      />
    </div>
  )
}

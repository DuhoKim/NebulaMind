export type BandId = "all" | "radio" | "sub_mm" | "infrared" | "optical" | "uv" | "xray" | "gamma" | "multi"
export type AxisKey = "sky_coverage_deg2" | "wavelength_center_um" | "z_max" | "dr_year" | "data_volume_tb"
export type PlotType = "coverage_year" | "wavelength_redshift" | "depth_sources"

export interface Survey {
  id: number
  slug: string
  name: string
  full_name: string
  description: string
  emoji: string | null
  logo_url: string | null
  logo_bg: "any" | "dark" | "light" | null
  wavelength_range: string
  wavelength_band: string
  sky_coverage_deg2: number | null
  sky_coverage_note: string | null
  redshift_range: string | null
  instruments: string[]
  current_data_release: string | null
  data_volume: string | null
  primary_science_goals: string
  flagship_programs: string[]
  operator: string | null
  status: string
  archive_url: string | null
  mission_url: string | null
  wavelength_center_um: number | null
  z_max: number | null
  dr_year: number | null
  data_volume_tb: number | null
  limiting_magnitude: number | null
  num_sources_count: number | null
  linked_research_ideas_count: number
  quality_score: number | null
  updated_at: string | null
}

export type ExplorerAction =
  | { type: "SET_VIEW"; view: "directory" | "chart" }
  | { type: "SET_BAND"; band: BandId }
  | { type: "TOGGLE_STATUS"; status: string }
  | { type: "TOGGLE_OPERATOR"; operator: string }
  | { type: "SET_OPERATORS"; operators: string[] }
  | { type: "SET_X_AXIS"; axis: AxisKey }
  | { type: "SET_Y_AXIS"; axis: AxisKey }
  | { type: "SET_HOVER"; slug: string | null }
  | { type: "SET_FOCUS"; slug: string | null }
  | { type: "SET_MODAL"; slug: string | null }
  | { type: "SET_SEARCH"; search: string }
  | { type: "SET_PLOT_TYPE"; plotType: PlotType }
  | { type: "RESET_FILTERS" }

export const BAND_COLORS: Record<string, string> = {
  radio:       "#ef4444",
  sub_mm:      "#f97316",
  infrared:    "#d97706",
  optical:     "#3b82f6",
  uv:          "#8b5cf6",
  xray:        "#c026d3",
  gamma:       "#22c55e",
  astrometric: "#94a3b8",
  multi:       "#14b8a6",
}

export const STATUS_COLORS: Record<string, { bg: string; color: string; label: string }> = {
  operational:   { bg: "rgba(34,197,94,0.12)",   color: "#22c55e", label: "Operational"   },
  commissioning: { bg: "rgba(234,179,8,0.12)",   color: "#ca8a04", label: "Commissioning" },
  planned:       { bg: "rgba(99,102,241,0.12)",  color: "#818cf8", label: "Planned"        },
  retired:       { bg: "rgba(100,116,139,0.12)", color: "#64748b", label: "Retired"        },
}

export const BAND_LABELS_LONG: Record<string, string> = {
  radio: "Radio",
  sub_mm: "Sub-mm",
  infrared: "Infrared",
  optical: "Optical",
  uv: "UV",
  xray: "X-ray",
  gamma: "Gamma",
  astrometric: "Astrometric",
  multi: "Multi-wavelength",
}

export const BAND_LABELS_SHORT: Record<string, string> = {
  radio: "Radio",
  sub_mm: "Sub-mm",
  infrared: "IR",
  optical: "Opt",
  uv: "UV",
  xray: "X-ray",
  gamma: "γ",
  astrometric: "Astro",
  multi: "Multi",
}

export const BAND_ORDER: BandId[] = ["radio", "sub_mm", "infrared", "optical", "uv", "xray", "gamma", "multi"]
export const BAND_IDS: BandId[] = ["all", ...BAND_ORDER]

export const DEFAULT_STATUSES = ["operational", "commissioning", "planned", "retired"]
export const PLOT_TYPES: PlotType[] = ["coverage_year", "wavelength_redshift", "depth_sources"]

export function isBandId(value: string | null): value is BandId {
  return value != null && BAND_IDS.includes(value as BandId)
}

export function parseBandParam(value: string | null, fallback: BandId = "all"): BandId {
  return isBandId(value) ? value : fallback
}

export function isStatusId(value: string | null): value is string {
  return value != null && Object.prototype.hasOwnProperty.call(STATUS_COLORS, value)
}

export function parseStatusesParam(value: string | null): string[] {
  if (!value) return DEFAULT_STATUSES
  const statuses = Array.from(new Set(
    value
      .split(",")
      .map(status => status.trim())
      .filter(isStatusId)
  ))
  return statuses.length > 0 ? statuses : DEFAULT_STATUSES
}

export function isPlotType(value: string | null): value is PlotType {
  return value != null && PLOT_TYPES.includes(value as PlotType)
}

export function parsePlotTypeParam(value: string | null, fallback: PlotType = "wavelength_redshift"): PlotType {
  return isPlotType(value) ? value : fallback
}

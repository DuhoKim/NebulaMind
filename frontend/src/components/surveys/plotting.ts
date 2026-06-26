import { bandUnit, convertUm } from "@/lib/wavelengthUnits"
import type { AxisKey, BandId, Survey } from "./constants"

export const AXIS_OPTIONS: {
  key: AxisKey; baseLabel: string; unit: string; scale: "log" | "linear"
}[] = [
  { key: "sky_coverage_deg2",    baseLabel: "Sky Coverage",    unit: "deg²", scale: "log"    },
  { key: "wavelength_center_um", baseLabel: "Wavelength",      unit: "μm",   scale: "log"    },
  { key: "z_max",                baseLabel: "Redshift Max",    unit: "",     scale: "log"    },
  { key: "dr_year",              baseLabel: "Data Release Yr", unit: "",     scale: "linear" },
  { key: "data_volume_tb",       baseLabel: "Data Volume",     unit: "TB",   scale: "log"    },
]

export function getAxisOption(axis: AxisKey) {
  return AXIS_OPTIONS.find(option => option.key === axis)
}

export function isAxisKey(value: string | null): value is AxisKey {
  return value != null && AXIS_OPTIONS.some(option => option.key === value)
}

export function parseAxisParam(value: string | null, fallback: AxisKey): AxisKey {
  return isAxisKey(value) ? value : fallback
}

export function getAxisUnit(axis: AxisKey, band: BandId): string {
  const option = getAxisOption(axis)
  if (axis === "wavelength_center_um" && band !== "all") return bandUnit(band)
  return option?.unit ?? ""
}

export function getAxisLabel(axis: AxisKey, band: BandId): string {
  const option = getAxisOption(axis)
  if (!option) return ""
  const unit = getAxisUnit(axis, band)
  return option.baseLabel + (unit ? ` (${unit})` : "")
}

export function getSurveyAxisValue(survey: Survey, axis: AxisKey, band: BandId): number | null {
  const value = survey[axis] as number | null
  if (value == null) return null
  if (axis === "wavelength_center_um" && band !== "all") return convertUm(value, band)
  return value
}

export function surveyHasPlottableAxisValue(survey: Survey, axis: AxisKey, band: BandId): boolean {
  const value = getSurveyAxisValue(survey, axis, band)
  if (value == null) return false
  const option = getAxisOption(axis)
  return option?.scale === "log" ? value > 0 : true
}

export function surveyHasPlottableAxes(survey: Survey, xAxis: AxisKey, yAxis: AxisKey, band: BandId): boolean {
  return surveyHasPlottableAxisValue(survey, xAxis, band) && surveyHasPlottableAxisValue(survey, yAxis, band)
}

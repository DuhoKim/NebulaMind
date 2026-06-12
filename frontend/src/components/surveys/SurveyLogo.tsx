"use client"

import { useState } from "react"
import { BAND_COLORS } from "./constants"

interface SurveyLogoSurvey {
  slug: string
  name: string
  wavelength_band: string
  logo_url: string | null
  logo_bg: "any" | "dark" | "light" | null
}

interface Props {
  survey: SurveyLogoSurvey
  size?: "card" | "peek"
}

export default function SurveyLogo({ survey, size = "card" }: Props) {
  const [failed, setFailed] = useState(false)
  const bandColor = BAND_COLORS[survey.wavelength_band] ?? "#818cf8"
  const slot = size === "peek"
    ? { width: 44, height: 44, maxImageWidth: 88, maxImageHeight: 36, fontSize: "0.78rem" }
    : { width: 48, height: 48, maxImageWidth: 96, maxImageHeight: 48, fontSize: "0.82rem" }
  const logoUrl = !failed ? survey.logo_url : null

  if (logoUrl) {
    const image = (
      <img
        src={logoUrl}
        alt={`${survey.name} logo`}
        loading="lazy"
        onError={() => setFailed(true)}
        style={{
          width: "auto",
          height: "auto",
          maxWidth: slot.maxImageWidth,
          maxHeight: slot.maxImageHeight,
          objectFit: "contain",
          display: "block",
        }}
      />
    )

    if (survey.logo_bg === "light") {
      return (
        <span
          style={{
            width: slot.width,
            height: slot.height,
            minWidth: slot.width,
            borderRadius: 6,
            background: "#e2e8f0",
            padding: 4,
            display: "inline-flex",
            alignItems: "center",
            justifyContent: "center",
            overflow: "hidden",
          }}
        >
          {image}
        </span>
      )
    }

    return (
      <span
        style={{
          width: slot.width,
          height: slot.height,
          minWidth: slot.width,
          display: "inline-flex",
          alignItems: "center",
          justifyContent: "center",
          overflow: "visible",
        }}
      >
        {image}
      </span>
    )
  }

  return (
    <span
      title={`${survey.name} has no official logo`}
      style={{
        width: slot.width,
        height: slot.height,
        minWidth: slot.width,
        borderRadius: 6,
        background: hexToRgba(bandColor, 0.2),
        border: `1px solid ${bandColor}`,
        color: bandColor,
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: slot.fontSize,
        fontWeight: 700,
        letterSpacing: "0.02em",
        userSelect: "none",
      }}
    >
      {survey.slug.slice(0, 2).toUpperCase()}
    </span>
  )
}

function hexToRgba(hex: string, alpha: number) {
  const clean = hex.replace("#", "")
  if (clean.length !== 6) return `rgba(129, 140, 248, ${alpha})`
  const r = parseInt(clean.slice(0, 2), 16)
  const g = parseInt(clean.slice(2, 4), 16)
  const b = parseInt(clean.slice(4, 6), 16)
  return `rgba(${r}, ${g}, ${b}, ${alpha})`
}

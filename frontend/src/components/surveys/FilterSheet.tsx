"use client"

import { useEffect, useRef } from "react"
import { STATUS_COLORS, type ExplorerAction } from "./constants"

interface Props {
  open: boolean
  checkedStatuses: string[]
  selectedOperators: string[]
  allOperators: string[]
  dispatch: React.Dispatch<ExplorerAction>
  onReset: () => void
  onClose: () => void
}

const STATUSES = [
  { id: "operational",   label: "Operational",  color: "#22c55e" },
  { id: "commissioning", label: "Commissioning", color: "#ca8a04" },
  { id: "planned",       label: "Planned",       color: "#818cf8" },
  { id: "retired",       label: "Retired",       color: "#64748b" },
]

export default function FilterSheet({
  open,
  checkedStatuses,
  selectedOperators,
  allOperators,
  dispatch,
  onReset,
  onClose,
}: Props) {
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!open) return
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose()
    }
    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [open, onClose])

  if (!open) return null

  return (
    <div
      className="filter-sheet__backdrop"
      style={{
        position: "fixed",
        inset: 0,
        zIndex: 990,
        background: "rgba(0, 0, 0, 0.6)",
        display: "flex",
        alignItems: "flex-end", // Mobile bottom sheet placement
        justifyContent: "center",
      }}
      onClick={onClose}
    >
      <style jsx global>{`
        .filter-sheet__backdrop {
          backdrop-filter: blur(2px);
          animation: filterFadeIn 150ms ease-out forwards;
        }
        .filter-sheet__content {
          animation: filterSlideUp 200ms cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        @keyframes filterFadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        @keyframes filterSlideUp {
          from { transform: translateY(100%); }
          to { transform: translateY(0); }
        }
        @media (min-width: 768px) {
          .filter-sheet__backdrop {
            align-items: center !important;
          }
          .filter-sheet__content {
            animation: filterScaleIn 150ms ease-out forwards !important;
            border-radius: 12px !important;
            max-width: 420px !important;
            height: auto !important;
            max-height: 80vh !important;
          }
        }
        @keyframes filterScaleIn {
          from { opacity: 0; transform: scale(0.96); }
          to { opacity: 1; transform: scale(1); }
        }
      `}</style>

      <div
        id="surveys-filter-sheet"
        role="dialog"
        aria-modal="true"
        aria-labelledby="surveys-filter-sheet-title"
        ref={containerRef}
        className="filter-sheet__content"
        style={{
          background: "#0f172a",
          border: "1px solid #1e293b",
          borderTopLeftRadius: "16px",
          borderTopRightRadius: "16px",
          width: "100%",
          maxHeight: "75vh",
          overflowY: "auto",
          padding: "1.5rem",
          position: "relative",
          boxShadow: "0 -10px 25px -5px rgba(0, 0, 0, 0.5), 0 20px 25px -5px rgba(0, 0, 0, 0.5)",
          display: "flex",
          flexDirection: "column",
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header Row */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: "1.25rem",
            paddingBottom: "0.5rem",
            borderBottom: "1px solid #1e293b",
          }}
        >
          <h4 id="surveys-filter-sheet-title" style={{ margin: 0, fontSize: "0.95rem", fontWeight: 700, color: "#f8fafc" }}>Filters</h4>
          <div style={{ display: "flex", gap: "0.5rem" }}>
            <button
              onClick={onReset}
              style={{
                background: "none",
                border: "none",
                color: "#3b82f6",
                fontSize: "0.75rem",
                fontWeight: 600,
                cursor: "pointer",
                padding: "0.25rem 0.5rem",
              }}
              className="hover:underline"
            >
              Reset
            </button>
            <button
              onClick={onClose}
              style={{
                background: "none",
                border: "none",
                color: "#64748b",
                fontSize: "0.75rem",
                fontWeight: 600,
                cursor: "pointer",
                padding: "0.25rem 0.5rem",
              }}
              className="hover:text-slate-200"
            >
              Done
            </button>
          </div>
        </div>

        {/* Content Body */}
        <div style={{ flex: 1, overflowY: "auto", display: "flex", flexDirection: "column", gap: "1.5rem" }}>
          {/* Status Checkboxes */}
          <div>
            <h5 style={{ margin: "0 0 0.5rem 0", fontSize: "0.78rem", fontWeight: 700, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.05em" }}>
              Status
            </h5>
            <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
              {STATUSES.map((st) => {
                const checked = checkedStatuses.includes(st.id)
                return (
                  <label
                    key={st.id}
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: "0.6rem",
                      fontSize: "0.82rem",
                      color: checked ? "#f8fafc" : "#cbd5e1",
                      cursor: "pointer",
                      userSelect: "none",
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={checked}
                      onChange={() => dispatch({ type: "TOGGLE_STATUS", status: st.id })}
                      style={{
                        width: "15px",
                        height: "15px",
                        accentColor: st.color,
                        cursor: "pointer",
                      }}
                    />
                    <span
                      style={{
                        display: "inline-block",
                        width: "6px",
                        height: "6px",
                        borderRadius: "50%",
                        backgroundColor: st.color,
                      }}
                    />
                    <span>{st.label}</span>
                  </label>
                )
              })}
            </div>
          </div>

          {/* Operator Dropdown/List */}
          <div>
            <h5 style={{ margin: "0 0 0.5rem 0", fontSize: "0.78rem", fontWeight: 700, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.05em" }}>
              Operator
            </h5>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                gap: "0.4rem",
                maxHeight: "180px",
                overflowY: "auto",
                border: "1px solid #1e293b",
                borderRadius: "6px",
                padding: "0.5rem",
                background: "#090d16",
              }}
            >
              {allOperators.map((op) => {
                const checked = selectedOperators.includes(op)
                return (
                  <label
                    key={op}
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: "0.5rem",
                      fontSize: "0.78rem",
                      color: checked ? "#f8fafc" : "#cbd5e1",
                      cursor: "pointer",
                      userSelect: "none",
                      padding: "0.25rem",
                      borderRadius: "4px",
                    }}
                    className="hover:bg-slate-800"
                  >
                    <input
                      type="checkbox"
                      checked={checked}
                      onChange={() => dispatch({ type: "TOGGLE_OPERATOR", operator: op })}
                      style={{
                        width: "14px",
                        height: "14px",
                        accentColor: "#3b82f6",
                        cursor: "pointer",
                      }}
                    />
                    <span>{op}</span>
                  </label>
                )
              })}
              {allOperators.length === 0 && (
                <div style={{ fontSize: "0.75rem", color: "#64748b", padding: "0.5rem", textAlign: "center" }}>
                  No operators available
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

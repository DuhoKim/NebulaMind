"use client"

import { useEffect, useState, useRef } from "react"
import type { ExplorerAction } from "./constants"

interface Props {
  view: "directory" | "chart"
  search: string
  activeFilterCount: number
  dispatch: React.Dispatch<ExplorerAction>
  onOpenFilters: () => void
}

export default function ControlBar({ view, search, activeFilterCount, dispatch, onOpenFilters }: Props) {
  const [localSearch, setLocalSearch] = useState(search)
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  // Keep local search in sync if prop changes from outside (e.g. reset)
  useEffect(() => {
    setLocalSearch(search)
  }, [search])

  const handleSearchChange = (val: string) => {
    setLocalSearch(val)
    if (timerRef.current) clearTimeout(timerRef.current)
    timerRef.current = setTimeout(() => {
      dispatch({ type: "SET_SEARCH", search: val })
    }, 150)
  }

  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
    }
  }, [])

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
        gap: "0.75rem",
        marginBottom: "1rem",
        width: "100%",
        flexWrap: "wrap",
      }}
    >
      <style jsx>{`
        .control-bar__toggle {
          display: flex;
          background: #0f172a;
          border: 1px solid #1e293b;
          border-radius: 6px;
          padding: 2px;
        }
        .control-bar__toggle-btn {
          padding: 0.4rem 1rem;
          font-size: 0.8rem;
          font-weight: 500;
          color: #64748b;
          background: transparent;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          transition: all 120ms;
        }
        .control-bar__toggle-btn--active {
          color: #f8fafc;
          background: #1e293b;
          box-shadow: inset 0 0 0 1px #334155;
          font-weight: 600;
        }
        .control-bar__search {
          flex: 1 1 auto;
          min-width: 180px;
          position: relative;
        }
        .control-bar__search-input {
          width: 100%;
          padding: 0.4rem 1rem 0.4rem 2.25rem;
          font-size: 0.82rem;
          color: #f8fafc;
          background: #0f172a;
          border: 1px solid #1e293b;
          border-radius: 6px;
          outline: none;
          transition: border-color 120ms;
        }
        .control-bar__search-input:focus {
          border-color: #3b82f6;
        }
        .control-bar__search-icon {
          position: absolute;
          left: 0.75rem;
          top: 50%;
          transform: translateY(-50%);
          color: #475569;
          font-size: 0.85rem;
          pointer-events: none;
        }
        .control-bar__filter-btn {
          display: flex;
          align-items: center;
          gap: 0.4rem;
          padding: 0.4rem 1rem;
          font-size: 0.82rem;
          font-weight: 600;
          color: #cbd5e1;
          background: #0f172a;
          border: 1px solid #1e293b;
          border-radius: 6px;
          cursor: pointer;
          transition: all 120ms;
          white-space: nowrap;
        }
        .control-bar__filter-btn:hover {
          background: #1e293b;
          border-color: #334155;
          color: #f8fafc;
        }
        .control-bar__filter-btn--active {
          border-color: #3b82f6;
          color: #3b82f6;
          background: rgba(59, 130, 246, 0.04);
        }
        .control-bar__badge {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          background: #3b82f6;
          color: #ffffff;
          font-size: 0.68rem;
          font-weight: 700;
          height: 16px;
          min-width: 16px;
          padding: 0 4px;
          border-radius: 99px;
          line-height: 1;
        }
        @media (max-width: 580px) {
          .control-bar__search {
            order: 3;
            width: 100%;
          }
        }
      `}</style>

      {/* Directory | Chart Segmented Toggle */}
      <div className="control-bar__toggle">
        <button
          className={`control-bar__toggle-btn ${view === "directory" ? "control-bar__toggle-btn--active" : ""}`}
          onClick={() => dispatch({ type: "SET_VIEW", view: "directory" })}
        >
          Directory
        </button>
        <button
          className={`control-bar__toggle-btn ${view === "chart" ? "control-bar__toggle-btn--active" : ""}`}
          onClick={() => dispatch({ type: "SET_VIEW", view: "chart" })}
        >
          Chart
        </button>
      </div>

      {/* Search Bar */}
      <div className="control-bar__search">
        <span className="control-bar__search-icon">🔍</span>
        <input
          type="text"
          className="control-bar__search-input"
          placeholder="Search name, operator, goals..."
          value={localSearch}
          onChange={(e) => handleSearchChange(e.target.value)}
        />
      </div>

      {/* Filters Sheet Trigger Button */}
      <button
        className={`control-bar__filter-btn ${activeFilterCount > 0 ? "control-bar__filter-btn--active" : ""}`}
        onClick={onOpenFilters}
      >
        <span>Filters</span>
        {activeFilterCount > 0 && <span className="control-bar__badge">{activeFilterCount}</span>}
      </button>
    </div>
  )
}

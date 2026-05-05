"use client";
import { useEffect } from "react";

export default function VisitTracker() {
  useEffect(() => {
    fetch("/api/stats/visit?path=" + encodeURIComponent(window.location.pathname), {
      method: "POST",
    }).catch(() => {});
  }, []);
  return null;
}

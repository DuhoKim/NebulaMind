import type { Metadata } from "next";
import PaperProfileClient from "./PaperProfileClient";

export const metadata: Metadata = {
  title: "Paper Profile — NebulaMind",
  description: "Read-only wiki-wide footprint profile for one indexed paper.",
};

export default function PaperProfilePage({ params }: { params: { paperId: string } }) {
  return <PaperProfileClient paperId={decodeURIComponent(params.paperId)} />;
}

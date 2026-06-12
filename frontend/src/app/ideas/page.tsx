import type { Metadata } from "next";
import IdeasIndexClient from "./IdeasIndexClient";

export const metadata: Metadata = {
  title: "Research Ideas — NebulaMind",
  description: "Browse AI-generated astronomy research ideas linked to NebulaMind wiki claims.",
};

export default function IdeasIndexPage() {
  return <IdeasIndexClient />;
}

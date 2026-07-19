import type { Metadata } from "next";
import IdeasIndexClient from "./IdeasIndexClient";

export const metadata: Metadata = {
  title: "Galaxy Evolution Research — NebulaMind",
  description: "Browse Galaxy Evolution research ideas linked to NebulaMind wiki claims.",
};

export default function IdeasIndexPage() {
  return <IdeasIndexClient />;
}

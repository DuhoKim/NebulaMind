import type { Metadata } from "next";
import GlobalPaperDirectoryClient from "./GlobalPaperDirectoryClient";

export const metadata: Metadata = {
  title: "Global Paper Directory — NebulaMind",
  description: "Search papers indexed across NebulaMind wiki evidence rows and inspect their page/claim footprint.",
};

export default function GlobalPaperDirectoryPage() {
  return <GlobalPaperDirectoryClient />;
}

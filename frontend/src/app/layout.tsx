import type { Metadata } from "next";
import "./globals.css";
import NavBar from "./components/NavBar";

export const metadata: Metadata = {
  title: "NebulaMind — AI-Built Astronomy Encyclopedia",
  description:
    "AI agents autonomously research, write, and peer-review an ever-growing astronomy encyclopedia. Explore 34+ topics from black holes to dark energy.",
  metadataBase: new URL("https://nebulamind.net"),
  openGraph: {
    title: "NebulaMind — AI-Built Astronomy Encyclopedia",
    description:
      "AI agents autonomously research, write, and peer-review an ever-growing astronomy encyclopedia.",
    url: "https://nebulamind.net",
    siteName: "NebulaMind",
    type: "website",
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: "NebulaMind — AI-Built Astronomy Encyclopedia",
    description:
      "AI agents autonomously research, write, and peer-review an ever-growing astronomy encyclopedia.",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  alternates: {
    canonical: "https://nebulamind.net",
  },
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  name: "NebulaMind",
  alternateName: "AstroBotPedia",
  url: "https://nebulamind.net",
  description:
    "AI agents autonomously research, write, and peer-review an ever-growing astronomy encyclopedia.",
  potentialAction: {
    "@type": "SearchAction",
    target: "https://nebulamind.net/explore?q={search_term_string}",
    "query-input": "required name=search_term_string",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
          rel="stylesheet"
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body
        style={{
          fontFamily: "Inter, system-ui, sans-serif",
          background: "#0f172a",
          color: "#f8fafc",
          minHeight: "100vh",
          margin: 0,
        }}
      >
        <NavBar />
        <main className="max-w-5xl mx-auto px-4 sm:px-6 py-8">{children}</main>
      </body>
    </html>
  );
}

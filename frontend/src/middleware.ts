import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

// Forwards the resolved app pathname as `x-pathname` so the root layout can give
// the AI-Scientist homepage a standalone (chrome-free) presentation.
function forward(req: NextRequest, appPath: string) {
  const headers = new Headers(req.headers);
  headers.set("x-pathname", appPath);
  return NextResponse.next({ request: { headers } });
}

export function middleware(req: NextRequest) {
  const host = (req.headers.get("host") || "").toLowerCase();
  const { pathname, search } = req.nextUrl;

  // The Lab became the main site; lab.nebulamind.net permanently redirects to canonical.
  if (host.startsWith("lab.")) {
    return NextResponse.redirect(`https://nebulamind.net${pathname}${search}`, 308);
  }

  return forward(req, pathname);
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};

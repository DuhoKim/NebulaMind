import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

// - Routes the lab.nebulamind.net subdomain: only the Lab landing is served there;
//   every other path redirects to the canonical nebulamind.net.
// - Forwards the resolved app pathname as `x-pathname` so the root layout can give
//   /lab a standalone (chrome-free) presentation.
function forward(req: NextRequest, appPath: string) {
  const headers = new Headers(req.headers);
  headers.set("x-pathname", appPath);
  return NextResponse.next({ request: { headers } });
}

export function middleware(req: NextRequest) {
  const host = (req.headers.get("host") || "").toLowerCase();
  const { pathname, search } = req.nextUrl;

  if (host.startsWith("lab.")) {
    // front door -> the Lab landing
    if (pathname === "/") {
      const url = req.nextUrl.clone();
      url.pathname = "/lab";
      const headers = new Headers(req.headers);
      headers.set("x-pathname", "/lab");
      return NextResponse.rewrite(url, { request: { headers } });
    }
    // the Lab route, its API calls, and framework assets serve locally
    if (
      pathname === "/lab" ||
      pathname.startsWith("/lab/") ||
      pathname.startsWith("/api/") ||
      pathname.startsWith("/_next/") ||
      pathname === "/favicon.ico"
    ) {
      return forward(req, pathname);
    }
    // anything else belongs to the main site
    return NextResponse.redirect(`https://nebulamind.net${pathname}${search}`, 308);
  }

  return forward(req, pathname);
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};

"""study_renderer package.

V33: this initialiser used to import from `.renderer`, the V13 renderer superseded in V19, so
`import study_renderer.renderer_v3` first loaded the OLD module and the package-level
`render_cutout` was the old one -- a stale import in a file no pin covered. A referee found it
by inspecting sys.modules. It now exports the pinned renderer's symbols and nothing else, and it
is pinned like every other executed file.
"""
from .renderer_v4 import Raster, RenderTarget, render_cutout  # noqa: F401  (V37: renderer_v4 supersedes renderer_v3)

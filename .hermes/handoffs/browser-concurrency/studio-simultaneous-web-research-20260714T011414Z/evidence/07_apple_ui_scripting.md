# Apple UI-scripting evidence
URL: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html
Accessed: 2026-07-14
Product/version: Apple Mac Automation Scripting Guide, updated 2016-06-13

> A user interface script simulates user interaction, such as mouse clicks and keystrokes.

> The user must manually enable it on an app-by-app (including script apps) basis.

> Once you know how an element fits into an interface, you target it within that hierarchy. For example, `button X of window Y of process Z`.

Official docs support process/window/element targeting. They do not establish safe simultaneous writes to one app/window; generic keystroke globality is therefore PARTIAL, not inferred.

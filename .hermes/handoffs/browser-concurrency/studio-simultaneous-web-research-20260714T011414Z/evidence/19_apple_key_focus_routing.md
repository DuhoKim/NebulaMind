# Apple key-event focus-routing evidence
URL: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/EventArchitecture/EventArchitecture.html
Accessed: 2026-07-14
Product/version: Apple Cocoa Event Handling Guide, updated 2016-09-13

> It dispatches most key events to the first responder of the key window.

> Such actions are sent to the first responder.

Verdict: VERIFIED for ordinary Cocoa key-event focus routing. Combined with Apple's UI-scripting documentation, untargeted System Events keystrokes must not be treated as independent per-agent channels.

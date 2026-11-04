---
version: alpha
colors:
  primary: "#ff5877"
  background: "#06111c"
  surface: "#0b1c2b"
  surfaceRaised: "#0e2233"
  text: "#eaf3fb"
  muted: "#9fb3c4"
  accent: "#5fd6e8"
  evidence: "#8fb9d4"
  signal: "#f5c584"
typography:
  body:
    fontFamily: "DM Sans, Inter, system-ui, sans-serif"
  data:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
rounded:
  control: "10px"
  panel: "13px"
spacing:
  compact: "8px"
  control: "12px"
  panel: "18px"
components:
  evidenceMap:
    backgroundColor: "surface"
    textColor: "text"
    rounded: "panel"
  archiveSignal:
    backgroundColor: "surfaceRaised"
    textColor: "text"
    rounded: "control"
---

## Overview

Influence Atlas is a dense public-record research interface for readers tracing declared relationships. Its register is investigative product UI: dark, restrained, and legible under high information density. Its visual reference is a rain-lit evidence terminal: neon-noir atmosphere at the edges, precise records at the center—not a generic data dashboard.

The signatures are the guided evidence map and the landing-page archive signal: a restrained live readout that follows the currently selected record. In directional stages, relationship lanes should make the reading order explicit: inputs at left, focal entities at center, and supporting context at right.

## Colors

Use `background` and `surface` for the layered night-blue workspace. `primary` is the magenta-red signal used for archival urgency and active record illumination; `accent` cyan marks navigation and active technical state; `signal` amber is reserved for identifiers and caution. Evidence connections use the subdued blue `evidence`, so they do not compete with entity colors. Do not use shared infrastructure color as proof of affiliation.

## Typography

Use DM Sans for names and explanations. Use IBM Plex Mono for identifiers, cluster labels, counts, and stage navigation. Keep relationship labels concise and factual.

## Layout

The persistent sidebar supports filtering; the canvas owns exploration. Guided stages may change node geometry when it improves comprehension. Stage 02 uses a three-lane map rather than a radial cluster: principals/brokers, registrants, then websites/owners/corporate context.

## Elevation & Depth

Panels use subtle borders and translucent dark fills. Use a neon glow only for an active physical metaphor—an active rack module, status signal, or transit layer—not for ordinary content. Avoid decorative shadows inside the graph; depth comes from spatial separation and line weight.

## Shapes

Controls are compact rounded rectangles. Entity nodes remain circular to preserve the map’s existing visual language.

## Components

The native connection-visibility select remains the canonical selector because its platform popup behavior is accepted for this static site. Canvas panning always retains zoom controls and the Fit view button as non-drag alternatives.

## Do's and Don'ts

Do use directional spacing and muted evidence lines to make relationships traceable. Do expose names at readable zoom levels in guided stages. Do preserve visible keyboard focus and reduced-motion behavior.

Do not imply ownership, funding, or coordination from shared infrastructure. Do not turn the evidence map into a decorative constellation, use neon as a substitute for hierarchy, or rely on color alone to communicate the pathway.

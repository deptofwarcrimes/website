---
version: alpha
colors:
  primary: "#54d4f3"
  background: "#070e19"
  surface: "#0c1624"
  surfaceRaised: "#111e30"
  text: "#eef4ff"
  muted: "#94a5bc"
  accent: "#54d4f3"
  evidence: "#9acbe0"
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
---

## Overview

Influence Atlas is a dense public-record research interface for readers tracing declared relationships. Its register is investigative product UI: dark, restrained, and legible under high information density. Its visual reference is a case-file evidence board, not a generic data dashboard.

The signature is the guided evidence map. In directional stages, relationship lanes should make the reading order explicit: inputs at left, focal entities at center, and supporting context at right.

## Colors

Use `background` and `surface` for the layered night-blue workspace. Cyan is reserved for active controls and navigation. Evidence connections use the subdued blue `evidence`, so they do not compete with entity colors. Do not use shared infrastructure color as proof of affiliation.

## Typography

Use DM Sans for names and explanations. Use IBM Plex Mono for identifiers, cluster labels, counts, and stage navigation. Keep relationship labels concise and factual.

## Layout

The persistent sidebar supports filtering; the canvas owns exploration. Guided stages may change node geometry when it improves comprehension. Stage 02 uses a three-lane map rather than a radial cluster: principals/brokers, registrants, then websites/owners/corporate context.

## Elevation & Depth

Panels use subtle borders and translucent dark fills. Avoid decorative shadows inside the graph; depth comes from spatial separation and line weight.

## Shapes

Controls are compact rounded rectangles. Entity nodes remain circular to preserve the map’s existing visual language.

## Components

The native connection-visibility select remains the canonical selector because its platform popup behavior is accepted for this static site. Canvas panning always retains zoom controls and the Fit view button as non-drag alternatives.

## Do's and Don'ts

Do use directional spacing and muted evidence lines to make relationships traceable. Do expose names at readable zoom levels in guided stages. Do preserve visible keyboard focus and reduced-motion behavior.

Do not imply ownership, funding, or coordination from shared infrastructure. Do not turn the evidence map into a decorative constellation or rely on color alone to communicate the pathway.

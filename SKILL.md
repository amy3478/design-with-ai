---
name: design-with-ai
description: |
  AI-assisted product design workflow — Figma API access, project context management,
  structured design reviews, flow specs, feature ideation, and prototype generation.
  Use when working on design projects, reviewing designs, building prototypes,
  pulling Figma data, or any task involving product design collaboration.
compatibility: Python 3 for Figma scripts. Optional FIGMA_ACCESS_TOKEN in .env for Figma API access.
metadata:
  version: "1.0"
  author: Amy Pu
---

# Design Companion

A workflow skill for AI-assisted product design. Load this file at the start of any design session to give your AI agent the full context on how to work with you.

## Overview

Two components:
- **This skill** (this repo): workflow instructions, templates, Figma API scripts, references
- **Project context** (`<project>/.design-companion/`): per-project design knowledge

The skill is project-agnostic. Project data lives with the project.

## Figma API Access

Scripts in `figma-scripts/` use the Figma REST API via `FIGMA_ACCESS_TOKEN` from `.env` in the repo root.

### Available Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `figma-file.py` | Get file structure (pages, frames, layers) | `python3 figma-scripts/figma-file.py <file_key> [--depth N]` |
| `figma-styles.py` | Extract design tokens (colors, text styles, effects) | `python3 figma-scripts/figma-styles.py <file_key>` |
| `figma-frames.py` | Export frames as PNG/SVG | `python3 figma-scripts/figma-frames.py <file_key> [--node-ids ID,...] [--format png|svg] [--scale N] [--out DIR]` |
| `figma-components.py` | List published components and their properties | `python3 figma-scripts/figma-components.py <file_key>` |

**File key**: from any Figma URL — `figma.com/design/<FILE_KEY>/...`

## Project Context Convention

When starting design work on a project, init a `.design-companion/` folder:

```
<project-dir>/.design-companion/
├── brief.md            # Product context, users, constraints
├── app-structure.md    # Screens, flows, navigation
├── design-system.md    # Extracted tokens + component inventory
├── decisions.md        # Design decision log with rationale
├── session-handoff.md  # Where last session left off (crash-proof)
└── [topic].md          # Additional context files as needed (roadmap, ia-map, etc.)
```

Use templates from `templates/` to initialize these files.

| Template | Purpose |
|----------|---------|
| `templates/project-brief.md` | Product context, users, constraints |
| `templates/content-spec.md` | Screen-by-screen content specification |
| `templates/design-review.md` | Structured design critique |
| `templates/feature-spec.md` | Feature proposal with tradeoffs |
| `templates/flow-spec.md` | User flow specification |
| `templates/visual-audit.md` | Competitive visual audit framework |
| `templates/prototype-base.html` | Reusable interactive prototype shell |

### Init a New Project

1. Create `<project>/.design-companion/` directory
2. Copy and fill templates from `templates/` folder
3. If Figma file exists, run scripts to populate `design-system.md` and `app-structure.md`
4. The brief is filled from user input (PRD, verbal description, etc.)

## Session Lifecycle

### Resuming a Design Session
**When starting work on a project that has a `.design-companion/` folder:**
1. Read ALL files in `.design-companion/` to load full project context
2. Check for `session-handoff.md` — this captures where the last session left off
3. Summarize current state for the user before diving in

This prevents context loss across sessions. The `.design-companion/` folder IS the project memory.

### During a Design Session
- **Update context files as decisions land** — don't wait until the end
- When a major decision is made, append to `decisions.md` immediately
- When the IA or strategy shifts, update the relevant `.md` file
- For long sessions, do periodic saves (every 3-4 major exchanges)

### Ending a Design Session
- Update `session-handoff.md` with: what was done, what's in progress, what's next
- This file is the crash-proof handoff — a letter to the next session
- Ensure all design artifacts (HTML mockups, etc.) are noted with paths

## Workflow Modes

### 1. Design Review
**Trigger:** User shares screenshots or says "review this"
**Input:** Images (screenshots/exports) + optional context
**Process:**
1. Load project context from `.design-companion/`
2. Analyze against design system, established patterns, and requirements
3. Output structured review using `templates/design-review.md` format

### 2. Flow Specification
**Trigger:** User asks to design a flow or rework navigation
**Input:** Requirements + current state (screenshots or Figma data)
**Process:**
1. Map current flow from project context or Figma API
2. Identify gaps, edge cases, decision points
3. Output numbered flow spec using `templates/flow-spec.md` format

### 3. Feature Ideation
**Trigger:** User describes a problem or new feature need
**Input:** Problem statement + constraints
**Process:**
1. Reference existing app structure and design patterns
2. Propose solutions with tradeoff analysis
3. Output using `templates/feature-spec.md` format

### 4. Figma Data Pull
**Trigger:** User says "pull my Figma data" or "update design system"
**Input:** Figma file URL or key
**Process:**
1. Run relevant scripts to extract structure/styles/components
2. Update `.design-companion/design-system.md` with findings
3. Report what changed

### 5. Prototype Generation
**Trigger:** User asks to "build a prototype", "make it interactive", "I want to test this flow"
**Input:** Design system (`.design-companion/design-system.md`) + content spec (`templates/content-spec.md` format)
**Process:**
1. Read design system tokens and content spec
2. Use `templates/prototype-base.html` as starting point
3. Map design tokens to CSS custom properties
4. Build each screen as a `<div class="screen">` with appropriate HTML/CSS
5. Wire navigation logic (path routing, back buttons, auto-advance timers)
6. Add motion: screen transitions, loading animations, confirmation animations
7. Test all paths: forward flow, back navigation, edge cases

**Output:** Single HTML file. Works on desktop (phone frame) and mobile (fullscreen).

**Key principles:**
- Phone frame on desktop, fullscreen on real phones
- PWA meta tags for home screen install
- Safe area insets for notched devices
- Touch + mouse support for all interactions
- 44px minimum tap targets
- Design tokens as CSS custom properties for easy theming

### 6. Visual Design Generation
**Trigger:** User asks to generate mockups, screen designs, or visual explorations
**Input:** Content spec + design system tokens
**Process:**
1. Read `references/visual-style-guide.md` for structural composition patterns
2. Apply project design tokens from `.design-companion/design-system.md`
3. Generate HTML mockups or structured design specs
4. Follow the style guide's spacing, typography, card anatomy, and shadow conventions

The visual style guide defines **how to compose things** (spacing, hierarchy, structure). The project design system defines **what it looks like** (colors, fonts, brand). Both are needed together.

## Output Principles

- **Actionable over analytical** — specs they can build from, not essays about design theory
- **Reference the design system** — use the project's actual tokens and components
- **Flag edge cases** — empty states, error states, loading states, accessibility
- **Be opinionated** — commit to recommendations, explain tradeoffs, don't hedge everything
- **Log decisions** — every non-trivial choice goes in `decisions.md` with rationale

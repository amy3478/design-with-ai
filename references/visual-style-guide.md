# Visual Style Reference — Structural Patterns

_Derived from shadcn/ui + Tailwind CSS. These are **layout and hierarchy patterns**, not brand/color decisions. Project-specific design systems supply colors, fonts, and brand identity. This guide supplies the bones._

_Use this when generating non-project-specific frames: context scaffolds, presentation decks, reference cards, flow specs, design review artifacts._

## Spacing System

Base unit: **4px**. All spacing is a multiple.

| Token | Value | Use |
|-------|-------|-----|
| `xs` | 4px | Tight inline gaps (icon-to-label) |
| `sm` | 8px | Within-group spacing (list items, bullet points) |
| `md` | 12px | Related element gaps (title-to-subtitle) |
| `lg` | 16px | Standard content padding, paragraph spacing |
| `xl` | 20px | Section header to content |
| `2xl` | 24px | Card internal padding, between card sections |
| `3xl` | 32px | Between major groups within a card |
| `4xl` | 40px | Between cards |
| `5xl` | 48px | Section padding (large containers) |
| `6xl` | 64px | Between sections |

**Rules:**
- Card padding: `2xl` (24px) — consistent on all sides
- Card internal section gap: `2xl` (24px)
- Within a section (e.g., title + items): `sm` (8px) between items, `md` (12px) title-to-first-item
- Between cards: `4xl` (40px)
- Section-level containers: `5xl` (48px) padding

## Typography Scale

Sizes follow a consistent ratio. Weights create hierarchy within each size.

| Token | Size | Weight | Line Height | Use |
|-------|------|--------|-------------|-----|
| `heading-xl` | 36px | Bold (700) | 1.1 | Section titles, hero headings |
| `heading-lg` | 24px | Semibold (600) | 1.2 | Card titles, major headings |
| `heading-md` | 18px | Semibold (600) | 1.3 | Sub-section headings |
| `heading-sm` | 15px | Semibold (600) | 1.4 | Group titles within cards |
| `body` | 14px | Regular (400) | 1.5 | Primary body text, descriptions |
| `body-sm` | 13px | Regular (400) | 1.5 | Secondary text, bullet points |
| `caption` | 12px | Regular (400) | 1.5 | Metadata, dates, labels |
| `overline` | 11px | Medium (500) | 1.4 | Category labels, all-caps tags |
| `display` | 48px | Bold (700) | 1.0 | Project title (one per page) |

**Rules:**
- Never jump more than 2 steps in the scale within a visual group
- `heading-lg` (24px) → `body` (14px) is fine for card title → card description
- `display` (48px) → `body` (14px) needs a `heading-md` (18px) bridge or generous spacing
- Muted text uses the same size but reduced opacity/contrast (the theme's muted color)
- Project-level hero titles can go larger (72–144px) but are one-offs, not part of the system

## Card Anatomy

Cards are the primary container for grouped content. Structure follows shadcn's Card component.

```
┌─ Card ──────────────────────────────────────┐
│  border: 1px solid borderColor              │
│  radius: 12px                               │
│  shadow: 0 1px 3px rgba(0,0,0,0.1),         │
│          0 1px 2px rgba(0,0,0,0.06)          │
│  fill: cardBackground                       │
│  padding: 24px all sides                    │
│                                             │
│  ┌─ Header ──────────────────────────────┐  │
│  │  Title          (heading-lg, 24px)    │  │
│  │                 gap: 8px              │  │
│  │  Description    (body, 14px, muted)   │  │
│  └───────────────────────────────────────┘  │
│                 gap: 24px                   │
│  ┌─ Content ─────────────────────────────┐  │
│  │  Section heading (heading-sm, 15px)   │  │
│  │                   gap: 12px           │  │
│  │  • Item text    (body-sm, 13px)       │  │
│  │  • Item text    gap: 8px between      │  │
│  │  • Item text                          │  │
│  └───────────────────────────────────────┘  │
│                 gap: 24px                   │
│  ┌─ Content ─────────────────────────────┐  │
│  │  (next section, same pattern)         │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

**Rules:**
- Always include a 1px border — this is what separates "designed" from "flat rectangles"
- Shadow is subtle (`shadow-sm`) — just enough to lift the card, not dramatic
- Corner radius: 12px for cards, 8px for nested elements (inner cards, version blocks)
- No border on nested elements — use background color difference instead
- Nested containers: reduce padding to 16px, reduce radius to 8px

## Border & Shadow

| Element | Border | Shadow | Radius |
|---------|--------|--------|--------|
| Card (primary) | 1px solid border color | `shadow-sm` | 12px |
| Nested container | none | none | 8px |
| Section wrapper | none | none | 16px |
| Badge/tag | 1px solid (outline variant) or none (filled) | none | full (9999px) |
| Placeholder/image area | 1px dashed border color | none | 8px |
| Input/interactive area | 1px solid border color | none | 6px |

### Shadow Definitions (for Figma)

| Token | Figma Shadow | When |
|-------|-------------|------|
| `shadow-sm` | X:0 Y:1 Blur:3 Spread:0 `rgba(0,0,0,0.1)` + X:0 Y:1 Blur:2 Spread:-1 `rgba(0,0,0,0.06)` | Cards, elevated containers |
| `shadow-md` | X:0 Y:4 Blur:6 Spread:-1 `rgba(0,0,0,0.1)` + X:0 Y:2 Blur:4 Spread:-2 `rgba(0,0,0,0.06)` | Popovers, dropdowns (rare in scaffolds) |
| `shadow-none` | — | Nested elements, inline content |

## Section Layout

Sections are the top-level organizer (e.g., "Context Framing", "User Flow").

```
┌─ Section ────────────────────────────────────────────────────┐
│  background: surfaceColor (subtle contrast from page bg)     │
│  radius: 16px                                                │
│  padding: 48px                                               │
│                                                              │
│  ┌─ Title Area ──────────────────────────────────────────┐   │
│  │  Section Title    (heading-xl, 36px, bold)            │   │
│  │                   gap: 12px                           │   │
│  │  Description      (body, 14px, muted)                 │   │
│  └───────────────────────────────────────────────────────┘   │
│                      gap: 32px                               │
│  ┌─ Content Area ────────────────────────────────────────┐   │
│  │  Cards / frames / artboards                           │   │
│  │  gap: 40px between cards                              │   │
│  └───────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

## Visual Hierarchy Principles

1. **Contrast through weight, not size.** A 15px semibold heading and 14px regular body text create clear hierarchy without dramatic size jumps.

2. **Muted text is a tool, not a default.** Use it for: descriptions, secondary info, placeholder text, metadata. Primary content stays full contrast.

3. **Borders create structure; shadows create depth.** Use borders to separate same-level items (card from background). Use shadows sparingly to elevate (card above page surface).

4. **White space > dividers.** Prefer spacing to separate groups. Use explicit dividers (1px lines) only when spacing alone is ambiguous.

5. **Consistent rhythm.** If cards use 24px padding, all cards use 24px padding. If section gaps are 64px, all section gaps are 64px. Inconsistency reads as unintentional.

## Badge / Tag Patterns

For labels like phase numbers, status indicators, category tags:

| Variant | Style | Use |
|---------|-------|-----|
| Filled | Background: primary or accent color, text: contrasting, radius: full, px: 8px, py: 2px, text: 12px medium | Active status, current phase |
| Outline | Border: 1px solid border color, text: foreground, same sizing | Neutral labels, categories |
| Muted | Background: muted color, text: muted-foreground, same sizing | Inactive, secondary labels |

## Color Roles (Semantic — Not Specific Values)

The scaffold's `StyleTheme` should map to these roles. Actual RGB values come from the theme (extracted or default).

| Role | What it colors | Derivation hint |
|------|---------------|-----------------|
| `background` | Page / canvas | Base color |
| `foreground` | Primary text | High contrast against background |
| `card` | Card fill | Same as or very slightly offset from background |
| `card-foreground` | Text on cards | Same as foreground |
| `muted` | Muted backgrounds, disabled areas | ~3-5% toward midgray from background |
| `muted-foreground` | Secondary text, descriptions | ~45% opacity feel (blend foreground toward background) |
| `border` | Card borders, dividers | ~8-10% toward foreground from background |
| `accent` | Highlighted areas, hover states | Subtle tint of brand color at low saturation |
| `surface` | Section containers | ~2-3% toward foreground from background |

**Dark mode adjustments:**
- Border becomes lighter (`rgba(255,255,255,0.1)`)
- Muted backgrounds go slightly lighter than background
- Shadows become less visible — borders carry more weight

## JSON Design Generation Guidelines

When generating JSON files for Figma's scaffold plugin "Load Design" feature, follow these patterns to ensure professional, well-structured designs.

### Card Pattern in JSON

A well-structured card uses auto-layout, proper padding, border, shadow, and corner radius:

```json
{
  "type": "frame",
  "name": "Story Card",
  "width": 400,
  "height": 200,
  "cornerRadius": 12,
  "backgroundColor": "#ffffff",
  "borderColor": "#e5e7eb",
  "borderWidth": 1,
  "shadow": "sm",
  "layoutMode": "VERTICAL",
  "padding": 24,
  "itemSpacing": 12,
  "children": [
    {
      "type": "text",
      "name": "Card Title",
      "content": "User Story",
      "fontSize": 24,
      "fontWeight": "semibold",
      "color": "#0f172a"
    },
    {
      "type": "text",
      "name": "Description",
      "content": "As a user, I want to...",
      "fontSize": 14,
      "fontWeight": "regular",
      "color": "#64748b",
      "maxWidth": 352
    }
  ]
}
```

**Key elements:**
- `cornerRadius: 12` for cards (8 for nested elements)
- `borderColor` + `borderWidth: 1` — always include borders
- `shadow: "sm"` for subtle elevation
- `layoutMode: "VERTICAL"` with `padding: 24` and `itemSpacing: 12`
- Text nodes constrained with `maxWidth` (card width minus padding × 2)

### Layout Strategies

Choose the right layout mode for each container:

**Use `layoutMode: "VERTICAL"`** for cards with stacked content:
- Card containers with title + description + content
- Section headers with title + subtitle
- Lists of items arranged top-to-bottom

**Use `layoutMode: "HORIZONTAL"`** for row layouts:
- Card grids (row frames containing cards)
- Set `itemSpacing` between cards (typically 40)
- Wrap multiple row frames in an absolute-positioned container

**Omit `layoutMode`** (absolute positioning) for:
- Top-level presentation frames
- Section containers where elements are placed at specific coordinates
- Complex layouts requiring precise positioning

**Grid pattern structure:**
```
Outer frame (absolute positioning, no layoutMode)
└─ Row frame (layoutMode: "HORIZONTAL", itemSpacing: 40)
   ├─ Card 1 (layoutMode: "VERTICAL", padding: 24)
   ├─ Card 2 (layoutMode: "VERTICAL", padding: 24)
   └─ Card 3 (layoutMode: "VERTICAL", padding: 24)
```

### Typography in JSON

Map the typography scale to JSON properties:

| Style | fontSize | fontWeight | Use |
|-------|----------|-----------|-----|
| `heading-xl` | 36 | `"bold"` | Section titles, hero headings |
| `heading-lg` | 24 | `"semibold"` | Card titles, major headings |
| `heading-md` | 18 | `"semibold"` | Sub-section headings |
| `heading-sm` | 15 | `"semibold"` | Group titles within cards |
| `body` | 14 | `"regular"` | Primary body text, descriptions |
| `body-sm` | 13 | `"regular"` | Secondary text, bullet points |
| `caption` | 12 | `"regular"` | Metadata, dates, labels |

**Additional text properties:**
- `lineHeight`: 1.1–1.5 (smaller for headings, larger for body)
- `letterSpacing`: -0.5 for large headings, 0 for body, 0.5 for uppercase labels
- `maxWidth`: constrain text to prevent overly long lines (card width minus padding)
- `opacity`: 0.6–0.7 for muted text (or use muted color directly)

### Color Conventions

Use semantic hex values for light themes:

| Role | Hex | Use |
|------|-----|-----|
| Background | `#f8fafc` or `#ffffff` | Page/canvas background |
| Card background | `#ffffff` | Card fill |
| Border | `#e5e7eb` | Card borders, dividers |
| Primary text | `#0f172a` or `#1e1e1e` | Headings, body text |
| Muted text | `#64748b` | Secondary text, descriptions |
| Section headers | Project accent | Use extracted brand colors |

**Important:**
- Keep borders visible even on white-on-white cards (`#e5e7eb` provides subtle definition)
- Always include `shadow: "sm"` on cards for depth
- Use project-specific accent colors for section titles and important headings
- Muted text should use gray tones, not just reduced opacity

### Common Anti-patterns

**Don't do these:**

❌ **Relying on background color alone for card boundaries**
```json
{
  "backgroundColor": "#f0f0f0"  // No border = flat rectangle
}
```
✅ Always add `"borderColor": "#e5e7eb"` and `"borderWidth": 1`

❌ **Using layoutMode on top-level frames**
```json
{
  "name": "Presentation",
  "layoutMode": "VERTICAL"  // Collapses grid layout
}
```
✅ Omit `layoutMode` for top-level frames; use absolute positioning

❌ **Excessive corner radius**
```json
{
  "cornerRadius": 24  // Looks dated/bubbly
}
```
✅ Use `12` for cards, `8` for nested elements, `16` maximum for large containers

❌ **No padding on cards**
```json
{
  "padding": 0,  // Content touches edges
  "children": [...]
}
```
✅ Always use `"padding": 24` on cards, `16` minimum on smaller containers

❌ **Uniform text weight**
```json
{
  "fontSize": 24,
  "fontWeight": "regular"  // No hierarchy
}
```
✅ Use weight to create hierarchy: `"semibold"` for headings, `"regular"` for body

### Complete Example

A presentation frame with section title and 3 cards in a row:

```json
{
  "type": "frame",
  "name": "User Stories Overview",
  "width": 1920,
  "height": 1080,
  "backgroundColor": "#f8fafc",
  "children": [
    {
      "type": "text",
      "name": "Section Title",
      "content": "User Stories",
      "x": 100,
      "y": 80,
      "fontSize": 36,
      "fontWeight": "bold",
      "color": "#0f172a"
    },
    {
      "type": "text",
      "name": "Section Description",
      "content": "Core user needs and acceptance criteria",
      "x": 100,
      "y": 132,
      "fontSize": 14,
      "fontWeight": "regular",
      "color": "#64748b"
    },
    {
      "type": "frame",
      "name": "Card Row",
      "x": 100,
      "y": 200,
      "layoutMode": "HORIZONTAL",
      "itemSpacing": 40,
      "children": [
        {
          "type": "frame",
          "name": "Card 1",
          "width": 400,
          "cornerRadius": 12,
          "backgroundColor": "#ffffff",
          "borderColor": "#e5e7eb",
          "borderWidth": 1,
          "shadow": "sm",
          "layoutMode": "VERTICAL",
          "padding": 24,
          "itemSpacing": 12,
          "children": [
            {
              "type": "text",
              "name": "Title",
              "content": "Authentication",
              "fontSize": 24,
              "fontWeight": "semibold",
              "color": "#0f172a"
            },
            {
              "type": "text",
              "name": "Description",
              "content": "Users can securely log in and manage their accounts",
              "fontSize": 14,
              "fontWeight": "regular",
              "color": "#64748b",
              "maxWidth": 352
            }
          ]
        },
        {
          "type": "frame",
          "name": "Card 2",
          "width": 400,
          "cornerRadius": 12,
          "backgroundColor": "#ffffff",
          "borderColor": "#e5e7eb",
          "borderWidth": 1,
          "shadow": "sm",
          "layoutMode": "VERTICAL",
          "padding": 24,
          "itemSpacing": 12,
          "children": [
            {
              "type": "text",
              "name": "Title",
              "content": "Dashboard",
              "fontSize": 24,
              "fontWeight": "semibold",
              "color": "#0f172a"
            },
            {
              "type": "text",
              "name": "Description",
              "content": "View key metrics and recent activity at a glance",
              "fontSize": 14,
              "fontWeight": "regular",
              "color": "#64748b",
              "maxWidth": 352
            }
          ]
        },
        {
          "type": "frame",
          "name": "Card 3",
          "width": 400,
          "cornerRadius": 12,
          "backgroundColor": "#ffffff",
          "borderColor": "#e5e7eb",
          "borderWidth": 1,
          "shadow": "sm",
          "layoutMode": "VERTICAL",
          "padding": 24,
          "itemSpacing": 12,
          "children": [
            {
              "type": "text",
              "name": "Title",
              "content": "Settings",
              "fontSize": 24,
              "fontWeight": "semibold",
              "color": "#0f172a"
            },
            {
              "type": "text",
              "name": "Description",
              "content": "Customize preferences and manage integrations",
              "fontSize": 14,
              "fontWeight": "regular",
              "color": "#64748b",
              "maxWidth": 352
            }
          ]
        }
      ]
    }
  ]
}
```

**This example demonstrates:**
- Top-level frame with absolute positioning (no `layoutMode`)
- Section title using `heading-xl` (36px bold)
- Row container with `layoutMode: "HORIZONTAL"` and `itemSpacing: 40`
- Cards with proper structure: border, shadow, padding, auto-layout
- Typography hierarchy: 24px semibold titles, 14px regular descriptions
- Semantic colors: white cards on light gray background, visible borders
- Text constrained with `maxWidth` (400 - 24×2 = 352)

---

_This reference is for structural quality. A scaffold built with these patterns looks professional regardless of what colors or fonts are plugged in._

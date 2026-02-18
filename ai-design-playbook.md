# The AI-Augmented Design Playbook

> A methodology for designers who use AI as a thinking partner, not a tool.
> Agent-agnostic. Process-first. Grounded in practice.

---

## How to Use This Playbook

**For yourself:** A mental model for when and how to leverage AI across the design process. Not every project hits every phase linearly — skip, loop, remix.

**To kick off with a new AI agent:** Drop the relevant phase section into your first message. It tells the AI what mode you need, what you'll bring, and what you expect back.

**The core principle:** AI handles breadth and speed. You provide depth and judgment. Every phase has a different ratio.

---

## The Process

```
 ┌─────────────────────────────────────────────────────────┐
 │                                                         │
 │   0. CONTEXT    Set the stage                           │
 │       ↓                                                 │
 │   1. DISCOVER   Understand the problem space            │
 │       ↓                                                 │
 │   2. DEFINE     Make strategic choices                  │
 │       ↓                                                 │
 │   3. STRUCTURE  Design the system                       │
 │       ↓                                                 │
 │   4. EXPLORE    Find the visual & interaction language   │
 │       ↓                                                 │
 │   5. DESIGN     Screen-level decisions                  │
 │       ↓                                                 │
 │   6. PROTOTYPE  Make it real & testable                 │
 │       ↓                                                 │
 │   7. REFINE     Critique, iterate, polish               │
 │       ↓                                                 │
 │   8. BRIDGE     Connect design to implementation        │
 │                                                         │
 │   ↻ Loop between any phases as needed                   │
 │                                                         │
 └─────────────────────────────────────────────────────────┘
```

**Cross-cutting practices** run through every phase:
- Decision logging
- Context management
- Friction → tooling automation

---

## Phase 0: Context

> *Set the stage so AI can think with you, not at you.*

### AI Leverage: 🔧 Setup (AI assists extraction, you curate)

This is the most underrated phase. Skip it and every subsequent AI interaction is worse. The quality of your context pack directly determines the quality of AI partnership throughout the project.

### What You Bring
- Product briefs, PRDs, or verbal description of what you're building
- Existing designs (Figma links, screenshots, prototypes)
- Brand guidelines, design system docs
- Technical constraints (platforms, hardware specs, API limitations)
- Business context (stage, timeline, team size, goals)

### What AI Does
- Extracts and structures raw information into organized context docs
- Pulls design tokens from existing files (colors, typography, spacing)
- Maps existing screen inventory and flow connections
- Identifies gaps in the brief ("you haven't mentioned X — is that intentional?")

### The Context Pack

Create a project context folder. This is your portable knowledge base — any AI can read it.

```
project-name/
├── context/
│   ├── brief.md              # Product, users, constraints, goals
│   ├── design-system.md      # Tokens, components, patterns
│   ├── app-structure.md      # Current screens, flows, navigation
│   ├── decisions.md          # Design decision log (ongoing)
│   └── [topic].md            # Competitive research, IA map, etc.
```

**brief.md is the anchor.** Everything else builds on it. A good brief includes:
- What the product is (one paragraph)
- Who it's for (primary + secondary users, pain points)
- Platform/technical constraints
- Current status (greenfield, redesign, feature addition)
- What success looks like

### Prompt Pattern
```
Here's the product context: [paste brief]
Help me organize this into a structured project brief.
What's missing that you'd need to be a useful thinking partner on this project?
```

### Exit Criteria
- [ ] Brief covers product, users, constraints, and goals
- [ ] Design system documented (even if minimal)
- [ ] Current state captured (or "greenfield" noted)
- [ ] You could hand the context folder to a new team member and they'd understand the project

---

## Phase 1: Discover

> *Expand the map before you pick a direction.*

### AI Leverage: ⚡ High (AI excels at breadth; you steer depth)

This is where AI earns its keep fastest. Competitive research that would take days takes hours. Problem space exploration that lives in your head gets externalized and pressure-tested.

### What You Bring
- Hypotheses about the problem space
- Knowledge of your users (even informal)
- Industry experience and intuition about what matters
- Specific questions you're trying to answer

### What AI Does
- **Competitive analysis:** Map competitor approaches across specific dimensions (not just feature lists — interaction patterns, monetization, onboarding, navigation)
- **Problem space mapping:** Surface adjacent problems, edge cases, user segments you haven't considered
- **Research synthesis:** Organize findings into patterns and gaps
- **Assumption surfacing:** "You're assuming X — is that validated?"

### Interaction Mode: Expansive Dialogue

Don't ask for a report. Think out loud and let AI expand on it.

### Prompt Patterns
```
# Competitive Research
Analyze [competitors] focusing on: [specific dimensions].
Don't just list features — compare approaches and interaction patterns.
What gaps exist that no one is filling?

# Problem Space Expansion
I'm designing [X] for [users]. Here's what I think the core problems are: [list].
What am I missing? What adjacent problems would a user encounter
before and after using this product?

# Assumption Check
Here are the assumptions I'm working with: [list].
Which ones are riskiest? What would change if each one were wrong?
```

### Output Artifacts
- Competitive research doc (structured comparison, not feature matrix)
- Problem space map (user needs, pain points, opportunities)
- Key assumptions list (ranked by risk)

### Exit Criteria
- [ ] You understand the landscape well enough to articulate your unique angle
- [ ] Assumptions are surfaced and you've consciously accepted the risks
- [ ] At least one surprising finding that shifted your thinking

---

## Phase 2: Define

> *Make strategic choices that constrain everything downstream.*

### AI Leverage: 🤝 Medium-High (AI generates options and pressure-tests; you decide)

This is where product intuition matters most. AI can generate 10 directions — your job is to pick the one with conviction and articulate why. The combination of AI breadth + your judgment is more powerful than either alone.

### What You Bring
- Conviction about who the product is for
- Business constraints and priorities
- Intuition about what "feels right" (trust it — then pressure-test it)

### What AI Does
- **User story generation:** Frames needs from user perspective across segments
- **Strategy articulation:** Helps you crystallize fuzzy intuitions into clear statements
- **Direction comparison:** "Here are 3 ways to frame this product. Each implies different tradeoffs..."
- **Reframing:** "What if you targeted [different segment]? Here's how that changes everything..."
- **Entity modeling:** Identifies core data objects and relationships in your product

### Interaction Mode: Socratic Challenge

Push back on AI suggestions. Ask "why not the opposite?" The best definitions come from eliminating alternatives with reason, not picking the first good option.

### Prompt Patterns
```
# User Story Reframe
I'm building [X]. The obvious user is [Y].
But I think the real opportunity is [Z]. Help me articulate why
and what it means for the product.

# Strategy Pressure Test
Here's my product strategy: [strategy].
Play devil's advocate. What's the strongest argument against this direction?
What would a competitor exploit?

# Entity Modeling
The core objects in this product are: [list].
Help me map the relationships. What's the central entity?
What does that choice imply for the UI?
```

### Output Artifacts
- Product strategy statement (one page max)
- Target user definition with priority segments
- Entity/data model (what the product is "about")
- Decision log entries with rationale

### Exit Criteria
- [ ] You can explain the product strategy in 2 sentences
- [ ] Target user is specific enough to make design decisions against
- [ ] Entity model clarifies what's primary vs. secondary in the UI
- [ ] Key strategic decisions are logged with rationale

---

## Phase 3: Structure

> *Design the bones before the skin.*

### AI Leverage: ⚡ High (AI generates and compares structural options fast)

Information architecture is combinatorial — there are many valid ways to organize the same content. AI can rapidly generate and compare structural options while you evaluate them against user mental models and business goals.

### What You Bring
- User mental models (how users think about the domain)
- Business priorities (what needs to be prominent)
- Technical constraints (what's feasible)
- Taste (what feels right structurally)

### What AI Does
- **IA generation:** Multiple navigation structures with tradeoffs articulated
- **Flow mapping:** User journeys through the structure for key scenarios
- **Structural comparison:** "5-tab vs 3-tab vs 2-tab+FAB — here's what each implies"
- **Edge case surfacing:** "What happens when a user has no [X] yet? Where does [Y] live?"
- **Pattern matching:** "Apps like [Z] solved this by..." (with critical analysis, not just copying)

### Interaction Mode: Structured Exploration

Explore 2-3 structural options in depth before committing. Have AI articulate the tradeoffs of each, then decide.

### Prompt Patterns
```
# IA Exploration
Here are the core surfaces in the app: [list].
Generate 3 navigation structures. For each one, explain:
- What it prioritizes
- What it buries
- How a new user would experience it
- How a power user would experience it

# Flow Validation
Here's the IA: [structure].
Walk me through these user stories: [stories].
Where does the structure support the flow? Where does it fight it?

# Empty State Design
For each screen in [IA], what does it look like when there's no data?
How does the empty state guide the user toward filling it?
```

### Output Artifacts
- Information architecture map (screens, hierarchy, navigation)
- Key flow diagrams (happy path + edge cases)
- Navigation model decision with rationale
- Screen inventory (what needs to be designed)

### Exit Criteria
- [ ] IA supports all key user stories without forcing awkward navigation
- [ ] Empty states and edge cases are accounted for
- [ ] Navigation model is decided with documented rationale
- [ ] Screen inventory is complete enough to estimate design scope

---

## Phase 4: Explore

> *Find the visual and interaction language.*

### AI Leverage: 🤝 Medium (AI generates options and references; taste is yours)

This is where your design eye matters most. AI can generate mood boards, suggest directions, and articulate the feeling of different approaches — but it can't replace your aesthetic judgment. Use AI to expand the option space, then curate ruthlessly.

### What You Bring
- Visual intuition and taste
- Brand sensibility
- References and inspiration (even vague — "it should feel like...")
- Understanding of the emotional register (playful? serious? minimal? rich?)

### What AI Does
- **Direction generation:** "Here are 4 visual directions for this product, each with a different personality..."
- **Concept articulation:** Puts words to visual ideas ("Living Garden" as a metaphor → design implications)
- **Style analysis:** Breaks down reference designs into structural patterns (spacing systems, typography scales, color relationships)
- **Design system scaffolding:** Proposes token sets (colors, type scale, spacing, radius, shadows) from a direction

### Interaction Mode: Creative Ping-Pong

Share a vague feeling. Let AI articulate it. React. Refine. The value is in the back-and-forth — AI helps you discover what you want by generating things to react to.

### Prompt Patterns
```
# Direction Exploration
The product is [X] for [users]. The feeling should be [descriptors].
Give me 3-4 visual directions. For each: name it, describe the personality,
suggest key design decisions (color, typography, density, motion).

# Reference Analysis
Here's a design I'm inspired by: [reference].
Break down what makes it work structurally — not the surface aesthetics,
but the spacing system, hierarchy, and composition principles I could extract.

# Design System Foundation
Based on [direction], propose a design system foundation:
color palette (with semantic roles), type scale, spacing scale,
corner radius system, shadow system, and component style guidelines.
```

### Output Artifacts
- Visual direction(s) with articulated personality
- Design system foundation (tokens + principles)
- Mood/concept documentation
- Visual style guide for consistent execution

### Exit Criteria
- [ ] Visual direction chosen with clear rationale
- [ ] Design system tokens defined (even if preliminary)
- [ ] You can articulate the "why" behind the visual choices
- [ ] Direction is specific enough to hand to someone else to execute

---

## Phase 5: Design

> *Screen-level decisions, one surface at a time.*

### AI Leverage: ⚡ High (AI drafts screens as structured specs or code; you art-direct)

This is where AI as execution partner accelerates the most. Instead of designing every screen from scratch, you can describe what a screen should do and have AI generate a structured draft — then refine through critique cycles.

### What You Bring
- Screen-level judgment (what information goes where, what's primary)
- Interaction design decisions (how things behave, not just how they look)
- Quality bar (knowing when something is "right")
- User empathy (how this screen feels in the flow, not in isolation)

### What AI Does
- **Screen spec generation:** Structured descriptions of what each screen contains, prioritized
- **Layout proposals:** Multiple layout options for complex screens
- **Content writing:** UI copy, microcopy, error messages, empty states
- **Interaction spec:** Describe transitions, gestures, state changes
- **Mockup generation:** HTML/CSS prototypes that visualize the design for quick evaluation
- **Design critique:** "This screen is doing too much. Consider splitting [X] and [Y]..."

### Interaction Mode: Art Direction

You're the director. AI proposes, you react and redirect. "More whitespace." "The card hierarchy is wrong — the plant status should be louder than the device info." "Try it with the action at the bottom."

### Prompt Patterns
```
# Screen Design
Here's the screen: [name and purpose].
Context: [where user came from, what they're trying to do].
Content: [what needs to be on this screen, in priority order].
Generate a detailed layout proposal. Include content, hierarchy,
and interaction notes.

# UI Copy
Write the copy for [screen/flow]. The tone is [tone].
The user is [context]. Keep it [concise/friendly/instructive].
Give me 2-3 options for the key headline.

# Screen Critique
Here's my current design for [screen]: [description or screenshot].
Critique it as a [first-time user / power user / accessibility reviewer].
What's working? What's fighting the user?
```

### Output Artifacts
- Screen specs (content, layout, hierarchy, interactions)
- UI copy document
- Visual mockups (HTML/Figma/image depending on tooling)
- Interaction specifications

### Exit Criteria
- [ ] All screens in the inventory are designed (at least lo-fi)
- [ ] Key interactions are specified
- [ ] Copy is written (not placeholder)
- [ ] Screens work as a flow, not just individual pages

---

## Phase 6: Prototype

> *Make it real enough to feel, test, and share.*

### AI Leverage: ⚡⚡ Very High (AI builds; you direct and test)

This is AI at maximum leverage. Building interactive prototypes from specs is exactly the kind of work AI does faster and more consistently than manual construction. Your role shifts to testing, feeling, and directing revisions.

### What You Bring
- The sense of "this doesn't feel right" when you click through
- Judgment about motion, timing, and feedback
- User perspective (testing your own work with fresh eyes)
- Stakeholder awareness (what needs to be shown, to whom)

### What AI Does
- **Interactive prototype generation:** Full click-through prototypes from specs
- **Motion and animation:** Transitions, micro-interactions, loading states
- **State handling:** Multi-state screens (empty, loading, populated, error)
- **Responsive adaptation:** Different screen sizes from the same spec
- **Rapid iteration:** "Make the transition slower." "Add a bounce." "Try swiping instead of tapping."

### Interaction Mode: Build → Feel → Direct

Don't over-spec before seeing it. Get a rough prototype fast, interact with it, then direct changes based on how it feels. Multiple quick iterations beat one perfect spec.

### Prompt Patterns
```
# Prototype Generation
Build an interactive prototype for [flow].
Here's the spec: [screens + transitions].
Make it feel like a real app — smooth transitions, touch targets,
proper spacing. Single HTML file I can open in a mobile browser.

# Iteration
The [specific part] doesn't feel right.
[What's wrong: too fast / too much information / wrong hierarchy / etc.]
Try [specific direction].

# Multi-State
Show me all states for [screen]:
empty (first time), loading, populated (few items),
populated (many items), error. How do transitions between states feel?
```

### Output Artifacts
- Interactive prototype (HTML/Figma/tool of choice)
- Flow demonstration (key scenarios clickable)
- State inventory (all screen states visualized)

### Exit Criteria
- [ ] Key flows are clickable end-to-end
- [ ] It "feels" right when you use it (trust your gut)
- [ ] Stakeholders can experience the design, not just see static screens
- [ ] Edge cases are visible (empty states, errors, loading)

---

## Phase 7: Refine

> *Critique, iterate, polish — with AI as a fresh pair of eyes.*

### AI Leverage: 🤝 Medium (AI provides structured critique; you filter)

AI critique is most valuable when you give it a specific lens. "What do you think?" gets generic feedback. "Critique this as a first-time user who doesn't know what this app does" gets actionable insight.

### What You Bring
- Design maturity (knowing what level of polish is needed now vs. later)
- Prioritization (which feedback to act on, which to defer)
- Quality bar (your standard for "done")

### What AI Does
- **Structured critique:** Evaluate against specific criteria (usability, consistency, accessibility, hierarchy)
- **Persona-based review:** "As a [user type], this is confusing because..."
- **Consistency audit:** Spot inconsistencies across screens (spacing, copy patterns, interaction patterns)
- **Accessibility check:** Color contrast, touch targets, screen reader flow, cognitive load
- **Copy review:** Tone consistency, clarity, brevity

### Interaction Mode: Structured Review Cycles

Ask for critique through specific lenses, one at a time. A focused critique round produces better feedback than "review everything."

### Prompt Patterns
```
# Persona-Based Critique
Review [screen/flow] as [specific persona with specific context].
What's your first impression? Where do you get confused?
What would make you abandon this flow?

# Consistency Audit
Here are all screens in [flow]: [list/screenshots].
Check for consistency in: spacing, typography usage, button styles,
copy patterns, icon usage, and interaction patterns.
Flag any inconsistencies.

# Accessibility Review
Review [design] for accessibility:
- Color contrast (WCAG AA minimum)
- Touch target sizes (44px minimum)
- Reading order and screen reader flow
- Cognitive load and information density
- Motion sensitivity
```

### Output Artifacts
- Critique notes organized by severity
- Consistency audit findings
- Accessibility report
- Prioritized iteration list

### Exit Criteria
- [ ] At least one round of structured critique completed
- [ ] Critical usability issues addressed
- [ ] Cross-screen consistency verified
- [ ] You're proud enough to show it to stakeholders

---

## Phase 8: Bridge

> *Connect design to everything beyond the Figma canvas.*

### AI Leverage: ⚡⚡ Very High (AI builds tools and specs; you validate)

The bridge between design and implementation is full of tedious, structural work that AI handles exceptionally well — specs, documentation, tooling, and translation between formats.

### What You Bring
- Knowledge of your team's workflow (what developers need, what format works)
- Quality standards for handoff (what level of detail prevents back-and-forth)
- Tool preferences (what your team uses)

### What AI Does
- **Spec generation:** Detailed screen specs with measurements, tokens, interactions, states
- **Custom tooling:** Figma plugins, design-to-code scripts, format converters
- **Design system documentation:** Component docs with usage guidelines, do/don't examples
- **Developer handoff docs:** Annotated specs, interaction guides, API-to-UI mapping
- **Design token export:** Transform design system into code-ready formats (CSS variables, JSON tokens, etc.)
- **Automation:** Anything repetitive in your workflow that could be scripted

### Interaction Mode: Specification + Tool Building

Be precise about what developers need. AI translates design intent into technical specification and builds workflow tools to reduce manual translation.

### Prompt Patterns
```
# Spec Generation
Generate developer specs for [screen]:
- All measurements (spacing, sizing) using the design system tokens
- Interaction behavior for each interactive element
- All states (default, hover, pressed, disabled, loading, error)
- Copy (final, not placeholder)

# Custom Tooling
I keep doing [repetitive task] manually.
Build me a [script/plugin/tool] that does it automatically.
Input: [what I provide]. Output: [what I need].

# Design System Documentation
Document [component] for the team:
- When to use it (and when not to)
- All variants and states
- Spacing and layout rules
- Interaction specs
- Code-ready token values
```

### Output Artifacts
- Developer handoff specs
- Design system documentation
- Custom tools and plugins
- Design token files

### Exit Criteria
- [ ] Key screens have developer-ready specs
- [ ] Design system is documented for the team
- [ ] Repetitive workflow friction has been automated where possible
- [ ] Developers can build from your specs without constant clarification

---

## Cross-Cutting Practices

These run through every phase. They're not steps — they're habits.

### Decision Logging

Every non-trivial design decision gets logged with:
- **What** was decided
- **Why** (the rationale — this is the valuable part)
- **What it affects** downstream
- **Status** (active / superseded / under review)

This log is your project's institutional memory. When someone asks "why is it like this?" six months later, the answer is in the log — not lost in a conversation thread.

**Prompt pattern:**
```
Log this decision: [what you decided and why].
What downstream effects should we note?
```

### Context Management

AI is only as good as its context. Manage it actively:

- **Start of session:** Load the context pack. Paste or reference your brief, relevant decisions, and where you left off.
- **During work:** When significant decisions are made, update the context docs immediately — don't wait until the end.
- **End of session / switching agents:** Write a handoff note capturing current state, open questions, and next steps.

The context pack makes you agent-agnostic. Any AI that reads your brief.md, decisions.md, and latest handoff note is 80% caught up.

### Friction → Tooling

Keep a friction log (mental or written). When something slows you down repeatedly:

1. Notice the friction ("I keep manually exporting these frames...")
2. Describe the transformation (input → output)
3. Ask AI to build a tool
4. Test it, iterate once, integrate into workflow

The best tools come from observed friction, not anticipated needs. Don't pre-build — let the pain reveal what matters.

---

## Kicking Off With a New AI Agent

When you start a design project with any AI, send this:

```
I'm a product designer starting work on [project].

Here's my project context: [paste brief.md or key summary]

I work with AI as a thinking partner across the full design process —
from strategy through prototyping to implementation. Here's how I like to work:

1. Be opinionated. I want a collaborator, not a yes-machine.
2. Push back on my assumptions. If you see a gap, say so.
3. Structure your thinking. Use headers, bullets, and clear hierarchy.
4. When I ask for options, give me 3 with distinct tradeoffs — not 3 variations of the same idea.
5. Log important decisions as we go (what, why, impact).
6. Ask me clarifying questions when you need them, but don't stall on every ambiguity.

Current phase: [which phase you're in]
Current focus: [what you're working on]
Open questions: [any unresolved items]

Let's go.
```

---

## Quick Reference

| Phase | AI Leverage | AI Mode | Your Mode |
|-------|-------------|---------|-----------|
| 0. Context | 🔧 Setup | Extract & structure | Curate & validate |
| 1. Discover | ⚡ High | Research & expand | Steer & prioritize |
| 2. Define | 🤝 Medium-High | Generate & pressure-test | Decide with conviction |
| 3. Structure | ⚡ High | Generate & compare | Evaluate & commit |
| 4. Explore | 🤝 Medium | Propose & articulate | React & curate |
| 5. Design | ⚡ High | Draft & iterate | Art-direct & refine |
| 6. Prototype | ⚡⚡ Very High | Build & revise | Feel & direct |
| 7. Refine | 🤝 Medium | Critique & audit | Filter & prioritize |
| 8. Bridge | ⚡⚡ Very High | Spec & build tools | Validate & ship |

---

*This playbook is a living document. Update it as your practice evolves.*
*Methodology by Amy Pu. Built through real design work, not theory.*

# Design With AI

A portable toolkit for AI-augmented product design. Agent-agnostic — works with Claude, ChatGPT, Gemini, or any AI that can read files and run scripts.

## What's Inside

```
design-with-ai/
├── ai-design-playbook.md       # The methodology (start here)
├── ai-design-playbook.html     # Shareable visual version
├── templates/                  # Project templates
│   ├── project-brief.md        # Product context, users, constraints
│   ├── content-spec.md         # Screen-by-screen content spec
│   ├── design-review.md        # Structured design critique
│   ├── feature-spec.md         # Feature proposal with tradeoffs
│   ├── flow-spec.md            # User flow specification
│   ├── visual-audit.md         # Competitive visual analysis
│   └── prototype-base.html     # Interactive prototype shell
├── figma-scripts/              # Figma API utilities
│   ├── figma-file.py           # Get file structure
│   ├── figma-styles.py         # Extract design tokens
│   ├── figma-frames.py         # Export frames as PNG/SVG
│   └── figma-components.py     # List components & properties
└── references/
    └── visual-style-guide.md   # Spacing, typography, composition patterns
```

## Quick Start

### 1. Read the Playbook

Start with `ai-design-playbook.md` — it covers the full design process and how to partner with AI at each phase.

### 2. Set Up a New Project

Create a `.design-companion/` folder in your project directory using the templates:

```bash
mkdir -p my-project/.design-companion
cp templates/project-brief.md my-project/.design-companion/brief.md
```

Fill in the brief. This is your context pack — any AI that reads it is immediately useful.

### 3. Connect Figma (optional)

```bash
cp .env.example .env
# Edit .env and add your Figma Personal Access Token
# Get one at: https://www.figma.com/developers/api#access-tokens
```

Then use the scripts:

```bash
# Get file structure
python3 figma-scripts/figma-file.py <file_key>

# Extract design tokens (colors, typography, effects)
python3 figma-scripts/figma-styles.py <file_key>

# Export frames as images
python3 figma-scripts/figma-frames.py <file_key> --format png --scale 2

# List components
python3 figma-scripts/figma-components.py <file_key>
```

The file key is from your Figma URL: `figma.com/design/<FILE_KEY>/...`

### 4. Kick Off With Any AI

Paste this into your first message with a new AI agent:

> I'm a product designer. Here's my project context: [paste brief.md]
>
> I work with AI as a thinking partner across the full design process. Be opinionated, push back on my assumptions, and structure your thinking clearly. When I ask for options, give me 3 with distinct tradeoffs.

See the full kickoff template in the playbook.

## Templates

| Template | When to Use |
|----------|-------------|
| **project-brief.md** | Starting any new project — the anchor document |
| **content-spec.md** | Specifying screens before design |
| **design-review.md** | Structured critique of existing designs |
| **feature-spec.md** | Proposing a new feature with tradeoffs |
| **flow-spec.md** | Mapping user flows and edge cases |
| **visual-audit.md** | Analyzing competitor visual approaches |
| **prototype-base.html** | Building interactive HTML prototypes |

## The Playbook Online

📖 [Read it here](https://amy3478.github.io/design-with-ai/ai-design-playbook.html)

## Requirements

- Python 3 (for Figma scripts)
- A Figma Personal Access Token (for Figma integration)
- Any AI agent that can read markdown files

---

*Built by Amy Pu. Methodology developed through real design work.*

# GitHub Configuration

This folder contains GitHub-specific configuration files.

## 📄 Files

### `copilot-instructions.md`
**Purpose:** Automatically loaded by GitHub Copilot Chat to provide project context  
**Contains:**
- Project overview (Alpha Rooster v10.0, tech stack)
- Core coding rules (no placeholders, use env vars, comprehensive logging)
- Phase-based development guidelines
- Code generation standards with examples
- Testing requirements
- What NOT to suggest (prevents scope creep)

**How it works:**
When you open Copilot Chat, it automatically reads this file. This means every conversation starts with Copilot knowing:
- ✅ Use FastAPI, not Flask
- ✅ Use BigQuery, not PostgreSQL
- ✅ Use Jinja2 templates, not React
- ✅ No placeholder code (`TODO`, `pass`, mocks)
- ✅ Always include error handling and logging
- ✅ Always use environment variables

**When to update:**
- Tech stack changes
- New coding patterns emerge
- Common mistakes need to be prevented

---

## 🎯 Usage

**You don't need to manually reference this file.** Copilot Chat loads it automatically.

**Best practices:**
- ✅ "I'm working on Phase 3.2. Build the /qualify route."
- ✅ "Add error handling to the postback endpoint."
- ❌ Don't need to say: "Reference copilot-instructions.md and..."

**If Copilot seems to ignore the rules:**
Explicitly mention the phase or constraint:
```
"Per copilot-instructions.md, build /qualify route with NO placeholders"
```

---

**For complete workspace setup, see [../docs/WORKSPACE_SETUP.md](../docs/WORKSPACE_SETUP.md)**

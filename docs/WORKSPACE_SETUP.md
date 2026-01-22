# Workspace Setup Guide

This workspace includes several configuration files to help you build efficiently with GitHub Copilot.

## 📁 File Organization

```
/alpha-rooster
  /.github
    copilot-instructions.md    # Auto-loaded by Copilot Chat
  /.vscode
    settings.json              # Editor settings, formatters, linting
    tasks.json                 # One-click commands (run, test, deploy)
    launch.json               # Debug configurations
    extensions.json           # Recommended extensions
  /docs
    PHASE_TRACKER.md          # Checkbox-based progress tracker
    WORKSPACE_SETUP.md        # This file
  .env.example                # Template for environment variables
  README.md                   # Complete project specification
```

---

## 🚀 Quick Start

### 1. First-Time Setup

**Install Recommended Extensions:**
```bash
# VS Code will prompt you to install recommended extensions
# Or manually: Cmd+Shift+P → "Extensions: Show Recommended Extensions"
```

**Create Environment File:**
```bash
cp .env.example .env
# Then edit .env and fill in your actual values
```

**Validate Setup:**
```bash
# Press Cmd+Shift+P → "Tasks: Run Task" → "✅ Validate Environment Variables"
```

---

## 🎯 How to Use Built-in Features

### Using Copilot Chat with Context

The `.github/copilot-instructions.md` file is **automatically loaded** by Copilot Chat. This means Copilot already knows:
- Your tech stack (Python, FastAPI, BigQuery, Meta Ads)
- Your coding rules (no placeholders, use env vars, log everything)
- Your phase-based workflow
- What NOT to suggest (React, PostgreSQL, etc.)

**Best practice prompts:**
```
"I'm starting Phase 3, Task 3.2. Build the /qualify route per spec."

"Add error handling to the postback endpoint for missing fbclid."

"What's the next unchecked task in docs/PHASE_TRACKER.md?"
```

### Using VS Code Tasks (One-Click Commands)

**Access:** Press `Cmd+Shift+P` → "Tasks: Run Task"

**Available tasks:**
- 🚀 **Run FastAPI Dev Server** (also: `Cmd+Shift+B` for default build)
- 🧪 **Test Postback Endpoint** (prompts for event_id and payout)
- 📊 **Query BigQuery Events** (last 10)
- 📊 **Query BigQuery Conversions** (last 10)
- 📦 **Build Docker Image**
- 🐳 **Run Docker Container**
- ☁️ **Deploy to Cloud Run**
- ✅ **Validate Environment Variables**
- 🔍 **Check Cloud Run Logs**
- 📈 **Daily Performance Report**

**Example workflow:**
1. `Cmd+Shift+B` → Starts dev server
2. Make code changes
3. `Cmd+Shift+P` → "Tasks: Run Task" → "Test Postback Endpoint"
4. `Cmd+Shift+P` → "Tasks: Run Task" → "Query BigQuery Events"

### Using the Debugger

**Start debugging:** Press `F5`

This will:
- Activate your virtual environment
- Load `.env` variables
- Start FastAPI with debugger attached
- Allow breakpoints in Python code and Jinja2 templates

**Set breakpoints:** Click left of line numbers in `.py` files

### Using Phase Tracker

**Open:** `docs/PHASE_TRACKER.md`

**Daily workflow:**
1. Find next unchecked `[ ]` task
2. Tell Copilot: "Work on task 3.2.1 from PHASE_TRACKER"
3. Complete task, test it, get proof (screenshot/log)
4. Check off `[x]` and add verification note
5. Commit with proof

**Why this matters:**
- Prevents "claiming done without testing"
- Creates audit trail of actual progress
- Shows what proof is needed (e.g., "Screenshot: tests/pixel_helper.png")

---

## 🛠️ Configuration Files Explained

### `.github/copilot-instructions.md`
**Purpose:** Loaded automatically by Copilot Chat  
**Contents:**
- Project context (Alpha Rooster v10.0, tech stack)
- Core rules (no placeholders, use env vars)
- Phase descriptions with verification steps
- Code generation standards with examples
- Testing requirements

**When Copilot reads this, it will:**
- ✅ Generate runnable code (no TODOs)
- ✅ Use environment variables
- ✅ Include error handling and logging
- ✅ Provide test commands
- ❌ NOT suggest React, PostgreSQL, or out-of-scope features

### `.vscode/settings.json`
**Purpose:** Auto-configure editor behavior  
**Key settings:**
- Enable Copilot for all file types
- Auto-format Python with Black on save
- Enable type checking with Pylance
- Auto-organize imports

### `.vscode/tasks.json`
**Purpose:** Define one-click commands  
**Key tasks:**
- Run dev server (integrates with `venv`)
- Test endpoints (includes input prompts)
- Query BigQuery (uses env vars)
- Deploy to Cloud Run (complete command)

**How it works:** Uses `${env:VARIABLE}` to pull from `.env` file

### `.vscode/launch.json`
**Purpose:** Configure debugger  
**Features:**
- Launches `uvicorn` with reload
- Loads `.env` automatically
- Enables Jinja2 template debugging

### `.vscode/extensions.json`
**Purpose:** Recommend required extensions  
**Recommended:**
- GitHub Copilot & Copilot Chat
- Python & Pylance
- Google Cloud Code
- YAML support

### `.env.example`
**Purpose:** Template for required environment variables  
**Usage:**
```bash
cp .env.example .env
# Edit .env with your actual values
```

**Security:** `.env` is gitignored, `.env.example` is committed

---

## 💡 Best Practices

### Starting a Coding Session

**1. Open Phase Tracker:**
```bash
code docs/PHASE_TRACKER.md
```

**2. Find current task** (e.g., Phase 3.2.1)

**3. Open Copilot Chat and say:**
```
I'm working on Phase 3, Task 3.2.1 from PHASE_TRACKER.md.
Build the /qualify route per README.md Part 3 spec.
```

**4. Start dev server:**
```bash
Cmd+Shift+B
```

### During Development

**Test as you go:**
- After each function: Run relevant task (e.g., "Test Postback Endpoint")
- After each route: Visit in browser
- After BigQuery write: Run "Query BigQuery Events"

**Use debugger for issues:**
- Press `F5` to start debugging
- Set breakpoints by clicking line numbers
- Step through code with `F10` (step over) or `F11` (step into)

### End of Day

**1. Update Phase Tracker:**
```markdown
- [x] 3.2.1 Pre-qualifier template created
  - Verification: Screenshot saved to tests/qualify_form.png
  - Notes: Form works on mobile, tested on iPhone Safari
```

**2. Commit with proof:**
```bash
git add .
git commit -m "Phase 3.2.1: Pre-qualifier form - VERIFIED (screenshot: tests/qualify_form.png)"
git push
```

---

## 🔧 Troubleshooting

### "Tasks not working"
**Issue:** Task fails with "command not found"  
**Fix:** Ensure you've activated venv and installed dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### "Environment variables not loading"
**Issue:** `.env` file not being read  
**Fix:** 
1. Ensure `.env` exists (copy from `.env.example`)
2. Run validation task: "✅ Validate Environment Variables"
3. Restart VS Code

### "Copilot not using instructions"
**Issue:** Copilot suggesting React, placeholders, etc.  
**Fix:**
1. Explicitly reference the file in chat:
   ```
   "Reference .github/copilot-instructions.md and build the /qualify route"
   ```
2. Or start prompt with phase:
   ```
   "Phase 3.2: Build /qualify route per spec"
   ```

### "Python debugger not starting"
**Issue:** Debug config shows errors  
**Fix:** Install Python extension:
```bash
Cmd+Shift+P → "Extensions: Install Extensions" → Search "Python"
```

---

## 📚 Additional Resources

- **Full Project Spec:** `README.md` (Parts 1-6)
- **Copilot Rules:** `.github/copilot-instructions.md`
- **Progress Tracker:** `docs/PHASE_TRACKER.md`
- **VS Code Tasks:** `.vscode/tasks.json` (view available commands)

---

## 🎓 Learning Path

If you're new to this setup:

**Week 1:** Get familiar with tasks
- Use `Cmd+Shift+B` to run server
- Use tasks menu for testing
- Manual commits

**Week 2:** Add debugging
- Set breakpoints in routes
- Step through code
- Inspect variables

**Week 3:** Optimize workflow
- Use Copilot Chat with phase context
- Reference PHASE_TRACKER in prompts
- Auto-format on save

**Week 4:** Advanced
- Create custom tasks (edit `.vscode/tasks.json`)
- Add custom launch configs
- Set up Cloud Logging integration

---

**Last Updated:** January 22, 2026

# VS Code Workspace Configuration

This folder contains VS Code-specific configuration files.

## 📄 Files

### `settings.json`
**Purpose:** Configure editor behavior, formatters, and Copilot  
**Key features:**
- Auto-format Python with Black on save
- Enable Copilot for all file types
- Configure Pylance type checking
- Auto-organize imports

### `tasks.json`
**Purpose:** Define one-click commands accessible via Task menu  
**Key tasks:**
- 🚀 Run FastAPI dev server (`Cmd+Shift+B`)
- 🧪 Test endpoints
- 📊 Query BigQuery
- ☁️ Deploy to Cloud Run

**Access:** `Cmd+Shift+P` → "Tasks: Run Task"

### `launch.json`
**Purpose:** Configure debugger  
**Features:**
- Debug FastAPI with breakpoints
- Auto-load `.env` variables
- Support Jinja2 template debugging

**Usage:** Press `F5` to start debugging

### `extensions.json`
**Purpose:** Recommend required extensions  
**Includes:**
- GitHub Copilot & Copilot Chat
- Python & Pylance
- Google Cloud Code
- YAML support

**VS Code will prompt to install these automatically**

---

## 🚫 Do Not Edit Manually (Usually)

These files are carefully configured to work together. If you need to customize:

1. **Add a new task:** Edit `tasks.json` → Add to `"tasks"` array
2. **Change formatter:** Edit `settings.json` → Modify `"python.formatting.provider"`
3. **Add extension:** Edit `extensions.json` → Add to `"recommendations"`

---

**For usage instructions, see [../docs/WORKSPACE_SETUP.md](../docs/WORKSPACE_SETUP.md)**

# Alpha Rooster Documentation

This folder contains project documentation and progress tracking files.

## 📄 Files in This Directory

### [PHASE_TRACKER.md](./PHASE_TRACKER.md)
**Purpose:** Checkbox-based progress tracker for all 6 build phases  
**Use:** Track daily progress, add verification proof, prevent "fake completions"  
**Update:** Daily (check off tasks as you complete them)

### [WORKSPACE_SETUP.md](./WORKSPACE_SETUP.md)
**Purpose:** Guide to using VS Code workspace features (tasks, debugger, Copilot)  
**Use:** Reference when setting up workspace or learning workflow  
**Update:** Rarely (only when adding new tasks or configs)

---

## 🔗 Other Important Docs

These files are in other locations but referenced frequently:

- **[../README.md](../README.md)** - Complete project specification (Parts 1-6)
- **[../.github/copilot-instructions.md](../.github/copilot-instructions.md)** - Copilot coding rules (auto-loaded)
- **[../.vscode/tasks.json](../.vscode/tasks.json)** - Available VS Code tasks
- **[../.env.example](../.env.example)** - Environment variable template

---

## 📊 Progress Overview

**Quick Status Check:**

```bash
# Count completed tasks
grep -c "\[x\]" PHASE_TRACKER.md

# Count remaining tasks
grep -c "\[ \]" PHASE_TRACKER.md
```

**View specific phase:**
```bash
# Show Phase 3 progress
sed -n '/## .*Phase 3/,/## .*Phase 4/p' PHASE_TRACKER.md | grep "\[ \]"
```

---

## 🎯 Workflow

**Daily routine:**
1. Open `PHASE_TRACKER.md`
2. Find next unchecked task
3. Build feature
4. Test and get proof (screenshot, log, query result)
5. Check off task and add verification note
6. Commit with proof in message

**Weekly routine:**
1. Review `PHASE_TRACKER.md` for week
2. Update "Notes & Learnings" section
3. Plan next week's tasks
4. Update README.md if scope changed

---

**For setup instructions, see [WORKSPACE_SETUP.md](./WORKSPACE_SETUP.md)**

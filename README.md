## Pomodoro Timer - How it works

This is a **Pomodoro Technique timer** built with Tkinter. It helps you work in focused intervals with breaks in between.

### What is the Pomodoro Technique

- 25 minutes of work
- 5 minutes short break
- After 4 work sessions → 20 minutes long break
- Repeat the cycle

### Project files

- `main.py` – the complete application
- `tomato.png` – tomato image for the canvas

### What is used

- `tkinter` module: for GUI window, labels, buttons, and canvas
- `math` module: for floor division in time conversion
- `.after()` method: to create the countdown timer

### How it works

**Timer cycles:**

| Session number | Type | Duration |
|----------------|------|----------|
| 1, 3, 5, 7 | Work | 25 minutes |
| 2, 6 | Short break | 5 minutes |
| 4 | Short break | 5 minutes |
| 8 | Long break | 20 minutes |
| 9+ | Repeats from start | |

**Features:**

1. **Start button** – begins the timer cycle
2. **Reset button** – stops timer and resets everything
3. **Checkmarks (✔)** – appear after each completed work session
4. **Timer label** – changes color based on session type:
   - Work → RED
   - Short break → PINK
   - Long break → RED

### Controls

| Button | Action |
|--------|--------|
| Start | Begin the Pomodoro cycle |
| Reset | Stop timer and reset all counters |

### Visual elements

- Tomato image with timer text inside
- Colored labels showing current session
- Checkmarks track completed work sessions
- Yellow background for eye comfort

### Example of a full cycle

```
Start → Work (25 min) → ✔ → Short break (5 min) → Work (25 min) → ✔ → Short break (5 min) → Work (25 min) → ✔ → Short break (5 min) → Work (25 min) → ✔ → Long break (20 min) → Repeat
```

### Benefits

- Improves focus and productivity
- Prevents burnout with regular breaks
- Visual progress tracking with checkmarks

---


# Elise Shaumbwa — Flet Web Portfolio

Cyber-themed portfolio built with the **Flet Python framework** for Computer Programming I.

## Folder Structure

```
elise-portfolio/
├── main.py                  # Entry point — run this
├── requirements.txt
├── README.md
├── app/
│   ├── theme.py             # Colors & styling
│   ├── components/
│   │   ├── nav_bar.py       # Top navigation
│   │   ├── overlay.py       # In-app video/image popups
│   │   └── math_view.py     # KaTeX math articles
│   └── pages/
│       ├── home.py
│       ├── skills.py
│       ├── projects.py      # CorroCheck
│       ├── timeline.py      # Weekly project log
│       ├── matlab_hub.py    # 8 MathWorks courses
│       ├── blog.py          # Confidence in Concepts
│       ├── github_evidence.py
│       └── contact.py
└── assets/
    ├── images/
    │   ├── profile.png
    │   ├── corrocheck_screenshot.png
    │   ├── github/
    │   │   ├── commits.png
    │   │   └── pull_requests.png
    │   └── matlab/
    │       ├── onramp.png
    │       ├── fundamentals.png
    │       ├── data_processing.png
    │       ├── visualisation.png
    │       ├── ml.png
    │       ├── signal.png
    │       ├── simulink.png
    │       └── engineering_maths.png
    └── videos/
        ├── corrocheck_demo.mp4
        ├── blog_corrosion.mp4
        ├── blog_flet.mp4
        └── blog_matlab.mp4
```

## How to Open Locally

1. Open a terminal in this folder:
   ```
   cd C:\Users\pcname\Projects\elise-portfolio
   ```

2. Runs on Flet 0.84 — ensure it's installed:
   ```
   python -m pip install -r requirements.txt
   ```

3. Run the portfolio:
   ```
   python main.py
   ```

4. Your browser opens at **http://localhost:8550**

> **Requires Flet 0.84+** — uses `ft.BoxFit` (not the old `ImageFit`) and `ft.run()` (not `ft.app()`).

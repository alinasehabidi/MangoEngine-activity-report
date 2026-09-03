# MangoEngine Quarterly Impact Report

A presentation-ready Streamlit application covering Jainam's activity, outcomes, learning, brand growth, and next priorities for **1 July – 3 September 2026**.

## Run locally

```powershell
cd mango-quarterly-report
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## What is included

- Meetings and outcomes
- Presentation and webinar feedback
- Events, networking, social presence, and speaking opportunities
- Learning and development, including book reading and AI sessions
- New SOPs that helped streamline work
- A clear summary of support provided to Jainam
- Presentation mode with short talk tracks, audience questions, and closing messages

## Data notes

This is a management report based on the supplied activity notes. Counts and stated results are recorded as reported. Items described as planned, in progress, or needing verification are deliberately labeled that way; they are not presented as completed outcomes.

To update a reporting period, edit the structured constants near the top of `app.py`.

## Project structure

```text
mango-quarterly-report/
├── app.py              # Interactive report application
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

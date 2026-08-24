# Welcome to 2026 Data Science Summer Prep!

## Thursdays 6:30-8:30pm [Virtuall via Zoom](https://us02web.zoom.us/j/82947169100?pwd=S4rxfb7jaDXWC1i8vsJb9x3eVbO6NZ.1)

### [Syllabus with all Information](https://docs.google.com/document/d/1H1zLD3qRmphI1QW9rtZqrR9gcYaCzUR2ubx3IMSP6JI/edit?tab=t.0#heading=h.8a01gder06rw)

*If you do not have access to the Syllabus, **you must be logged into the email you shared with CTP when you applied.**  If you dont remember, please try a few before DMing me directly for access.* 


Please have your full name, how to pronounce, and photo in Zoom and Slack. 

## Jupyter notebook setup

From the repository root, create and activate a Python virtual environment, then
install the course dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name ds-summer-prep --display-name "Python (ds-summer-prep)"
```

Start JupyterLab with:

```bash
jupyter lab
```

When opening a notebook, select the **Python (ds-summer-prep)** kernel. In VS
Code or Codespaces, select that same kernel from the notebook's kernel picker.
Run these commands once per machine (or once per Codespace rebuild). The virtual
environment and Jupyter checkpoint folders are intentionally ignored by Git.

## Schedule / Topics
* Week 01: Thursday 23rd - Setup && How to Succeed
* Week 02: Thursday 30th - Python Basics, Github, and IDE Ninja Skillz
* Week 03: Thursday 06th - Beyond Python Basics - Libraries
* Week 04: Thursday 13th - Advanced Python

## Homework submission policy

- Submit exactly one homework notebook per PR.
- Do not combine multiple weeks or multiple students' work in one pull request.
- Copy the template into `homeworks/` and work on the copy, not the original template file.
- Use a unique filename prefix per student, not just initials. Bare initials are not accepted.
- Good examples include:
  - `faizan_khan_week_3_hw.ipynb`
  - `student_12345678_week_03_exercise.ipynb`
- A full name, CUNY/student ID, or another stable unique identifier is required in the filename prefix.
- Avoid names that are too generic or likely to collide across a shared repo.
- Keep the PR focused on the current week's assignment and avoid unrelated file changes.
- If a PR is left inactive for too long, it may receive a warning and then be closed automatically by the course bot.

# Git Workflow Refresher

How your work moves from the class repo to a graded submission, and back through review.

## The Big Picture

![Student Git Workflow](data/workflow-overview.png)

Three things you're working with:

- **Upstream repo** — the class repo. You don't have write access, and you shouldn't need it.

- **Your fork** — your personal copy of the class repo, under your own GitHub account. This is where you actually work.
- **Branches** — a separate "lane" inside your fork for one specific piece of work (like this week's homework), so it doesn't touch your `main`.

**In git terms**, those map to specific remote names — you'll see these in the terminal and in GitHub's UI:

```
upstream          → CUNYTechPrep/2026-ds-summer-prep       (the class repo)
origin            → YOUR-GITHUB-NAME/2026-ds-summer-prep   (your fork)
origin/main       → your fork's main branch
origin/week2      → your fork's week2 branch (last week's work)
```

`origin` is set automatically the moment you clone or open a Codespace from your fork — every push you do goes to `origin`. `upstream` is just what we call the class repo when we're talking about it; you don't need a local `upstream` remote for anything in this doc, since syncing happens through GitHub's **Sync fork** button, not the command line.

Why fork instead of working directly in the class repo? Isolation. Nothing you do in your fork can break the repo for anyone else, so you have full freedom to experiment.

Why branch instead of just committing to your fork's `main`? Same idea, one level down. Each week gets its own branch (`week2`, `week3`, ...) so your `main` stays a clean mirror of the class repo, and each week's work is easy to review on its own.

## This week: sync → branch → work → push

Your fork already exists from an earlier week, so today's steps are:

![Sync your fork](data/sync-fork.png)
![Press Sync](data/Sync-button.png)

1. **Sync your fork's `main`.** The class repo has moved on since you forked it (merged PRs, new files). On GitHub: your fork → `main` → **Sync fork**. Now your fork matches upstream.

2. **Create this week's branch** off your updated `main`, named `week{x}` (example: `week3`).
3. **Open a Codespace** from your fork, on the `main` branch.

![Your workflow in Codespaces](data/codespaces-workflow.png)

4. In the terminal, run `git status` to confirm where you are, then `git checkout week{x}` to move onto your branch.

5. **Don't edit the exercise file directly.** Copy it into `homeworks/`, rename it with your initials (example: `HM_Week_3_HW.ipynb`), and work on the copy.
6. Stage **only your file**: `git add homeworks/HM_Week_3_HW.ipynb` — not `git add .` (This is the single biggest avoidable cause of merge conflicts).
7. Commit the added file with a message: `git commit -m "completed week 3 hw"`
8. `git push`. First push on a brand-new branch prompts you to set an upstream — accept it, or run `git push --set-upstream origin week{x}`. Either way, this goes to *your fork*, not the class repo.

**Note:** You could also complete all these steps using the GUI instead, same result, less terminal wizardry.

## The Pull Request

This is the step that actually submits your work.

A pull request (PR) is a proposal: "take the commits on my branch and merge them into the upstream repo." Opening one shows a diff — an exact, line-by-line view of what you're proposing to add.

1. **Open the PR.** After you push, GitHub shows a "Compare & pull request" banner on your fork — click it. Don't see it? Go to your fork → **Pull requests** → **New pull request**.

![Open Pull Request](data/open-PR.png)

2. **Check the direction.** Base should be the upstream repo's `main`; compare should be your `week{x}` branch. You're proposing to merge your branch into the class repo, not the other way around.

![PR Compare](data/PR-compare.png)

3. **Review the diff**, add a short description if you want (what you did, anything you're unsure about), then **Create pull request**.


Why we do it this way instead of pushing straight to `main` ?

- **It's how real teams work.** Nobody with production access pushes straight to `main` at a real job — everything goes through a PR and a review first. This is that habit, early.
- **It's a checkpoint.** A PR is a moment where something (a person, a CI check) looks at your change before it lands anywhere permanent.
- **It's literally how you submit.** For us, the PR *is* the handoff — it's what gets graded.

![PR List](data/PR-list.png)

___

# CSC 121 - Python Programming

A modified version of Harvard's [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) (CS50P).

## What this course covers

This is an introductory, no-prior-experience course in Python, organized into ten modules (`module_0` through `module_9`) that build on each other week over week. It starts with the fundamentals — functions, arguments, variables, and return values — then moves into control flow with conditionals and loops, and how to reason about and debug errors using exceptions.

From there the course covers the tools that make Python useful day to day: working with libraries and packages (including calling APIs and parsing JSON), writing automated unit tests with `pytest`, reading and writing files (text, CSV, and images), and using regular expressions to validate and clean up messy input. The final modules introduce object-oriented programming — classes, inheritance, properties, and operator overloading — and close with a tour of more advanced language features such as type hints, comprehensions, generators, and unpacking.

Each module pairs its lecture material with a small set of hands-on labs, and each lab has a corresponding automated test, so the emphasis throughout is on writing code that is not just correct once, but verifiably correct — a theme that carries into the CI workflow described below.

The original course material is copyright Harvard University / David J. Malan and is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0). This repository is an adaptation of that material, shared under the same license (see [license](license)).

## What's different from CS50P

CS50P's own submission/grading tool (`check50`) has been replaced with a **Continuous Integration (CI)** workflow built on Git and GitHub Actions. Instead of running a grading CLI, students:

1. do the lab work on a branch,
2. push it to GitHub, and
3. open a pull request, which triggers a GitHub Actions workflow that runs the automated tests (`pytest`) and reports a score on the PR.

The goal is to use the same lecture content and labs as CS50P while practicing a realistic branch → push → pull request → CI → merge workflow.

## Prerequisites

You'll need three things installed before starting:

| Tool | Purpose | Install |
|---|---|---|
| Git | version control, branches, pull requests | https://git-scm.com/downloads |
| VS Code | editor used throughout the course | https://code.visualstudio.com/download |
| Python (3.10+) | runs the labs and tests | https://www.python.org/downloads/ |

In VS Code, also install the **Python** extension (from the Extensions view) so test discovery and debugging work out of the box.

## Setting up the repo

```bash
# 1. clone the repo
git clone <this-repo-url>
cd csc_121

# 2. create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 3. install dependencies
pip install -r requirements.txt

# 4. open in VS Code
code .
```

VS Code is already configured (see [.vscode/settings.json](.vscode/settings.json)) to run tests with `pytest`. Once the interpreter is set to `.venv`, you can run tests from the Testing panel, or from the terminal:

```bash
pytest
```

## Repository structure

```
csc_121/
├── readme.md                 # this file
├── license                   # CC BY-NC-SA 4.0
├── pyproject.toml            # pytest config (pythonpath=src, testpaths=tests)
├── requirements.txt          # python dependencies
├── .vscode/                  # editor settings (test runner config)
├── src/
│   ├── module_0/
│   │   ├── module_0_readme.md   # lecture link, labs, git branch, turn-in, CI instructions
│   │   ├── lab0_hello.py
│   │   └── ...
│   ├── module_1/
│   └── ...                   # one folder per course module (module_0 .. module_9)
└── tests/
    ├── module_0/
    │   └── test_lab0_functions.py
    ├── module_1/
    └── ...                   # mirrors src/, one test file per lab
```

- **`src/module_N/`** — starter/solution code for each module's labs, plus a `module_N_readme.md` describing the lecture, the labs to complete, and the turn-in/CI steps for that module.
- **`tests/module_N/`** — the automated tests (`pytest`) that CI runs against the corresponding lab code in `src/module_N/`.
- Each module's readme is the source of truth for that module's lecture link and lab list — start there.

## Working through a module

Each `module_N_readme.md` follows the same pattern:

1. **Git branch** — create a branch named for the module, e.g. `git checkout -b module_0`.
2. **Labs** — work through the labs listed in that module's readme, following the linked CS50P short.
3. **Turn-in** — run the tests locally, and once you're happy with the result:
   ```bash
   git add .
   git commit -m "module 0 labs"
   git push
   ```
4. **CI** — open a pull request on GitHub for that branch. This triggers a GitHub Actions run that executes the tests and reports your score directly on the PR.

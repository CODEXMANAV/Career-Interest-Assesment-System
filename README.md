# Python-Based Career Interest Assessment System

A beginner-level command-line program that asks students 10 yes/no questions about their interests and suggests a broad career area using simple scoring.

## Student
- **Name:** Manav Sharma
- **Programme:** CSE Core
- **University:** Vellore Institute of Technology
- **Course:** Introduction to Problem Solving

## Features
- 10 yes/no interest questions across 5 areas: Technology, People, Creative, Business, Science
- Input validation (only `y` or `n` accepted; anything else is re-prompted)
- Scores each area by counting "yes" answers and suggests the highest-scoring area
- Returns **Explore** if no question is answered "yes"
- Prints a score breakdown by area

## Project Structure
| File | Purpose |
|------|---------|
| `main.py` | Program entry point; runs questionnaire, assessment and report |
| `questionnaire.py` | Holds the questions and collects/validates answers |
| `assessor.py` | Interest scoring logic (`assess`) |
| `report.py` | Displays the result (`show_result`) |
| `test_project.py` | Basic test for the scoring logic |
| `design_notes.md` | Architecture and workflow notes |
| `statement.md` | Project statement and scope |
| `requirements.txt` | Dependencies (none required) |

## How It Works
```
User -> main.py -> questionnaire -> assessor -> report -> output
```
1. `get_answers()` asks each question and returns a list of `(area, "y"/"n")` pairs.
2. `assess(answers)` counts "y" answers per area and picks the highest.
3. `show_result(result)` prints the suggested area and all scores.

## How to Run
1. Install Python 3 (no external packages needed).
2. Open a terminal in the project folder.
3. Run:
   ```
   python main.py
   ```

## Example
```
--- Career Interest Assessment System ---
Do you enjoy solving logical problems? (y/n): y
...
--- Assessment Result ---
Suggested interest area: Technology
Score: 2

Scores by area:
Technology: 2
Creative: 1

Note: This is a simple educational assessment, not a professional career test.
```

## Testing
```
python test_project.py
```
Expected output: `All basic tests passed.`

## Technologies
- Python 3
- Python standard library only

## Limitations
- Ties go to the area that was scored first.
- Results are a simple educational guide, not a professional career test.

## Version Control
```
git init
git add .
git commit -m "Initial project submission"
```
Then create a GitHub repository, add it as the remote, and push.

## Submission Checklist
- [x] README.md
- [x] statement.md
- [x] Source code
- [x] Test file
- [ ] Project report PDF

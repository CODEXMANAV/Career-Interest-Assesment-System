QUESTIONS = [
    ("Do you enjoy solving logical problems?", "technology"),
    ("Do you enjoy helping and communicating with people?", "people"),
    ("Do you enjoy creative design and new ideas?", "creative"),
    ("Do you enjoy organizing money or business activities?", "business"),
    ("Do you enjoy experiments and scientific questions?", "science"),
    ("Do you enjoy building or fixing things?", "technology"),
    ("Do you enjoy presentations and teamwork?", "people"),
    ("Do you enjoy writing, drawing or content creation?", "creative"),
    ("Do you enjoy planning projects and budgets?", "business"),
    ("Do you enjoy observing and analyzing results?", "science")
]

def get_answers():
    answers = []
    for question, area in QUESTIONS:
        while True:
            value = input(question + " (y/n): ").strip().lower()
            if value in ["y", "n"]:
                answers.append((area, value))
                break
            print("Please enter y or n.")
    return answers

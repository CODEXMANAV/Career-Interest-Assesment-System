from questionnaire import get_answers
from assessor import assess
from report import show_result

def main():
    print("--- Career Interest Assessment System ---")
    answers = get_answers()
    result = assess(answers)
    show_result(result)

if __name__ == "__main__":
    main()

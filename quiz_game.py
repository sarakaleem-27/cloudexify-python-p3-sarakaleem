"""  CloudExify Python Internship
     Month 1   Project 3
     Quiz Game
     Sara Kaleem  |  Reg No: CX-INT-2026-PY-0159 """


import random
 
HIGH_SCORE_FILE = "highscore.txt"
QUESTIONS_PER_GAME = 10
 
question_bank = [
    {
        "text": "Which symbol is used to start a comment in Python?",
        "options": {"A": "//", "B": "#", "C": "<!--", "D": "**"},
        "correct": "B",
    },
    {
        "text": "What will print(10 % 3) show?",
        "options": {"A": "3", "B": "1", "C": "0", "D": "3.33"},
        "correct": "B",
    },
    {
        "text": "Which of these creates an empty dictionary?",
        "options": {"A": "dict()", "B": "[]", "C": "()", "D": "empty()"},
        "correct": "A",
    },
    {
        "text": "What keyword is used to repeat code while a condition is true?",
        "options": {"A": "loop", "B": "repeat", "C": "while", "D": "for"},
        "correct": "C",
    },
    {
        "text": "What does the len() function do?",
        "options": {
            "A": "Rounds a number",
            "B": "Returns the length of something",
            "C": "Converts to lowercase",
            "D": "Deletes an item",
        },
        "correct": "B",
    },
    {
        "text": "Which of these is a valid way to open a file for writing?",
        "options": {
            "A": "open('data.txt', 'r')",
            "B": "open('data.txt', 'w')",
            "C": "open('data.txt', 'read')",
            "D": "file.open('data.txt')",
        },
        "correct": "B",
    },
    {
        "text": "What is the data type of True in Python?",
        "options": {"A": "int", "B": "str", "C": "bool", "D": "float"},
        "correct": "C",
    },
    {
        "text": "How do you add an item to the end of a list called scores?",
        "options": {
            "A": "scores.append(5)",
            "B": "scores.add(5)",
            "C": "scores.push(5)",
            "D": "scores.insertEnd(5)",
        },
        "correct": "A",
    },
    {
        "text": "What does 'hello'.upper() return?",
        "options": {"A": "hello", "B": "Hello", "C": "HELLO", "D": "HELLo"},
        "correct": "C",
    },
    {
        "text": "Which block runs only if none of the earlier if/elif conditions matched?",
        "options": {"A": "else", "B": "except", "C": "finally", "D": "default"},
        "correct": "A",
    },
    {
        "text": "What does range(3) produce when looped over?",
        "options": {"A": "1, 2, 3", "B": "0, 1, 2", "C": "0, 1, 2, 3", "D": "3 only"},
        "correct": "B",
    },
    {
        "text": "Which keyword defines a reusable block of code?",
        "options": {"A": "func", "B": "define", "C": "def", "D": "method"},
        "correct": "C",
    },
    {
        "text": "What is the result of type([1, 2, 3])?",
        "options": {"A": "list", "B": "array", "C": "tuple", "D": "set"},
        "correct": "A",
    },
    {
        "text": "Which function converts user input into a whole number?",
        "options": {"A": "str()", "B": "float()", "C": "int()", "D": "num()"},
        "correct": "C",
    },
    {
        "text": "What does the try/except block handle?",
        "options": {
            "A": "Loops",
            "B": "Errors",
            "C": "File names",
            "D": "Comments",
        },
        "correct": "B",
    },
]
 
 
def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            saved_value = file.read().strip()
            if saved_value == "":
                return 0
            return int(saved_value)
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
 
 
def save_high_score_if_better(score):
    current_best = load_high_score()
    if score > current_best:
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(score))
        return True
    return False
 
 
def ask_one_question(question, number, total):
    print(f"\nQuestion {number}/{total}")
    print(question["text"])
 
    for letter in ["A", "B", "C", "D"]:
        print(f"  {letter}) {question['options'][letter]}")
 
    while True:
        answer = input("Your answer: ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("Please type A, B, C, or D.")
 
    if answer == question["correct"]:
        print("Correct!")
        return True
    else:
        correct_letter = question["correct"]
        correct_text = question["options"][correct_letter]
        print(f"Wrong. The correct answer was {correct_letter}) {correct_text}")
        return False
 
 
def get_grade(score, total):
    percent = (score / total) * 100
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"
 
 
def play_one_round():
    shuffled_questions = question_bank.copy()
    random.shuffle(shuffled_questions)
    round_questions = shuffled_questions[:QUESTIONS_PER_GAME]
 
    high_score = load_high_score()
    print("\n========================================")
    print("           PYTHON QUIZ GAME")
    print("========================================")
    print(f"Number of questions: {len(round_questions)}")
    print(f"Current high score: {high_score}")
    input("Press Enter to start...")
 
    score = 0
    question_number = 1
    for question in round_questions:
        correct = ask_one_question(question, question_number, len(round_questions))
        if correct:
            score = score + 1
        question_number = question_number + 1
 
    percent = (score / len(round_questions)) * 100
    grade = get_grade(score, len(round_questions))
 
    print("\n========================================")
    print("            QUIZ FINISHED")
    print("========================================")
    print(f"Score   : {score}/{len(round_questions)}")
    print(f"Percent : {percent:.1f}%")
    print(f"Grade   : {grade}")
 
    if save_high_score_if_better(score):
        print(f"New high score: {score}!")
    print("========================================")
 
 
def main():
    while True:
        play_one_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
 
 
if __name__ == "__main__":
    main()
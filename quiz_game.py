"""
Quiz Game - A simple text-based quiz using Python dictionaries.

This game asks the user a series of questions and checks their answers.
At the end, it shows the total score
"""

# Dictionary holding quiz questions and answers

quiz = {
    "What is the capital of India?": "Delhi",
    "What is 5 + 7?": "12",
    "What is the color of the sky?": "Blue"
}

score = 0

# Loop through each question

for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print('Correct Answer')
        score += 1
    else:
        print('Wrong Answer, Please try again!')

print(f"\nYour final score is {score} / {len(quiz)}")

match score:
    case 3:
        print("Quiz master!")
    case 2:
        print("Close enough!")
    case _:
        print("Needs improvement")




title = "Loop Practice Quiz"
score = 0

quiz_questions = [
   { "question": "1. What is the output of the following code snippet?", "answer": "1 5 7 11 13 17 19" ,"snippet": "for i in range(1, 20):\n    if i % 2 != 0 and i % 3 != 0:\n        print(i)"},
   { "question": "2. What is the output of the following code snippet?", "answer": "1 5 7 11 13 17 19" ,"snippet": "for i in range(1, 20):\n    if i % 2 != 0 and i % 3 != 0:\n        print(i)"},
   { "question": "3. What is the output of the following code snippet?", "answer": "1 5 7 11 13 17 19" ,"snippet": "for i in range(1, 20):\n    if i % 2 != 0 and i % 3 != 0:\n        print(i)"}
]
print(f"\n{title}")
print("Press any key to start the quiz...  Press q to quit.")
if input().lower() == "q":
    print("Thanks for playing! Goodbye.")
    raise SystemExit
for item in quiz_questions:
    print("\n" + item["question"])
    print("Snippet: \n" + item["snippet"])
    user_answer = input("Your answer: ")
    if user_answer == item["answer"]:
        print("Great job! You got it right.")
        score += 1
    else:
        print("Sorry, that's not correct.")

print(f"\n quiz completed! Your score is {score}/{len(quiz_questions)}")
if input("Would you like to play again? (y/n): ") == "y":
    exec(open("loop_practice.py").read())
else:
    print("Thanks for playing! Goodbye.")
    
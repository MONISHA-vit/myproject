
# Simple Python Quiz Program

questions = [
    {
        "question": "1. What is the output of: print(2 * 3)?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 23"],
        "answer": "B"
    },
    {
        "question": "2. Which data type is mutable in Python?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
        "answer": "C"
    },
    {
        "question": "3. What keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    }
]

score = 0

print("=== PYTHON QUIZ ===")
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer == q["answer"]:
        print("✔ Correct!")
        score += 1
    else:
        print(f"✘ Wrong! Correct answer is: {q['answer']}")

print(f"\nYour final score: {score}/{len(questions)}")

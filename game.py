import random

#These are the Quiz questions
quiz = [
    {
        "question": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "answer": "4"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Who is the greatest basketball player ever?",
        "options": ["Tom Brady", "Stephen Curry", "Alex Caruso", "Lebron James"],
        "answer": "Lebron James"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Central Program Unit", "Control Processing Unit"],
        "answer": "Central Processing Unit"
    }
]
random.shuffle(quiz)

for i,q in enumerate(quiz,start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for idx, option in enumerate(q['options'],start=1):
        print(f"{idx}. {option}")
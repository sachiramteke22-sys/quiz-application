questions = {
    "Capital of india ?": "Delhi",
    "4+6?": "10",
    "coding is easy ?": "NO",
    "vibe coding is easy?": "yes",
    
    
    
}

score = 0

for question, answer in questions.items():
    user = input(question + " ")
    
    if user.lower() == answer.lower():
        score += 1
print("Score:", score)
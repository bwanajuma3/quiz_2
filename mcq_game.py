
questions = [
    {
        "question": "1. A patient presents with hypotension, distended neck veins, and absent breath sounds on the right after chest trauma. What is the most likely diagnosis?",
        "options": [
            "A. Haemothorax",
            "B. Tension pneumothorax",
            "C. Cardiac tamponade",
            "D. Pulmonary contusion"
        ],
        "answer": "B"
    },
    {
        "question": "2. What is the most appropriate initial fluid for resuscitation of an adult with major burns?",
        "options": [
            "A. 5% dextrose",
            "B. 3% saline",
            "C. Ringer's lactate",
            "D. 20% albumin"
        ],
        "answer": "C"
    },
    {
        "question": "3. Which clinical feature is most suggestive of strangulated intestinal obstruction?",
        "options": [
            "A. Intermittent colicky pain only",
            "B. Passage of normal stool",
            "C. Painless abdominal distension",
            "D. Continuous severe pain with systemic toxicity"
        ],
        "answer": "D"
    }
]

score = 0

print("\n===== SURGERY QUIZ 2 =====")

for item in questions:
    print("\n" + item["question"])

    for option in item["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print("Correct answer:", item["answer"])

print("\n===== RESULTS =====")
print("Score:", score, "/", len(questions))
print("Percentage:", round(score / len(questions) * 100), "%")

if score == 3:
    print("Excellent! All answers correct.")
elif score == 2:
    print("Good work! Revise the question you missed.")
else:
    print("Keep practising and reviewing the key surgical principles.")


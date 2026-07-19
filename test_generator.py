from src.generator import generate_quiz

quiz = generate_quiz("Cricket")

for i, question in enumerate(quiz, start=1):
    print(f"\nQuestion {i}")
    print(question["question"])

    print("\nOptions:")
    for option in question["options"]:
        print("-", option)

    print("\nCorrect Answer:", question["answer"])
    print("Difficulty:", question["difficulty"])
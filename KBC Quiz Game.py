def kbc():
    questions = [
        {
            "question": "What is my name?",
            "options": ["a. Vaibhav", "b. Rohit", "c. Sidd", "d. Shreyash"],
            "ans": "a"
        },
        {
            "question": "Name of the financial capital of India?",
            "options": ["a. Delhi", "b. Bengaluru", "c. Mumbai", "d. Pune"],
            "ans": "c"
        },
        {
            "question": "Where is Maharashtra located?",
            "options": ["a. East", "b. West", "c. North", "d. South"],
            "ans": "b"
        },
        {
            "question": "What is the capital of India?",
            "options": ["a. Mumbai", "b. Karnataka", "c. Noida", "d. Delhi"],
            "ans": "d"
        }
    ]
    prize = 0  # initialize prize

    print("\nWelcome to KBC!\n")

    for i in range(len(questions)):
        print("Question", i + 1, ":", questions[i]["question"])  # print the question text
        for opt in questions[i]["options"]:  # print the options from the dictionary
            print(opt)

        user_ans = input("Enter your answer (a/b/c/d): ")

        if user_ans == questions[i]["ans"]:
            prize += 1000  # Add 1000 for each correct answer
            print("Correct! You won ₹1000.\n")
        else:
            print("Wrong answer! Game Over.\n")
            break

    print("You won a total of ₹", prize)

# Run the game
kbc()

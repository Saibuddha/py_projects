questions = [
    {
        "q": "who is the founder of Nothing electronics?",
        "options": ["A. Carl Pei", "B. Steve Jobs", "C. Pete Lau"],
        "answer": "A"
    },
    {
        "q": "when is the first Iphone launched?",
        "options": ["A. 2001", "B. 2007", "C. 2009"],
        "answer": "B"
    },
    {
        "q": "who is the founder of Nvidia?",
        "options": ["A. Steve Jobs", "B. Jensen Huang", "C. Mark Zuckerberg"],
        "answer": "B"
    },
    {
        "q": "who is the creator of python?",
        "options": ["A. Guido Van Rossum", "B. Linus Torvalds", "C. Sergey Brin"],
        "answer": "A"
    },
    {
        "q": "Google was founded in the year?",
        "options": ["A. 1990", "B. 1998", "C. 2001"],
        "answer": "B"
    },
    {
        "q": "who is the founder of Bitcoin?",
        "options": ["A. Satoshi Nakamoto", "B. Craig Wright", "C. Jack Dorsey"],
        "answer": "A"
    },
    {
        "q": "who is the creator of Ethereum?",
        "options": ["A. Elon Musk", "B. Satoshi Nakamoto", "C. Vitalik Buterin"],
        "answer": "C"
    },
    {
        "q": "Fullform of DAPP",
        "options": ["A. Dramatic Approver", "B. Decentralised Application", "C. Decentralised Approval"],
        "answer": "B"
    },
    {
        "q": "Bitcoin is created in the year?",
        "options": ["A. 2001", "B. 2007", "C. 2009"],
        "answer": "C"
    },
    {
        "q": "which of the following is a web3 company?",
        "options": ["A. Amazon", "B. Polkadot", "C. Instagram"],
        "answer": "B"
    },

]

def run_quest(questions):
    points = 0
    for question in questions:
        print(question["q"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A, B, or C):").strip().upper()
        if answer == question["answer"]:
            print("Correct Answer, You are good to move on!\n")
            points += 1
        else:
            print("LOSERRR!!! The correct answer is", question["answer"], "\n")
    
    print(f"You scored {points} out of {len(questions)} questions correct.")

run_quest(questions)

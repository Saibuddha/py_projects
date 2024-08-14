import random

words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself"},
    {"spanish": "no", "english": "no"},
    {"spanish": "haber", "english": "to have"},
    {"spanish": "por", "english": "for"},
    {"spanish": "con", "english": "with"},
    {"spanish": "para", "english": "for"},
    {"spanish": "como", "english": "as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "to him/her"},
    {"spanish": "lo", "english": "the"},
    {"spanish": "lo", "english": "the"},
    {"spanish": "todo", "english": "all"}
    # add more words as you prefer and change format if need be 
]

def learn_lang(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the english translation of '{word['spanish']}")
        user_answer = input("Your answer(Type 'quit' or 'exit' to quit): ").strip().lower()
        
        if user_answer in ['quit', 'exit']:
            print("user wants to quit!")
            break
        
        correct_answers = word['english'].lower().split('/')

        if user_answer in correct_answers:
            print("Correct!!\n!")
            score += 1
        
        else:
            print(f"Wrong, learn your vocab! The correct answer is '{word['english']}'.\n")
        
    
    print(f"Quiz complete! you scored : {score}/{len(words)}")

def main():
    print("Welcome to the language learning program!")
    input("Press Enter to start the program!")
    learn_lang(words)

if __name__ == "__main__":
    main()

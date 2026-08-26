
def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text:
        return "I'm a simple rule-based chatbot."
    elif "help" in text:
        return "You can talk to me by typing greetings, asking how I am, or saying bye."
    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("Chatbot: Hi! Type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    chat()
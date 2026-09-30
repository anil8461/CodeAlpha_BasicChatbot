def chatbot():
    print("================================")
    print("      🤖 Simple Chatbot")
    print("================================")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi! How can I help you?")

        elif "how are you" in user_input:
            print("Bot: I'm fine, thanks! 😊")

        elif "your name" in user_input:
            print("Bot: My name is SimpleBot.")

        elif "what can you do" in user_input:
            print("Bot: I can have a simple conversation with you.")

        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day! 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot.")

        elif "help" in user_input:
            print("Chatbot: I can answer greetings, tell my name, and respond to basic questions.")

        elif "weather" in user_input:
            print("Chatbot: I can't check live weather, but it's always a good idea to carry an umbrella!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
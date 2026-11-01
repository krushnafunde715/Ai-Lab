print("\n =====Rule based chatbot===== \n")
print("Chatbot: Hello! I am a simple chatbot.")
print("Enter 'bye' to end the chat \n")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Chatbot: Hello! How are you?")

    elif "how are you" in user:
        print("Chatbot: I am fine. How are you?")

    elif "i am fine" in user:
        print("Chatbot: Okayy!!, How can i help you?")

    elif "what is your name" in user:
        print("Chatbot: My name is simplebot")

    elif "bye" in user:
        print("Chatbot: Goodbye !!")
        break

    else:
        print("Chatbot: Sorry!, I dont understand")



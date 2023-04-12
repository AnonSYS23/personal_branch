def greet():
    print("Hello! I'm a chatbot. How can I assist you today?")

def respond(input_text):
    if "hello" in input_text.lower():
        return "Hi there!"
    elif "how are you" in input_text.lower():
        return "I'm doing well, thank you. How about you?"
    elif "goodbye" in input_text.lower():
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I don't understand. Could you please rephrase your question?"

greet()

while True:
    user_input = input("You: ")
    bot_response = respond(user_input)
    print("Chatbot:", bot_response)

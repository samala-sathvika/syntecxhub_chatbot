import datetime
import string

def log_chat(user, bot):
    with open("chat_log.txt", "a") as file:
        file.write(f"USER: {user}\n")
        file.write(f"BOT: {bot}\n")

def chatbot_response(user_input):
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you?"

    elif "how are you" in user_input:
        return "I'm doing great!"

    elif "help" in user_input:
        return "Ask me about AI, Python, or chatbots."

    elif "ai" in user_input:
        return "AI is Artificial Intelligence."

    elif "python" in user_input:
        return "Python is a programming language."

    elif user_input in ["bye", "exit"]:
        return "Goodbye!"

    else:
        return "I don't understand."

# 👉 THIS PART IS IMPORTANT
print("Chatbot started. Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    log_chat(user_input, response)

    if user_input.lower() == "exit":
        break
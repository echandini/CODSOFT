import datetime
import random

print("===================================")
print("      AI RULE-BASED CHATBOT")
print("===================================")

name = input("Enter your name: ")
print(f"Hello {name}! Type 'bye' to exit.\n")

jokes = [
    "Why do programmers prefer Python? Because it is easy to understand!",
    "Why did the computer get cold? Because it forgot to close Windows!",
    "AI is like magic, but with code."
]

while True:

    user = input(f"{name}: ").lower()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Asking chatbot name
    elif "your name" in user:
        print("Bot: I am an AI Rule-Based Chatbot.")

    # Asking user name
    elif "my name" in user:
        print(f"Bot: Your name is {name}")

    # How are you
    elif "how are you" in user:
        print("Bot: I am working perfectly!")

    # Date
    elif "date" in user:
        today = datetime.date.today()
        print("Bot: Today's date is:", today)

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is:", current_time)

    # Joke feature
    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    # Simple calculator
    elif "add" in user:
        try:
            nums = user.split()
            num1 = int(nums[1])
            num2 = int(nums[2])
            print("Bot: Sum =", num1 + num2)
        except:
            print("Bot: Use format -> add 5 10")

    # Help command
    elif "help" in user:
        print("Bot: You can ask me about:")
        print("- time")
        print("- date")
        print("- joke")
        print("- your name")
        print("- add numbers")

    # Exit
    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a great day.")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")
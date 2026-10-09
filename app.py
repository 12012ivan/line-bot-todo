print("Todo Bot started")

while True:
    message = input("You: ")

    if message == "quit":
        print("Bot stopped")
        break

    elif message.startswith("record:"):
        task = message[7:].strip()

        if task:
            print("Bot: Recorded -", task)
        else:
            print("Bot: Please enter a task.")

    else:
        print("Bot: Use record: followed by your task.")
tasks = []

print("Todo Bot started")

while True:
    message = input("You: ").strip()

    if message == "quit":
        print("Bot stopped")
        break

    elif message == "list":
        if tasks:
            print("Bot: Your tasks:")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
        else:
            print("Bot: No tasks recorded yet.")

    elif message.startswith("record:"):
        task = message[7:].strip()

        if task:
            tasks.append(task)
            print("Bot: Recorded -", task)
        else:
            print("Bot: Please enter a task.")

    else:
        print("Bot: Use record: followed by your task, or type list.")

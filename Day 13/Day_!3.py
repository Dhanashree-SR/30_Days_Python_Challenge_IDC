class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"✅ '{item}' pushed to stack.")

    def pop(self):
        if not self.items:
            print("⚠️ Stack is empty. Cannot pop.")
        else:
            removed = self.items.pop()
            print(f"✅ Popped item: {removed}")

    def peek(self):
        if not self.items:
            print("⚠️ Stack is empty.")
        else:
            print(f"👀 Top of the stack: {self.items[-1]}")

    def display(self):
        print("📦 Current Stack:", self.items[::-1] if self.items else "Empty Stack")

# CLI interaction
def run_stack_app():
    stack = Stack()
    print("📘 Stack CLI App - Type 1 to Push, 2 to Pop, 3 to Peek, 4 to Display, 5 to Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                value = input("Enter value to push: ")
                stack.push(value)
            elif choice == 2:
                stack.pop()
            elif choice == 3:
                stack.peek()
            elif choice == 4:
                stack.display()
            elif choice == 5:
                print("👋 Exiting the program.")
                break
            else:
                print("❌ Invalid choice. Please select between 1 to 5.")
        except ValueError:
            print("❌ Please enter a valid number.")

# Run the app
run_stack_app()

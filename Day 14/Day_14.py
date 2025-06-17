def factorial(n):
    # Step 2: Base case
    if n == 1:
        return 1
    else:
        # Step 3: Recursive call
        return n * factorial(n - 1)

# Step 4: Input from user
try:
    num = int(input("Enter a number to calculate factorial: "))
    if num < 1:
        print("❌ Please enter a positive integer.")
    else:
        result = factorial(num)
        print(f"✅ Factorial of {num} is {result}")
except ValueError:
    print("❌ Invalid input! Please enter an integer.")

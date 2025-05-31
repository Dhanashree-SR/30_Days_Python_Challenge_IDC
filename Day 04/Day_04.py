# ✅ Prime Number Checker Program
print("🔢 Welcome to the Prime Number Checker!\n")
print("You can test any number to see if it's prime.\n")

num = int(input("Enter a number: "))

# Edge cases: 0 and 1 are not prime
if num <= 1:
    print(f"\n{num} is not a prime number ❌\n")
else:
    # Loop from 2 to square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number ❌\n")
            print(f"It is divisible by {i} (i.e., {i} x {num // i} = {num})\n")
            break
    else:
        print(f"{num} is a prime number ✅\n")

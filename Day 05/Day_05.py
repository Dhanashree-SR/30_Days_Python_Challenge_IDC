# ✅ 1. Without Parameters, Without Arguments
def calc1():
    print("\nType 1: No Parameters, No Arguments")
    numbers = [10, 20, 30]
    total = sum(numbers)
    average = total / len(numbers)
    print(f"List: {numbers}")
    print(f"Sum: {total}, Average: {average}")

# ✅ 2. With Parameters, With Arguments
def calc2(numbers):
    print("\nType 2: With Parameters, With Arguments")
    total = sum(numbers)
    average = total / len(numbers)
    print(f"List: {numbers}")
    print(f"Sum: {total}, Average: {average}")

# ✅ 3. With Parameters, Without Arguments (Using default value)
def calc3(numbers=[5, 10, 15]):
    print("\nType 3: With Parameters, No Arguments (Default Used)")
    total = sum(numbers)
    average = total / len(numbers)
    print(f"List: {numbers}")
    print(f"Sum: {total}, Average: {average}")

# ✅ 4. Lambda Function
sum_lambda = lambda numbers: sum(numbers)
avg_lambda = lambda numbers: sum(numbers) / len(numbers)

def calc4():
    print("\nType 4: Using Lambda Function")
    numbers = [2, 4, 6, 8]
    print(f"List: {numbers}")
    print(f"Sum: {sum_lambda(numbers)}, Average: {avg_lambda(numbers)}")

# 🔄 Function Calls
calc1()
calc2([50, 60, 70])
calc3()
calc4()

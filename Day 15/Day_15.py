import time
# ⏱️ Decorator to log execution time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"🚀 Running: {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n ⏱️ Finished in {end_time - start_time:.4f} seconds\n")
        return result
    return wrapper
# 🔁 Function 2: Reverse a string
@timer_decorator
def reverse_string(s):
    reversed_str = s[::-1]
    print(f"🔄 Reversed: {reversed_str}")
    return reversed_str
# 🚀 Run the functions
print("🧪 Decorator Demo:\n")
reverse_string("IDC Python Challenge...")

# 🚨 Day 1️⃣0️⃣: Exception Handling in Python

📅 **Date:** June 6, 2025  
📚 **Challenge:** [Indian Data Club - #30DaysOfPython](https://www.linkedin.com/company/indian-data-club/)

---

## 🧠 Topics Covered

- `try` and `except` blocks
- Catching specific exceptions
- Using `finally` for clean-up
- Real-life use case: reading numbers from a file with error handling


## 📌 What is Exception Handling?

In Python, exception handling is a way to manage **runtime errors** without crashing your program.

It helps you catch mistakes like dividing by zero, missing files, or invalid user input — and respond gracefully!

### 🔧 Syntax:

```python
try:
    # Code that might raise an error
except SomeError:
    # Handle the error
finally:
    # Code that will always run
````


## 🧪 Simple Example

```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Oops! That was not a valid number.")
finally:
    print("Execution finished.")
```


## 🎯 Daily Challenge

**Task:**
Write a Python program that:

1. Tries to read numbers from a file.
2. Handles errors like:

   * File not found
   * Non-integer values in the file
3. Prints only the valid numbers.

📁 File-based real-world error handling — simulating a data read pipeline! 📊



## 🔗 Resources Used

* 📺 [Exception Handling – Python Programming Tutorials (YouTube)](https://www.youtube.com/watch?v=kqVQDXfc9hU)
* 🎥 [Try Except in Python – 3 Minutes Crash Course](https://youtu.be/QTVcbdVILsA?si=qJNsmVC-quuZ7uAA)



## 🚀 Reflections

Learning to **fail safely** is just as important as writing correct code. Today’s challenge taught me how to anticipate and manage errors — like a pro! 😎


## 🏁 Streak Update

🎉 Proud to share — I’ve officially completed **10 Days in a Row** of this challenge!

And… I received a **personalized 7-day streak badge** from Indian Data Club! 🏅
It’s the little wins that keep us going. Let’s push forward 🚀


<img src="https://github.com/user-attachments/assets/6b0f0841-fd47-4c8c-9d1c-887332d4b192" height="540" width="540"/>


## 💡 Connect With Me


LinkedIn - [Click here to view my profile](https://www.linkedin.com/in/dhanashree-sr/)

🗺️ Notion Roadmap: [Click Here](https://www.notion.so/dhanashreesr/30DaysOfPython-Tracker-d0c88bdb3a2f4d43b792a9a93b4235b7)


🤝 Let’s Learn Together: [Discord Community](https://discord.com/channels/1298526897788944474/1298572243680624692)

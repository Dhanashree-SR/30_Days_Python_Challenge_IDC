# 📅 Day 14 – Recursion in Python

## 🧠 Topics Covered

- Recursive functions
- Base cases
- Function call stack (how Python tracks recursive calls)

## 🎯 Challenge
Write a recursive function to calculate the factorial of a number.

## 📖 Concepts Explained


🔁 What is Recursion?
Recursion is a method where the solution to a problem depends on solving smaller instances of the same problem.
In Python, this means a function calling itself with modified input.

**📌 Base Case vs Recursive Case**



Base case: The condition at which recursion stops (e.g., n == 0)


Recursive case: Function keeps calling itself with a smaller input (e.g., factorial(n-1))

## Real-Life Analogy
Think of a Matryoshka doll (Russian nesting doll):
You open one doll, and inside is a smaller one, then a smaller one...
Until you reach the tiniest one (base case) — then you start stacking them back.
That’s exactly how recursion works — unwrapping and wrapping!


### 📁 File
- `day14_.py` Check the implementation → [Day\_14.py](./Day_14.py)



## 💡 Key Takeaways
- Recursion can simplify problems that have repetitive structure.
- Always define a base case, or you'll end up in an infinite loop!
- Useful for problems like factorial, Fibonacci, tree traversals, etc.

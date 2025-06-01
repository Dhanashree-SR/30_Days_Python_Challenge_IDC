# 📘 Day 0️⃣5️⃣: Functions in Python

📅 **Date:** June 1, 2025

## 🗒️ Topics Covered

### 1. Defining Functions

Functions help organize code into reusable blocks. They are defined using the `def` keyword.

```python
def greet():
    print("Hello!")
````

### 2. Parameters vs Arguments

* **Parameters** are variables listed in the function definition.
* **Arguments** are the actual values passed when calling the function.

```python
def greet(name):     # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Dhanashree")   # "Dhanashree" is an argument
```

---

## ✨ Types of Functions (Based on Parameters & Arguments)

| Type | Description                                               |
| ---- | --------------------------------------------------------- |
| 1️⃣  | Without Parameters, Without Arguments                     |
| 2️⃣  | With Parameters, With Arguments                           |
| 3️⃣  | With Parameters, Without Arguments (using default values) |
| 4️⃣  | Lambda Function (Anonymous function)                      |

---

## ⚡ Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword. Commonly used for simple operations.

```python
sum_lambda = lambda nums: sum(nums)
avg_lambda = lambda nums: sum(nums) / len(nums)

numbers = [10, 20, 30]
print(sum_lambda(numbers))   # 60
print(avg_lambda(numbers))   # 20.0
```

---

## 🎯 Challenge

**Task:** Write a function that computes the **sum** and **average** of a list of numbers.
💡 Bonus: Try writing it in all 4 function types!


### 📁 [Click here to view the full code](./Day_05.py)
---

## 📚 Resources

* [10. Functions \[Python 3 Programming Tutorials\]](https://youtu.be/fz_BCnhEQYQ?si=TZwuDalb0bjDtAzz)


📒 **#30DaysOfPython Roadmap Link:** [Click Here to View](https://indiandataclub.notion.site/30DaysOfPython-1f9a16c0422f8074bf29eee315a6802a)

---

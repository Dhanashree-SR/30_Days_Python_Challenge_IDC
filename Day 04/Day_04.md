# 📘 Day 0️⃣4️⃣: Control Structures in Python

📅 **Date:** May 31, 2025

---

## 🗒️ Topics Covered

### 1. Conditional Statements (`if`, `elif`, `else`)

Control the flow of your program by making decisions based on conditions.

**Example:**

```python
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
```

### 2. Loops (`for`, `while`)

Used to repeat a block of code multiple times.

* **For loop:** Iterates over a sequence (like a list or range).

```python
for i in range(5):
    print(i)
```

* **While loop:** Repeats as long as a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### 3. Loop Control Statements (`break`, `continue`, `else`)

* **`break`**: Exit the loop immediately.

```python
for i in range(10):
    if i == 3:
        break
    print(i)  # Prints 0, 1, 2 then stops
```

* **`continue`**: Skip the current iteration and continue with the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Skips 2
```

* **`else` with loops**: Runs if the loop completes normally without hitting `break`.

```python
for i in range(3):
    print(i)
else:
    print("Loop ended without break")
```
---

## 📚 Resources

* [If Statement \[Python 3 Programming Tutorials\]](https://youtu.be/hNddJ3_hahk?si=Xnauey3iEAxaO6qq)
* [For loop \[Python 3 Programming Tutorials\]](https://www.youtube.com/watch?v=3ykIpmAxdoY&list=PLeo1K3hjS3uv5U-Lmlnucd7gqF-3ehIh0&index=10)
* [Break, Continue, Pass in Python](https://www.youtube.com/watch?v=yCZBnjF4_tU)

---

## 🎯 Challenge
Build a program that:
* Checks if a number entered by the user is prime.<br/>
📁 [Click here to view the full code](./Day_04.py)
---


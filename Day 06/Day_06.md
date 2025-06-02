# 📘 Day 0️⃣6️⃣: Modules & Packages in Python

📅 **Date:** June 2, 2025

## 🗒️ Topics Covered

### 🧠 What are Modules in Python?

Modules are files containing Python code — such as **functions**, **classes**, or **variables** — that can be reused across multiple programs. They help in keeping code **organized**, **modular**, and **easy to maintain**.

### 1. **Importing Built-in Modules**

Python provides many powerful modules out of the box.

#### 🔹 Example: `math` Module
```python
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592...
````

#### 🔹 Example: `random` Module

```python
import random

print(random.randint(1, 10))        # Random number between 1 and 10
print(random.choice(['a', 'b']))    # Randomly selects one item
```

---

### 2. **Creating and Importing Custom Modules**

You can define your own `.py` file with reusable code and import it in other files.

#### ✅ Example Structure:

```
📁 project/
   ├── main.py
   └── my_module.py
```

#### 🔸 `my_module.py`

```python
def greet(name):
    return f"Hello, {name}!"
```

#### 🔸 `main.py`

```python
import my_module

print(my_module.greet("Dhanashree"))
```

---

### 💎 Bonus: Other Useful Built-in Modules

* `datetime` – Work with date & time
* `os` – Interact with files & folders
* `sys` – Handle system-specific info
* `json` – Parse JSON data

```python
import datetime
print(datetime.datetime.now())
```

---

### 💡 Pro Tip

Use `dir()` to explore module contents:

```python
import math
print(dir(math))
```

---

## 🎯 Challenge

### 🔐 Task:

**Generate a random 8-character password** using:
* Letters (uppercase & lowercase)
* Numbers
* Symbols

📁 Click here to view the full code → [Day\_06.py](./Day_06.py)

---

## 📚 Resources

* [🎥 Modules – Python 3 Programming Tutorials (YouTube)](https://youtu.be/DdGVBZv46PI?si=CARXC5ZoKysQL2CG)

---

## 🧾 Summary

* Modules help you avoid rewriting code
* Python includes many useful built-in modules
* You can write your own reusable modules
* Today's challenge gave you a real-world use case

---

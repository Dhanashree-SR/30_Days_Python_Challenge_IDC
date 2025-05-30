# 📘 Day 0️⃣3️⃣: Lists, Tuples, Sets, and Dictionaries

📅  **Date: May 30, 2025**

---

## 🗒️ Topics Covered

- Python Data Structures:
  - Lists (mutable, ordered, allows duplicates)
  - Tuples (immutable, ordered, allows duplicates)
  - Sets (mutable, unordered, no duplicates)
  - Dictionaries (mutable, key-value pairs, no duplicate keys)
  - Mutability and common operations for each data type

---

## 🧠 Mutability Overview

| Data Type   | Mutable? | Ordered? | Allows Duplicates? | Indexed? |
|-------------|----------|----------|---------------------|----------|
| **List**    | ✅ Yes    | ✅ Yes   | ✅ Yes              | ✅ Yes   |
| **Tuple**   | ❌ No     | ✅ Yes   | ✅ Yes              | ✅ Yes   |
| **Set**     | ✅ Yes    | ❌ No    | ❌ No               | ❌ No    |
| **Dict**    | ✅ Yes    | ✅ Yes   | ❌ Keys must be unique | ✅ Keys used as index |

---

## 🔹 Lists

- Syntax: `my_list = [1, 2, 3]`
- Stores a sequence of items, allows duplicates

```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.remove(2)
my_list[0] = 10
print(len(my_list))
````

---

## 🔹 Tuples

* Syntax: `my_tuple = (1, 2, 3)`
* Immutable, cannot be changed after creation

```python
my_tuple = (10, 20, 30)
print(my_tuple[0])
print(len(my_tuple))
# my_tuple[0] = 5  # ❌ Will throw an error
```

---

## 🔹 Sets

* Syntax: `my_set = {1, 2, 3}`
* Stores only unique elements, unordered

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(len(my_set))
```

---

## 🔹 Dictionaries

* Syntax: `my_dict = {'apple': 10, 'banana': 5}`
* Stores key-value pairs, keys must be unique

```python
inventory = {'pen': 5, 'pencil': 10}
inventory['pen'] = 15
inventory['eraser'] = 8
del inventory['pencil']
print(inventory['pen'])
```

---

## 📚 Resources

* [Python Lists, Tuples, and Sets – Tech With Tim](https://youtu.be/W8KRzm-HUcc?si=Y17f4RWk3NIHs-Rx)
* [Dictionaries and Tuples – CodeBasics](https://www.youtube.com/watch?v=RCM-lVAfXFg&list=PLeo1K3hjS3uv5U-Lmlnucd7gqF-3ehIh0&index=12)

---

## 🎯 Challenge

✅ Create an **Inventory Management System** using a dictionary that allows:

* Viewing items
* Adding new items
* Updating quantities
* Deleting items
* Checking item presence

---

📒 **#30DaysOfPython Roadmap Link:** [Click Here to View](https://indiandataclub.notion.site/30DaysOfPython-1f9a16c0422f8074bf29eee315a6802a)

---

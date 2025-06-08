# 📅 **Day 1️⃣2️⃣: Regular Expressions (Regex)**

**Date:** June 8, 2025

---

## ✅ What is Regex?

Regular Expressions (Regex) are sequences of characters used to search, match, or validate patterns in strings. In Python, we use the `re` module to work with regex.

---

## 🔧 Commonly Used `re` Functions

| Function        | Description                                    |
| --------------- | ---------------------------------------------- |
| `re.match()`    | Matches a pattern at the beginning of a string |
| `re.search()`   | Searches the whole string for a match          |
| `re.findall()`  | Returns all non-overlapping matches in a list  |
| `re.finditer()` | Returns an iterator of match objects           |
| `re.sub()`      | Replaces occurrences of the pattern            |
| `re.split()`    | Splits a string by the pattern                 |

---

## 🔤 Regex Syntax Cheatsheet

| Pattern | Description                  |
| ------- | ---------------------------- |
| `.`     | Any character except newline |
| `^`     | Start of string              |
| `$`     | End of string                |
| `*`     | Zero or more                 |
| `+`     | One or more                  |
| `[]`    | Set of characters            |
| `{n}`   | Exactly n times              |
| `\d`    | Any digit                    |
| `\w`    | Word character               |
| `\s`    | Whitespace                   |

---

## 🏡 Real-World Analogy

Using Regex is like having a smart filter that can extract exactly what you’re looking for from messy or unstructured data — like finding needles in a haystack!

---

## 🎯 Challenge

Validate Gmail addresses using a regular expression. The regex should only accept emails that match this pattern:
`username@gmail.com`
Where username can include letters, numbers, dots, underscores, and certain symbols like `+` and `%`.


📁 Check the implementation → [Day\_12.py](./Day_12.py)

![day12](https://github.com/user-attachments/assets/85d9f347-de1d-48a6-86b4-6ae609acb04d)

---

## 📤 Sample Output

```
me@gmail.com → ✅ Valid Gmail ID  
you@outlook.com → ❌ Invalid Gmail ID  
fake@gmail → ❌ Invalid Gmail ID  
hi@gmail.com → ✅ Valid Gmail ID  
hello@@gmail.com → ❌ Invalid Gmail ID  
dhanashree@outlook.com → ❌ Invalid Gmail ID  
check123*_@gmail.com → ❌ Invalid Gmail ID  
dhanashreesr@gmail.com → ✅ Valid Gmail ID  
deepika123@gmail.com → ✅ Valid Gmail ID  
```

---

## 😂 Meme Time!

![galaxy brain](https://github.com/user-attachments/assets/c0be39d0-ac93-4c59-b42c-ed7eeaa04cd1)

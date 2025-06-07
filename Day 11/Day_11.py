from datetime import datetime, timedelta
# 🕰️ Current date and time
now = datetime.now()
print("Current Date & Time:", now)

# 📆 Formatting the date
formatted = now.strftime("%d-%m-%Y %H:%M:%S\n")
print("Formatted Date & Time:", formatted)

# 🧮 Ask user to input two dates in YYYY-MM-DD format
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

# 📌 Convert strings to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

# 🔁 Calculate difference using timedelta
difference = abs(date2 - date1)
print(f"\n📊 The difference between {date_str1} and {date_str2} is {difference.days} days.")

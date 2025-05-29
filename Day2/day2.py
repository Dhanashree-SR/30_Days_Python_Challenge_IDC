# - Calculate the area of a rectangle using user-input length and width

# Type 1: Using hardcoded values
print("-------Type 1-------")
length = 5
width = 15
print(length * width)

# Type 2: User input with intermediate variable and default print
print("-------Type 2-------")
width = float(input("Enter the Width of a rectangle: "))
length = float(input("Enter the Length of a rectangle: "))
area = width * length
print("Area of the rectangle is:", area)

# Type 3: User input with inline calculation in print
print("-------Type 3-------")
width = float(input("Enter the Width of a rectangle: "))
length = float(input("Enter the Length of a rectangle: "))
print("Area of the rectangle is:", width * length)

# Type 4: User input with f-string formatting
print("-------Type 4-------")
width = float(input("Enter the Width of a rectangle: "))
length = float(input("Enter the Length of a rectangle: "))
area = width * length
print(f"Area of the rectangle is {area}")

# Type 5: BONUS — Include units in the result
print("-------Type 5: Bonus Version with Units-------")
width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))
unit = input("Enter the unit of measurement (e.g., cm, m, in): ")
area = width * length
print(f"The area of the rectangle is {area} {unit}²")

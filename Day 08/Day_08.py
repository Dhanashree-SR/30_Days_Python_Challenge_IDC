class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"🚗 Car: {self.brand} {self.model} ({self.year})")

# Ask user how many cars they want to enter
n = int(input("How many cars do you want to enter? "))

# List to store all car objects
cars = []
for i in range(n):
    print(f"\nEnter details for Car {i+1}:")
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    year = input("Enter year of manufacture: ")
    
    car = Car(brand, model, year)
    cars.append(car)
    
# Display all car details
print("\n✅ Car Details:")
for car in cars:
    car.display_info()

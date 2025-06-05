# Parent Class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"🚗 Car: {self.brand} {self.model} ({self.year})")

# Child Class (ElectricCar)
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        print(f"🔋 Electric Car: {self.brand} {self.model} ({self.year}) with {self.battery_capacity} kWh battery")

# Ask user how many cars they want to enter
n = int(input("How many electric cars do you want to enter? "))

# List to store all ElectricCar objects
electric_cars = []

for i in range(n):
    print(f"\nEnter details for Electric Car {i+1}:")
    brand = input("Enter car brand: ")
    model = input("Enter car model: ")
    year = input("Enter year of manufacture: ")
    battery = input("Enter battery capacity (in kWh): ")
    
    e_car = ElectricCar(brand, model, year, battery)
    electric_cars.append(e_car)
    
# Display all electric car details
print("\n✅ Electric Car Details:")
for car in electric_cars:
    car.display_info()

Inventory = {
    'Apple': 10,
    'Grapes': 20,
    'Pen': 20,
    'Pencil': 25
}

print("-------Welcome to Inventory-------\n")

while True:
    print("\nChoose an option:")
    print("1. View Items in Inventory")
    print("2. Add Item to Inventory")
    print("3. Update Item Quantity")
    print("4. Delete Item from Inventory")
    print("5. Check if Item Exists")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        print("\n📦 Inventory Items:")
        for item, qty in Inventory.items():
            print(f"- {item}: {qty}")

    elif choice == '2':
        item = input("Enter item name to add: ").capitalize()
        qty = int(input("Enter quantity: "))
        if item in Inventory:
            Inventory[item] += qty
            print(f"{item} already exists. Quantity updated to {Inventory[item]}")
        else:
            Inventory[item] = qty
            print(f"{item} added to inventory with quantity {qty}")

    elif choice == '3':
        item = input("Enter item name to update: ").capitalize()
        if item in Inventory:
            qty = int(input("Enter new quantity: "))
            Inventory[item] = qty
            print(f"{item} quantity updated to {qty}")
        else:
            print(f"{item} not found in inventory.")

    elif choice == '4':
        item = input("Enter item name to delete: ").capitalize()
        if item in Inventory:
            del Inventory[item]
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")

    elif choice == '5':
        item = input("Enter item name to check: ").capitalize()
        if item in Inventory:
            print(f"✅ Yes, {item} is in inventory with quantity {Inventory[item]}")
        else:
            print(f"❌ No, {item} is not in the inventory.")

    elif choice == '6':
        print("Exiting Inventory. Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

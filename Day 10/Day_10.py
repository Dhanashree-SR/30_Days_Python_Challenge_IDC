def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            valid_numbers = []
            for line in lines:
                try:
                    number = int(line.strip())
                    print(f"✅ Number: {number}")
                    valid_numbers.append(number)
                except ValueError:
                    print(f"❌ Not a valid number: '{line.strip()}'")

            print(f"\n🔢 Total valid numbers: {len(valid_numbers)}")

    except FileNotFoundError:
        print("⚠️ Error: File not found. Please check the filename.")

    except Exception as e:
        print(f"🚨 Unexpected error: {e}")

    finally:
        print("🔚 Program completed.")

# Run the function
read_numbers_from_file("numbers.txt")

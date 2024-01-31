x = input("Enter one Number: ")

# Check if x is a number before trying to format it
try:
    x = float(x)
    print(f"You entered the number: {x}")
except ValueError:
    print("Invalid input. Please enter a valid number.")


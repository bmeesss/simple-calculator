def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero"
    return a / b

def calculate_percentage(value, percentage):
    return (value * percentage) / 100


def main():
    print("Welcome to the calculator! (CTRL+C to quit)")
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        try:
            if choice == "5":
                value = float(input("Enter a number (e.g., 124): "))
                percentage = float(input("Enter a percentage (e.g., 32): "))
                result = calculate_percentage(value, percentage)
                print(f"{percentage}% of {value} = {result}")
            elif choice in ["1", "2", "3", "4"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)
                    print(f"Result: {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"Result: {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"Result: {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"Result: {result}")
            else:
                print("❌ Invalid choice. Please try again.")
        except ValueError:
            print("❌ Invalid input, please enter numbers only.")


if __name__ == "__main__":
    main()

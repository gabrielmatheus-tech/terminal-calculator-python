import os

# ==========================================
# 1. HELPER FUNCTIONS
# ==========================================

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(message):
    """Ensures the user types a valid float number, supporting commas."""
    while True:
        try:
            text_input = input(message)
            corrected_text = text_input.replace(',', '.')
            return float(corrected_text)
        except ValueError:
            print("❌ Error: Please enter a valid number!")

def save_to_file(result_text):
    """Saves the calculation result to a text file."""
    with open("calculator_history.txt", "a", encoding="utf-8") as file:
        file.write(result_text + "\n")

# Basic math functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: return "Error: Division by zero"
    return a / b

# ==========================================
# 2. CALCULATOR FUNCTION
# ==========================================

def calculator():
    clear_screen()
    line = "=" * 40
    print("      🧮 AVAILABLE OPERATIONS")
    print(line)
    print("1 - Addition (+)\n2 - Subtraction (-)\n3 - Multiplication (*)\n4 - Division (/)\n5 - Exit")
    print(line)

    choice = input("\nChoose an option (1-5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("\n❌ Invalid operation option!")
        return None
    elif choice == '5':
        print('\n👋 Exiting calculator...')
        return None

    print("\n" + line)
    n1 = get_number('Enter the first number: ')
    n2 = get_number('Enter the second number: ')

    if choice == '1':
        result = add(n1, n2)
        operation = "+"
    elif choice == '2':
        result = subtract(n1, n2)
        operation = "-"
    elif choice == '3':
        result = multiply(n1, n2)
        operation = "*"
    elif choice == '4':
        result = divide(n1, n2)
        operation = "/"
    
    # Formatting the final string
    result_text = f"{n1} {operation} {n2} = {result}"
    print(line)
    print(f"\n📊 Result: {result_text}")
    print('\n' + line)

    return result_text

# ==========================================
# 3. MAIN MENU
# ==========================================

history = []

# Load history on startup if the file exists
if os.path.exists("calculator_history.txt"):
    with open("calculator_history.txt", "r", encoding="utf-8") as file:
        for line in file:
            history.append(line.strip())

while True:
    clear_screen()
    line = "=" * 40
    print('\n' + line)
    print('          🏠 MAIN MENU')
    print(line)
    print('1 - New operation\n2 - View history\n3 - Clear history\n4 - Exit')
    print(line)

    menu_choice = input('\nChoose an option (1-4): ')

    if menu_choice == '1':
        final_result = calculator()
        if final_result is not None:
            history.append(final_result)
            save_to_file(final_result)
            input("\n✅ Operation finished and saved! Press Enter to return...")
        else:
            input("\n⚠️  Returning to main menu. Press Enter...")

    elif menu_choice == '2':
        if not history:
            print(line)
            print('\n⚠️ No operations performed yet.')
        else:
            clear_screen()
            print(line)
            print("\n📜 OPERATION HISTORY:")
            for index, item in enumerate(history, start=1):
                print(f"{index}) {item}")
        input("\n🔍 Press Enter to return to the menu...")

    elif menu_choice == '3':
        while True:
            print(line)
            confirm = input('\nDo you want to clear the history? (y/n): ').lower()
            if confirm == 'y':
                history.clear()

                # Clear the file content by opening in 'write' mode
                with open("calculator_history.txt", "w", encoding="utf-8") as file:
                    file.write("") 
                print(line)
                print('🗑️ History cleared!')
                break
            elif confirm == 'n':
                print('🛑 History kept.')
                break
            else:
                print("❌ Please answer only with 'y' or 'n'")
        input("\nPress Enter to continue...")

    elif menu_choice == '4':
        print('\n👋 Exiting... See you!')
        break

    else:
        print('\n❌ Invalid option in Main Menu!')
        input("Press Enter to try again...")
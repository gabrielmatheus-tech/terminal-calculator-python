# Import math operations from the core module
# These functions perform the actual calculations
from src.core import add, subtract, multiply, divide

# Import functions responsible for saving and loading history from files
from src.storage import load_history, save_operation, clear_history

# Import UI helper functions to keep the terminal interface clean and reusable
from src.ui import clear_screen, print_header, print_menu, pause, ask_choice, ask_number


# Decorative line used in prompts and separators
line = "=" * 40

# File where calculation history will be stored
HISTORY_FILE = "calculator_history.txt"


def main():
    """
    Main entry point of the calculator application.

    This function controls the program flow:
    - Loads the history from file
    - Displays the main menu
    - Executes user-selected operations
    - Saves results to history
    """

    # Load previously saved operations from file into memory
    history = load_history(HISTORY_FILE)

    # Main menu options displayed to the user
    menu_options = [
        "New Operation",
        "View History",
        "Clear History",
        "Exit"
    ]

    # Infinite loop keeps the calculator running until the user exits
    while True:

        # Clear terminal screen for a clean interface
        clear_screen()

        # Display the main menu header
        print_header("MAIN MENU")

        # Print all available menu options
        print_menu(menu_options)

        # Valid choices for the main menu
        valid_choices = ["1", "2", "3", "4"]

        # Ask user for a valid menu option
        choice = ask_choice(line + "\nChoose an option (1-4): ", valid_choices)

        # ---------------------------
        # OPTION 1: NEW CALCULATION
        # ---------------------------
        if choice == "1":

            # Clear screen before starting a new calculation
            clear_screen()

            # Display operation menu header
            print_header("AVAILABLE OPERATIONS")

            # List of available math operations
            operations = [
                "Addition (+)",
                "Subtraction (-)",
                "Multiplication (*)",
                "Division (/)"
            ]

            # Display operations to the user
            print_menu(operations)

            # Ask which math operation the user wants
            operation_choice = ask_choice(
                line + "\nChoose an operation (1-4): ",
                ["1", "2", "3", "4"]
            )

            # Ask user for the first number
            n1 = ask_number(line + "\nEnter the first number: ")

            # Ask user for the second number
            n2 = ask_number("Enter the second number: ")

            # Try executing the calculation
            # Division may raise a ZeroDivisionError
            try:

                # Determine which operation to execute
                if operation_choice == "1":
                    result = add(n1, n2)
                    operation_symbol = "+"

                elif operation_choice == "2":
                    result = subtract(n1, n2)
                    operation_symbol = "-"

                elif operation_choice == "3":
                    result = multiply(n1, n2)
                    operation_symbol = "*"

                elif operation_choice == "4":
                    result = divide(n1, n2)
                    operation_symbol = "/"

                # Create a formatted string describing the calculation
                result_text = f"{n1} {operation_symbol} {n2} = {result}"

                # Display result header
                print_header("📊 RESULT")

                # Print calculation result
                print(result_text)

                # Add result to in-memory history
                history.append(result_text)

                # Save result to file
                save_operation(HISTORY_FILE, result_text)

                # Pause before returning to menu
                pause(line + "\nPress Enter to return to the main menu...")

            # Handle division by zero error
            except ZeroDivisionError:

                # Print error message
                print(line)
                print("\n❌ Error: Division by zero is not allowed.")

                # Pause so user can read the message
                pause(line + "\nPress Enter to return to the main menu...")

        # ---------------------------
        # OPTION 2: VIEW HISTORY
        # ---------------------------
        elif choice == "2":

            # Clear screen for clean history display
            clear_screen()

            # Print history section header
            print_header("📜 OPERATION HISTORY")

            # If history list is empty
            if not history:
                print("\n⚠️ No operations performed yet.")

            # Otherwise display all saved operations
            else:
                for index, item in enumerate(history, start=1):
                    print(f"{index}) {item}")

            # Pause before returning to main menu
            pause(line + "\nPress Enter to return to the main menu...")

        # ---------------------------
        # OPTION 3: CLEAR HISTORY
        # ---------------------------
        elif choice == "3":

            # Clear screen for confirmation interface
            clear_screen()

            # Print clear history header
            print_header("🗑️ CLEAR HISTORY")

            # Ask the user to confirm deletion
            confirm = ask_choice(
                line + "\nDo you want to clear the history? (y/n): ",
                ["y", "n"]
            )

            # If user confirms
            if confirm == "y":

                # Clear history list in memory
                history.clear()

                # Clear history file on disk
                clear_history(HISTORY_FILE)

                print("\n✅ History cleared successfully.")

            # If user cancels
            else:
                print("\n⚠️ History was not cleared.")

            # Pause before returning to menu
            pause(line + "\nPress Enter to return to the main menu...")

        # ---------------------------
        # OPTION 4: EXIT PROGRAM
        # ---------------------------
        elif choice == "4":

            # Exit message
            print("\n👋 Exiting... See you!")

            # Break the infinite loop to end program
            break


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
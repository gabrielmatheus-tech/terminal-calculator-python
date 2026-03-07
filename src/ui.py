import os


def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title):
    """Print a centered header with decorative lines."""
    line = "=" * 40
    print("\n" + line)
    print(title.center(40))
    print(line)


def print_menu(options):
    """Print a numbered menu from a list of options."""
    for index, option in enumerate(options, start=1):
        print(f"{index} - {option}")


def pause(message="Press Enter to continue..."):
    """Pause the program until the user presses Enter."""
    input(f"\n{message}")


def ask_choice(prompt, valid_choices):
    """Ask the user for a valid menu choice."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("❌ Invalid option. Try again.")


def ask_number(message):
    """Ask the user for a valid number, supporting commas."""
    while True:
        try:
            text = input(message).strip().replace(",", ".")
            return float(text)
        except ValueError:
            print("❌ Error: Please enter a valid number.")
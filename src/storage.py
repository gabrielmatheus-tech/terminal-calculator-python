def load_history(path):
    """Load operation history from a text file."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            history = file.read().splitlines()
        return history
    except FileNotFoundError:
        return []

def save_operation(path, text):
    """Save a new operation to the history file."""
    with open(path, 'a', encoding='utf-8') as file:
        file.write(text + '\n') 

def clear_history(path):
    """Clear the operation history by overwriting the file."""
    with open(path, 'w', encoding='utf-8') as file:
        file.write('') # Write an empty string to clear the file
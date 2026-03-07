# 🧮 Python Calculator (Terminal Project)

A modular command-line calculator built with Python.
This project demonstrates clean code structure, error handling, file persistence, and automated testing using **pytest**.

---

## 🚀 Features

* Basic operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Operation history saved to file
* View and clear history
* Error handling (division by zero)
* Automated tests with **pytest**
* Modular architecture

---

## 📁 Project Structure

```
calculator/
│
├─ src/
│   ├─ core.py        # Math operations
│   ├─ storage.py     # File handling (history)
│   ├─ ui.py          # Terminal interface utilities
│   └─ main.py        # Main application logic
│
├─ tests/
│   └─ test_core.py   # Unit tests
│
├─ pytest.ini
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/python-calculator.git
```

Enter the project folder:

```
cd python-calculator
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install pytest
```

---

## ▶️ Running the calculator

Run the application with:

```
python -m src.main
```

---

## 🧪 Running tests

To run automated tests:

```
pytest
```

Expected result:

```
5 passed
```

---

## 🧠 Concepts Demonstrated

This project demonstrates several core Python development practices:

* Modular project structure
* Separation of concerns
* Exception handling
* File persistence
* Unit testing
* Clean CLI interface

---

## 📌 Future Improvements

Possible enhancements:

* Scientific calculator functions
* Timestamp for history entries
* Export history to CSV
* CLI arguments support (argparse / typer)
* GUI version (Tkinter or PyQt)

---

## 👨‍💻 Author

Gabriel Matheus

Learning Python and software development.

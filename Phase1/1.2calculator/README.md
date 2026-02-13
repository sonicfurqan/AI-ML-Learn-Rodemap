# 🎓 Learning Project: Simple Streamlit Calculator

This project is a functional calculator built with **Python** and **Streamlit**. It serves as a practical exploration of state management, user interface design, and mathematical expression parsing.

---

## 🧠 What This Project Teaches

Building a calculator is a rite of passage for developers. This specific project focuses on three core concepts:

### 1. Persistent State (`st.session_state`)
Streamlit apps are "stateless" by default—meaning they rerun the entire script every time you click a button. Without session state, the calculator would "forget" the numbers you typed.
* **Learning point:** How to store a running list of operations that survives script reruns.

### 2. Expression Parsing & RPN
The original logic uses a **Reverse Polish Notation (RPN)** style approach. 
* **The Process:** 1. **Normalize:** Take raw button clicks and turn them into a clean list using Regex (`re`).
    2. **Stack Logic:** Move operators and numbers into a specific order to handle math correctly.
    3. **Calculate:** Pop values from a stack to perform the arithmetic.



### 3. UI Execution Order
In Streamlit, the order of your code determines the order of the UI. This project demonstrates how to capture input at the top but display the final result (using `st.badge`) at the very bottom, even when using callback functions like `on_click`.

---

## 🛠️ The Tech Stack

| Feature | Tool | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Handles the buttons, columns, and badges. |
| **Logic** | Python Classes | Organizes the normalization and calculation code. |
| **Parsing** | Regex (`re`) | Splits strings into numbers and operators accurately. |

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/simple-calculator.git](https://github.com/your-username/simple-calculator.git)

 

---

## 📦 Project Tooling

We use **uv** for blazing-fast package management and **Ruff** for maintaining code quality.

### 1. UV (Package Manager)
| Task | Command |
| :--- | :--- |
| **Initialize Project** | `uv init calculator` |
| **Add Dependencies** | `uv add streamlit` |
| **Run Program** | `uv run main.py` |

### 2. Streamlit (UI Library)
To launch the web interface during development:
`python -m streamlit run main.py`

### 3. Ruff (Linter & Formatter)
Ruff replaces Flake8 and Black. It is written in Rust and is extremely fast.
* **Install:** `uv tool install ruff`
* **Check for errors:** `ruff check main.py`
* **Auto-fix issues:** `ruff check --fix main.py`
* **Watch mode (Real-time):** `ruff check --watch main.py`
* **Format code:** `ruff format main.py`

---

## 🐍 Python Fundamentals

### Type Annotation (Type Hinting)
Type hints make Python code more readable and allow tools like **Mypy** to catch bugs before the code runs.

#### 1. Function Annotations
```python
# Defining input types and the return type (->)
def add(num1: int, num2: int) -> int:
    return num1 + num2

# Simple Types
number: int = 10
decimal: float = 1.1
text: str = 'Gemini'
active: bool = False

# Complex Collections
names: list[str] = ['Alice', 'Bob']
coordinates: tuple[float, float] = (1.2, 3.5)
unique_ids: set[int] = {1, 2, 3}
user_data: dict[str, str] = {'Name': 'S'}

```

### Object-Oriented Programming (OOP)
The __init__ Method
The __init__ method is a constructor. It is automatically called when you create a new instance (object) of a class. It "initializes" the object's attributes.

```
class Calculate:
    def __init__(self, user_input: list):
        """
        This runs the moment 'Calculate(data)' is called.
        'self' refers to the specific object being created.
        """
        self.user_input = user_input
        self.result = 0
```

### The self Keyword
Definition: self represents the specific instance of the class.

Purpose: It allows methods within the class to access variables (attributes) and other methods associated with that specific object.
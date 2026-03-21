# 🐍 Python Programming Journey

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![Programs](https://img.shields.io/badge/Programs-68+-orange?style=for-the-badge)

> A structured collection of Python programs progressing from basic syntax to advanced data structures and Object-Oriented Programming (OOP).

---

## 📚 Table of Contents

- [About](#about)
- [Topics Covered](#topics-covered)
- [Program Index](#program-index)
- [Concepts Learned](#concepts-learned)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)

---

## About

This repository documents a step-by-step Python learning journey. Each program (`program930.py` to `program997.py`) builds upon the previous one, gradually introducing new concepts — from printing output and defining functions, to implementing full-blown data structures using OOP.

---

## Topics Covered

| # | Topic | Programs |
|---|-------|----------|
| 1 | Basic Output & Hello World | 930 |
| 2 | Functions — Definition & Calling | 931 – 933 |
| 3 | User Input & Type Conversion | 934 – 936 |
| 4 | Functions with Parameters & Return Values | 937 – 938 |
| 5 | Conditional Statements (`if`/`else`) | 939 |
| 6 | `range()` and `for` Loops | 940 – 943 |
| 7 | `while` Loop | 944 |
| 8 | Even/Odd Check | 945 |
| 9 | Factors of a Number | 946 – 947 |
| 10 | Sum of Factors | 948 |
| 11 | Perfect Number Check | 949 |
| 12 | `del` Keyword & Memory Management | 993 – 994 |
| 13 | Arrays (Lists) with OOP (`ArrayX` class) | 994 – 995 |
| 14 | Singly Linear Linked List (OOP) | 991 – 992, 996 – 997 |

---

## Program Index

### 🔰 Basics (930–933)
| File | Description |
|------|-------------|
| `program930.py` | First Python program — basic `print()` output |
| `program931.py` | Defining and calling a simple `Display()` function |
| `program932.py` | Introducing `main()` function — no explicit call |
| `program933.py` | `main()` function with explicit call |

### ➕ Input & Arithmetic (934–938)
| File | Description |
|------|-------------|
| `program934.py` | Addition using `input()` — string concatenation bug demo |
| `program935.py` | Fixed addition using `int(input())` |
| `program936.py` | Addition inside `main()` function |
| `program937.py` | Addition via separate `Addition(A, B)` function with return |
| `program938.py` | Generic `Addition()` — works with int, float, and strings |

### 🔀 Conditionals & Loops (939–944)
| File | Description |
|------|-------------|
| `program939.py` | Find maximum of two numbers using `if/else` |
| `program940.py` | Exploring `range()` — basic and stepped |
| `program941.py` | Assigning `range()` to a variable |
| `program942.py` | `for` loop printing numbers 0–9 |
| `program943.py` | `for` loop printing a message 5 times |
| `program944.py` | `while` loop printing a message 5 times |

### 🔢 Number Problems (945–949)
| File | Description |
|------|-------------|
| `program945.py` | Check if a number is Even or Odd |
| `program946.py` | Display all factors of a number |
| `program947.py` | Optimized factor display (loop up to `N/2`) |
| `program948.py` | Sum of factors of a number |
| `program949.py` | Perfect number check (sum of factors == number) |

### 🗃️ Arrays & Memory (993–995)
| File | Description |
|------|-------------|
| `program993.py` | Demo of `del` keyword — variable deletion |
| `program994.py` | Dynamic array creation using `[0] * size` and `del` |
| `program995.py` | `ArrayX` class — OOP array with `Accept()`, `Display()`, `Summation()` |

### 🔗 Singly Linear Linked List — OOP (991–992, 996–997)
| File | Description |
|------|-------------|
| `program991.py` | `Node` + `SinglyLL` class — `InsertFirst`, `InsertLast`, `InsertAtPos`, `Display`, `Count` |
| `program992.py` | Added `DeleteFirst()` method |
| `program996.py` | Added `DeleteLast()` method |
| `program997.py` | Completed — `DeleteAtPos(pos)` method added |

---

## Concepts Learned

```
✔ print(), input(), int(), type conversion
✔ Functions — defining, calling, parameters, return values
✔ Generic functions (duck typing)
✔ if / else conditionals
✔ for loop with range()
✔ while loop
✔ Mathematical logic — factors, perfect numbers
✔ del keyword and memory management
✔ Lists as dynamic arrays
✔ Object-Oriented Programming (OOP)
    └── Classes & Objects
    └── __init__ constructor
    └── Instance methods
    └── if __name__ == "__main__" guard
✔ Data Structures
    └── Array (OOP)
    └── Singly Linear Linked List (OOP)
        └── InsertFirst / InsertLast / InsertAtPos
        └── DeleteFirst / DeleteLast / DeleteAtPos
        └── Display / Count
```

---

## How to Run

Make sure Python 3.x is installed, then:

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Run any program
python program930.py
python program997.py
```

---

## Tech Stack

- **Language:** Python 3.x
- **Paradigms:** Procedural & Object-Oriented Programming
- **IDE:** Any — VS Code, PyCharm, IDLE, etc.

---

> 🙏 *Jay Ganesh..* — as every program begins, so does this journey.

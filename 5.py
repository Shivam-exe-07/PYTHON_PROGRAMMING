def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        expr = input("Enter expression (e.g. 6 + 9): ").strip()
        if expr.lower() == 'quit':
            print("Goodbye!")
            break

        for op in ['+', '-', '*', '/']:
            if op in expr:
                try:
                    parts = expr.split(op, 1)
                    a, b = float(parts[0].strip()), float(parts[1].strip())
                    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
                    result = ops[op](a, b)
                    print(f"Result: {result}\n")
                except ValueError as e:
                    print(f"Error: {e}\n")
                except Exception:
                    print("Invalid input. Try again.\n")
                break
        else:
            print("Invalid expression. Use format: number operator number\n")

if __name__ == "__main__":
    main()
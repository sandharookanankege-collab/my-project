# bonus.py

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b


# Example usage
print("Multiply:", multiply(4, 5))
print("Divide:", divide(10, 2))
print("Power:", power(2, 3))

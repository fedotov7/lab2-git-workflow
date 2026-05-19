def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b

def divide(a, b):
    """Divide a by b.
    
    Args:
        a (float): Numerator
        b (float): Denominator
    
    Returns:
        float: Result of division
    
    Raises:
        ValueError: If denominator is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def demo_calculator():
    """Demonstrate calculator functions."""
    print("Simple Calculator")
    print(f"2 + 3 = {add(2, 3)}  # BASE")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")

if __name__ == "__main__":
    demo_calculator()
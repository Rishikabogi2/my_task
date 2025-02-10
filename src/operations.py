async def add(a: float, b: float) -> float:
    """
    Adds two numbers.
    
    Args:
      a: The first number.
      b: The second number.
    
    Returns:
      The sum of a and b.
    """
    return a + b

async def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.
    
    Args:
      a: The first number.
      b: The second number.
    
    Returns:
      The difference of a and b.
    """
    return a - b

async def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.
    
    Args:
      a: The first number.
      b: The second number.
    
    Returns:
      The product of a and b.
    """
    return a * b

async def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second.
    
    Args:
      a: The first number.
      b: The second number.
    
    Returns:
      The quotient of a and b.
    
    Raises:
      ZeroDivisionError: If the second number is 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

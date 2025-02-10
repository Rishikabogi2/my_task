import asyncio
from src.operations import add, subtract, multiply, divide

async def calculate(num1: float, num2: float, operator: str) -> float:
    """
    Perform calculation based on the operator provided.

    Args:
        num1: The first number for the operation.
        num2: The second number for the operation.
        operator: The operator (+, -, *, /).

    Returns:
        The result of the operation.
    """
    if operator == "+":
        return await add(num1, num2)
    elif operator == "-":
        return await subtract(num1, num2)
    elif operator == "*":
        return await multiply(num1, num2)
    elif operator == "/":
        return await divide(num1, num2)
    else:
        raise ValueError("Invalid operator")

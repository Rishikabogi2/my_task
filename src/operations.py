async def add(a: float, b: float) -> float:
    return a + b

async def subtract(a: float, b: float) -> float:
    return a - b

async def multiply(a: float, b: float) -> float:
    return a * b

async def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


async def calculate(num1: float, num2: float, operator: str) -> float:
    from src.operations import add, subtract, multiply, divide

    if operator == '+':
        return await add(num1, num2)
    elif operator == '-':
        return await subtract(num1, num2)
    elif operator == '*':
        return await multiply(num1, num2)
    elif operator == '/':
        return await divide(num1, num2)
    else:
        raise ValueError("Invalid operator")


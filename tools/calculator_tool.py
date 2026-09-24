from crewai.tools import tool


@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Calculate basic mathematical expressions.
    Example: 25 * 4
    """
    try:
        allowed_characters = "0123456789+-*/().% "

        if not all(char in allowed_characters for char in expression):
            return "Error: Only basic mathematical expressions are allowed."

        result = eval(expression, {"__builtins__": {}}, {})
        return f"Result: {result}"

    except Exception as e:
        return f"Calculation error: {str(e)}"

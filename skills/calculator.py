SKILL_NAME = "Calculator"

KEYWORDS = [
    "calculate",
    "plus",
    "minus",
    "multiply",
    "divide"
]

def handle(command):

    command = command.lower()

    if not command.startswith("calculate"):
        return None

    expression = command.replace("calculate", "").strip()
    expression = (
        expression
        .replace("x", "*")
        .replace("×", "*")
        .replace("plus", "+")
        .replace("minus", "-")
        .replace("into", "*")
        .replace("divide", "/")
    )

    try:
        result = eval(expression)

        return f"The answer is {result}."

    except:

        return "I couldn't calculate that."
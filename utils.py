def greet(name):
    """
    Return a greeting message for the given name.
    """
    return f"Hello, {name}!"


def flip(input_string):
    """
    Reverse the characters in the given string.
    """
    return input_string[::-1]


def count_letters(input_string, letter):
    """
    Count how many times a specific letter appears in a string.
    """
    count = 0
    for char in input_string:
        if char == letter:
            count += 1
    return count


if __name__ == "__main__":
    print("This file is being run directly.")
# FREEZE CODE END


# ----------------------
# PARTE I - V (AGREGADO)
# ----------------------

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2


def exponent(base, exp):
    return base ** exp


def modulo(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    return num1 % num2


def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2


def absolute(num):
    return abs(num)

"""
Ask 2 numbers as input, sum them, print result.
"""

def addition(a, b):
    return a + b


def ask_for_number(text):
    while True:
        num = input(text)
        try:
            num = int(num)
            break
        except ValueError:
            print("try again")
    return num


a = ask_for_number("give me a number: ")
b = ask_for_number("give me another number: ")
result = addition(a, b)
print(f"result is {result}")

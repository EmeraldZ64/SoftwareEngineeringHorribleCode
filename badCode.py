# YAGNI
history_log = []  # YAGNI: code is there but functionality to save this is not implemented

# Single responsibility violation; no reason to make this a function, it is only called once
def process_calculate_print(num1, oper, num2):
    if oper == "+":
        result = int(num1) + int(num2)
    elif oper == "-":
        result = int(num1) - int(num2)
    elif oper == "*":
        result = int(num1) * int(num2)
    elif oper == "/":
        result = float(num1) / float(num2)

    print(result)
    history_log.append(result)


def main():
    calculation_string = input("Enter an operation with single digits (Ex. 2 ( +, -, *, / ) 4): ")

    # Violation of DRY code (Don't repeat yourself), also KISS (better ways to do this)
    for char in calculation_string[0]:
        if char in "0123456789":
            first_num = calculation_string[0]

    for char in calculation_string:
        if char in "+-*/":
            operand = calculation_string[1]

    for char in calculation_string[2]:
        if char in "0123456789":
            second_num = calculation_string[2]

    process_calculate_print(first_num, operand, second_num)


if __name__ == "__main__":
    main()
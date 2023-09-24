def operManager(math_oper):
    while True:
        if math_oper in ('+', '-', '*', '/'):
            break
        else:
            print("Error: Please enter only one of the following characters: +, -, *, /")
            math_oper = input("Enter a mathematical operation (+, -, *, /): ")
    return math_oper

while True:
    math_oper = input("Enter a mathematical operation (+, -, *, /): ")
    NumberOne = int(input("Enter the first number: "))
    NumberTwo = int(input("Enter the second number: "))
    
    math_oper = operManager(math_oper)
    
    if math_oper == "+":
        result = NumberOne + NumberTwo
    elif math_oper == "-":
        result = NumberOne - NumberTwo
    elif math_oper == "*":
        result = NumberOne * NumberTwo
    elif math_oper == "/":
        if NumberTwo == 0:
            print("Error: Division by zero")
        else:
            result = NumberOne / NumberTwo
    else:
        print("Invalid mathematical operation")
        continue

    print(f"Result: {result}")

    more_questions = input("Do you want to perform another calculation? (y/n): ")
    if more_questions.lower() == "n":
        break
    elif more_questions.lower() == "y":
        continue
    else:
        print("Incorrect answer. Enter 'y' or 'n'.")

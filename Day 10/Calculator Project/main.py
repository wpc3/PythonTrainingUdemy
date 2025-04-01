import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

calc_dictionary = {}

calc_dictionary["+"] = add
calc_dictionary["-"] = subtraction
calc_dictionary["*"] = multiplication
calc_dictionary["/"] = division

# print(calc_dictionary["*"](4,8))

calc_on = True

while calc_on:
    first_num = int(input("What is the first number?: "))

    print(" + \n - \n * \n /")

    first_operation_input = input("Pick an operation: ")

    second_num = int(input("What is the second number?: "))
    result = 0


    if first_operation_input == "+":
        result += calc_dictionary["+"](first_num,second_num)
        print(result)
    elif first_operation_input == "-":
        result += calc_dictionary["-"](first_num,second_num)
        print(result)
    elif first_operation_input == "*":
        result += calc_dictionary["*"](first_num, second_num)
        print(result)
    elif first_operation_input == "/":
        result += calc_dictionary["/"](first_num,second_num)
        print(result)

    keep_calculating = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()
    while keep_calculating == "y":
        print(" + \n - \n * \n /")
        second_operation = input("Pick an operation: ")
        new_num = int(input("What is the second number?: "))
        if second_operation == "+":
            result = calc_dictionary["+"](result, new_num)
            print(result)
        elif second_operation == "-":
            result = calc_dictionary["-"](result, new_num)
            print(result)
        elif second_operation == "*":
            result = calc_dictionary["*"](result, new_num)
            print(result)
        elif second_operation == "/":
            result = calc_dictionary["/"](result, new_num)
            print(result)
        keep_calculating = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()
    if keep_calculating == "n":
        result = 0


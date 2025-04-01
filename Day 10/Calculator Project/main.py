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
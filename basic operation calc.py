
def calculator(num_1, op, num_2):
    result = 0

    if op == "+":
        result = num_1 + num_2
    elif op == "-":
        result = num_1 - num_2
    elif op == "*":
        result = num_1 * num_2
    elif op == "/":
        result = num_1 / num_2
        
    print(f"{float(num_1)} {op} {float(num_2)} = {float(result)}")
    
print("This is a basic operation calculator.")
print("Type in the first number, the operation sign, and then the second number.")
first_variable  = float(input("First #: "))
op = input("Operation sign: ")
second_variable = float(input("Second #: "))

calculator(first_variable, op, second_variable)       
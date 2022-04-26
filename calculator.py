def calculator(num_1, num_2, op):
    result = 0

    if op == "+":
        result = num_1 + num_2
    elif op == "-":
        result = num_1 - num_2
    elif op == "*":
        result = num_1 * num_2
    elif op == "/":
        result == num_1 / num_2

    return result

print(calculator(5, 10, "+"))
    



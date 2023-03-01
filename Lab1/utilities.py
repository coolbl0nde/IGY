def print_hello():
    print('Hello world')

def calculation(first_number, second_number, operation):

    if operation == "add":
        return first_number + second_number
    elif operation == "sub":
        return first_number - second_number
    elif operation == "mult":
        return first_number * second_number
    elif operation == "div":
        return first_number / second_number
    else:
        print("Incorrect operation!")

        
def error_massage():
    print("Incorrect Data! Enter a number!")


def ask_list_length():
    while True:
        try:
            list_length = int(input("Enter list length: "))
            return list_length
        except ValueError:
            print(error_massage())


def ask_start_range():
    while True:
        try:
            start_range = int(input("Enter start of range for generate random list: "))
            return start_range
        except ValueError:
            print(error_massage())


def ask_end_range():
    while True:
        try:
            end_range = int(input("Enter end of range for generate random list: "))
            return end_range
        except ValueError:
            print(error_massage())

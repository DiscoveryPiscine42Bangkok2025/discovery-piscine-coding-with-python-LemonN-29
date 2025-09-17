number_str = input("Give me a number: ")
number = float(number_str)
if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
result = a * b
print(f"{a} x {b} = {result}")

if result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is negative.")

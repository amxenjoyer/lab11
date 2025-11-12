# calculator program

z = input("Enter the operation: ")
a = float(input("Enter the first operand: "))
b = float(input("Enter the second operand: "))

if z == "add":
    result = a + b
elif z == "sub":
    result = a - b
elif z == "mul":
    result = a * b
elif z == "div":
    result = a / b
else:
    result = 'Error'

print(f"Result is {round(result,2)}")

a = float(input("Enter first value : "))
b = float(input("Enter second value : "))
print("\n Select Operations")
print("1. for Add")
print("2. for Subtraction")
print("3. for Multiplication")
print("4. for Division")
print("5. for Remainder")
print("6. for Floor Division")
print("7. for Power")

op = input("Enter any number as per operations : ")
if op == '1':
    result = a + b
    print("Sum of a and b is", result)
if op == '2':
    result = a - b
    print("Subtraction of a and b is", result)
if op == '3':
    result = a * b
    print("Multiplication of a and b is", result)
if op == '4':
    result = a / b
    print("Division of a and b is", result)
if op == '5':
    result = a % b
    print("Remainder of a and b is", result)
if op == '6':
    result = a // b
    print("Floor division of a and b is", result)
if op == '7':
    result = a ** b
    print("Power of a to b is", result)

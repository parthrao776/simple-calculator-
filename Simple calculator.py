print("Using Conditonal statement for arithmetic operations")
a = int(input("Enter first no.: "))
b = int(input("Enter Second no.: "))
print("1 = Addition [+]")
print("2 = subtraction [-]")
print("3 = Multiplication [*]")
print("4 = Division [/]")
print("5 = Modulo [%]")
x = int(input("Enter the Number as per given operator: "))
if x == 1:
    print(a + b)
elif x == 2:
    print(a - b)
elif x == 3:
    print(a * b)
elif x == 4:
    print(a / b)
elif x == 5:
    print(a % b)
else:
    print("Given input is invalid")
    


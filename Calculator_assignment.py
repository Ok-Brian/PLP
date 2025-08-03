num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero")
        exit()
else:
    print("Invalid operation")
    exit()

print("Result:", result) #The result of the operation

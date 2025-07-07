# Menu
print("Welcome!")
print("Introduce one of the following options typing its corresponding number :)")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Choose option
option = int(input("Choose an option: "))

if option not in [1, 2, 3, 4]:
    print("Not valid")
else:
    num1 = float(input("Introduce the first number: "))
    num2 = float(input("Introduce the second number: "))

    if option == 1:
        print("Result: ", num1 + num2)
    elif option == 2:
        print("Result: ", num1 - num2)
    elif option == 3:
        print("Result: ", num1 * num2)
    elif option == 4:
        if num2 == 0:
            print("You cannot divide by zero!")
        else:
            print("Result: ", num1 / num2)

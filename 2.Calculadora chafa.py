    #menu
print("Welcome!")
print("Introduce one of the following options typing its corresponding number :)")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

    #choose number
option = int(input("Choose an option: "))
num1 = float(input("Introduce the first number: "))
num2 = float(input("Introduce the second number: "))

if option == 1:
     print("Result: ", num1 + num2)
elif option == 2:
     print("result: ", num1 - num2)
elif option == 3:
    print("Result: ", num1 * num2)
elif option == 4:
    print("Result: ", num1 / num2)
else:
     print("Not valid")

print("welcome to the primitive calculator")
x = int(input("choose your first number: "))
y = int(input("choose your second number: "))

operation = input("choose the operation (addition, subtraction, multiplication or division): ")

# if the user enters an invalid string ask him again


if operation == 'addition':
    result = x+y
    print(str(x) + " + " + str(y) + " = " + str(result))
    
elif operation == 'subtraction':
    result = x-y
    print(str(x) + " - " + str(y) + " = " + str(result))
    
elif operation == 'multiplication':
    result = x*y
    print(str(x) + " * " + str(y) + " = " + str(result))

elif operation == 'division':
    if y==0:
        print("Sorry, we cannot do the operation, we cannot divide by 0")
    else:
        result = x/y
        print(str(x) + " / " + str(y) + " = " + str(result))
    


#Simple Calculator

#Init
#functions
def add(num1, num2): #Function for addition
    result = num1 + num2
    print(result)

def sub(num1, num2): #Function for subtract
    result = num1 - num2
    print(result)

def mul(num1, num2): #Function for multiplication
    result = num1 * num2
    print(result)

def div(num1,num2): #Function for divide
    result = num1/num2
    print(result)


def calc():
    print("Welcome to Simple Calculator")
while True:
    print("Please choose an operation")
    print("""1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Quit""")

    option = int(input("1-5:"))
    if option == 1:  #You pick the numbers you need to add
        num1 = int(input("Please enter the first number"))
        num2 = int(input("Please enter the second number"))
        add(num1,num2)

    if option == 2:  #You pick the number to subtract
        num1 = int(input("Please enter the first number"))
        num2 = int(input("Please enter the second number"))
        sub(num1,num2)

    if option == 3:  #You pick the numbers to multiply
        num1 = int(input("Please enter the first number"))
        num2 = int(input("Please enter the second number"))
        mul(num1,num2)

    if option == 4: #You pick the numbers you need to divide
        num1 = int(input("Please enter the first number"))
        num2 = int(input("Please enter the second number"))
        div(num1,num2)

    if option == 5:
        print("bye bye")
    break
#main
calc()

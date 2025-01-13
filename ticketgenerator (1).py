price = 100
global price
def draw_ticket(name, age, dayofweek, coupon): #Tell the computer your name, age, dayofweek, and it will tell you your price
    t.goto(-50, 0)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    #Prices according to your age and day of week
    t.goto(50, 215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, 215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, 135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(10, 5)
    t.write(age, font=("Arial", 15), align="right")
    price = "$100"
    t.goto(50,5)
    t.write(price, font=("Arial", 15), align="right")

#Main
#1
print("Welcome to David's exotic wonderland!")
#2
#Your information/inputs
name = input("Please enter your name: ")
age = input("Please enter your age: ")
day = input("What is today's day? ")
coupon = input("Do you possibly have a coupon code?")

#3

#This is a code that defines your price from ages 0-18
if age > 3 and age < 18 and day == ("monday","tuesday","wednesday","thursday","friday"):
    if age <= 3:
        price = 0
    elif age > 3 and age < 18:
        price = 50
if age > 18 :
    price = 100


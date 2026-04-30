print("hello word, this is my GitHub File")
name = input("What's your name ")
print(f" Hello, {name}")
#======================================================

#conditionals - age category system 

age = int(input("Input age = "))

if age <13:
    print("Child")
elif age <=19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

#======================================================

#number range checker

size = int(input("What's your size ="))

if size <= 10:
    print("Small")
elif size <= 100:
    print("Medium")
elif size >100:
    print("Large")
else:
    print("Invalid")

#==========================================================

#Day of the week

day = int(input("Put in a number = "))

match day:

 case 1:
    print("Monday")
 case 2:
    print("Tuesday")
 case 3:
    print("Wednesday")
 case 4:
    print("Thursday")
 case 5:
    print("Friday")
 case 6:
    print("Saturday")
 case 7:
    print("Sunday")
 case _:
    print("Invalid")

#====================================================================

#simple ATM withdrawal

balance = 1000

withdrawal = int(input("put in mount you want to withdraw -> "))

if withdrawal > balance:
    print("insufficient funds available")
    if withdrawal <=0:
        print("Inavalid amount")
else:
    print(f"Remaining balance = {balance - withdrawal}")

#=====================================================================

#shipping cost calculator

Country_region = input("put in country or region here -> ")

match Country_region:

    case "UK":
     cost = 5
    case "USA":
     cost = 7
    case "EU":
     cost = 9
    case _:
     cost = 20

print(f"£{cost}")

#======================================================================



     

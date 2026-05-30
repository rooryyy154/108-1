x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

if x > 5: print("x is greater than 5")

print("Even") if x % 2 == 0 else print("odd")

# nested
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

age = 18

if age >= 18 and age <= 21:
    print("You are between 18 and 21 years old")

"""
MINI CHALLENGE
"""
age = int(input("Please share me your age: "))
has_id = input("Do you have a valid ID?(yes/no): ")
if age >0:
    if age >= 21 and has_id == "yes":
        print("Access Granted")
    elif age >= 21 and has_id == "no":
        print("Acces Denied - ID requiered")
    elif age >= 18 and age <= 20:
        print("Acces Limited")
    else:
        print("Acces Denied - Too Young")
else:
    print("Invalid age entered")

can_enter = age>= 21 and has_id == "yes"
if can_enter:
    print("¡Welcome inside!")
else:
    print("Please see the front desk")


print("Hello World from Python!")
print(2)
print(5+3)
print(True)

name = "Angela"
age = 28
middle_name = "John"
last_name = "Scott"
print(name,age)
print("My anme is "+ name + "" + middle_name + "" + last_name + "and I am" + str(age))

main_character = "Jim"
side_character = "Roy"
days = 32
country = "France"
river = "Seine"

print(f"{main_character} and {side_character} had been walking in the countryside of {country} for about {days} days, they were hopeless until they saw saw the {river} and both drank fresh water")

print(f"""Hi
      {main_character}
    """)

print(type(country))
print(type(days))
print(type(True))

print(20 + int("20"))
print(20 + age)
print(20 + 2.98)

#user_name = input("Enter your username: ")
#print(f"Hello, {user_name}")

print("Welcome to Mama Mia Pizza, please fill the next blank spaces:")
pizza = int(input("How many slices do you want in your pizza? "))
people = int(input("How many people are in your group? "))
slices = float(pizza/people)
print(f"Each one would get {slices} ")
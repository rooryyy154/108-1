my_list = [10, 20, 30, 40, 50]
print(my_list)

mixed_list = [1, "apple", 3.5, True]
print(mixed_list)

fruits = ["apple","banana","cherry"]
print(fruits[0])
print(fruits[2])

print(fruits[-1])

fruits[1] = "mango"
print(fruits)

fruits.append("orange")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

for fruit in fruits:
    print(fruit)

if "mango" in fruits:
    print("Yes, mango is in the list")
else:
    print("No, mango is not in the list")

print(len(fruits))

# ==================
movies_list = ["Lalaland","Parasites","Superman","Project Hail Mary"]
print(movies_list)

movies_list.insert(1,"Alien:Romulus")
print(movies_list)

movies_list.remove(movies_list[3])

for movie in movies_list:
    print(movie)

print(len(movies_list))

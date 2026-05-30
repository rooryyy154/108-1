# Dictionaries store data in KEY: VALUE pairs
# created using {}

student = {
    "name":"Arturo",
    "age": 24,
    "major": "Computer"
}

print(student)

#adding items
print(student["name"])
print(student.get("major"))

# adding at the last of the dictionary
student["graduation_year"] = 2025
print(student)

#change values
student["age"] = 20
print(student)

#removing items
student.pop("major")
print(student)

#check if a key exists
if "name" in student:
    print("Key 'name' exists in the dictionary!")

#nested dictionary
students = {
    "student1": {"name": "Arturo", "age": 22},
    "student2": {"name": "Ram", "age": 21}
}

print(students["student1"]["age"])

"""
mini challenge
"""

player = {
    "username": "Arturo",
    "level": 20,
    "stats": {
        "health": 10,
        "attack": 5
    }
}
print(player["username"])
print(player["level"])

player["level"] = player["level"] + 1
player["gold"] = 500

if player["stats"]["attack"] >= 30:
    print("Strong player!")
else:
    print("Needs more training!")

player["stats"].pop("health")
print(player)
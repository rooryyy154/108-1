#Tuples
my_tuple = ("apple","banana","cherry")
print(my_tuple)

# access items
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1])

#check if item exists
if "banana" in my_tuple:
    print("Yes, banana is in the tuple")

print(len(my_tuple))

#single item tuples
single = ("water",)
print(type(single))

# nested tuples
tuple1 = ("A","B","C")
tuple2 = (1, 2, 3)
combine = (tuple1, tuple2)
print(combine)

"""
mini challenge
"""
quiz_scores = (11,71,92,84,76,73)
print(quiz_scores[0:3])
print(quiz_scores[3:6])

print(max(quiz_scores))
print(min(quiz_scores))

if any(score < 70 for score in quiz_scores):
    print("Warning: At least one failling score!")
else:
    print("All students passed")

bonus_scores = tuple(score + 5 for score in quiz_scores)

final_scores = (quiz_scores + bonus_scores)
print(final_scores)
print(final_scores[-1])


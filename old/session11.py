# person = ("ali", 14, "tehran")
# print(person[0])
# for x in person:
#     print(x)

# favorite_sport = [
#     ["ali", "football"], ["reza","baseball"]
# ]
# print(favorite_sport[0][0], "likes", favorite_sport[0][1])
# print(favorite_sport[1][0], "likes", favorite_sport[1][1])

# favorite_sport = {
#     "ali" : ["football", "tennis"], 
#     "reza" :"baseball",
#     "sara" : "tennis"
# }

# print("ali likes",favorite_sport["ali"])
# print("reza likes",favorite_sport["reza"])
# print("sara likes",favorite_sport["sara"])

# favorite_sport["matin"] = "football"
# favorite_sport["ali"] = "tennis"
# del favorite_sport["reza"]
# print(favorite_sport)

# student = {
#     "name" : "nikan",
#     "age" : 13,
#     "grade" : 19.5
# }

# for key, val in student.items():
#     print(key, val)

# print(student["name"])
# print(student.get("name"))
# print(student["age"])
# print(student.get("age"))
# print(student["grade"])
# print(student.get("grade"))


# numbers = {1,2,3,4,5,1,2,3,6,7,1}
# numbers.add(100)
# numbers.remove(3)
# print(numbers)

# names = ["sara", "matin", "sara"]
# names = set(names)
# print(len(names))

# if "sara" in names:
#     print("yes")

import turtle
turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("darkgreen")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.done()
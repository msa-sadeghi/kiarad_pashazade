# name = input("enter a name:  ")
# # print(len(name))

# c = 0
# for ch in name:
#     c += 1
# print(c)

# for i in range(3):
#     x = int(input("enter a number: "))
#     if x > 0:
#         print(f"{x} is positive")
#     elif x < 0:
#         print(f"{x} is negative")
#     else:
#         print("zero")


# x = int(input("enter a negative number: "))
# s = 0
# for i in range(x, 0):
#     s += i

# print(s)



# x = int(input("enter a number: "))

# if x >= 10 and x <= 50:
#     print("ok")
# else:
#     print("not ok")


# for i in range(1,6):
#     print("*" * i)


# s = 0
# for i in range(2):
#     x = int(input("enter a number: "))
#     s += x
# print(s)

# for i in range(2):
#     x = int(input("enter a number: "))
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# secret = 12

# for i in range(3):
#     n = int(input("enter a number: "))
#     if n == secret:
#         print("success")
#         break
#     else:
#         print("incorrect")


# numbers = [1,2,3]
# print(len(numbers))
# for n in numbers:
#     print(n)

# for n in range(3, 21):
#     print(f"multiplies of {n}:")
#     multiplies = []
#     for i in range(1, 101):
#         if i % n == 0:
#             multiplies.append(i)
    
#     print(multiplies)


# name = "nikan"

# for x in range(len(name)):
#     print(x, name[x])
# # for x in name:
# #     print(x)

# for i, val in enumerate(name):
#     print(i, val)


# names = ["ali", "sara", "nima"]
# print(names[0])
# names.append("armin")
# names.remove("sara")
# names.sort(reverse=True)
# print(names)

# numbers = []
# numbers.append(1)
# numbers.append(11)
# numbers.append(4)
# numbers.sort(reverse=True)
# numbers.remove(4)
# print(numbers)

# text = "hello python"
# text = text.replace("o", "0")
# for x in text:
#     print(x.upper(), end=" ")

# notes = []

# for i in range(3):
#     n = input("enter a note: ")
#     notes.append(n)

# print("your notes: ")

# for n in notes:
#     print("-", n)


# string = "sara"
# print(len(string))

# numbers = [1,2,3,4,5,6]
# print(len(numbers))

# names = ["amir", "sara"]

# new_name = input("enter the name: ")
# names.append(new_name)

# names.remove("sara")

# print(names)

# names = []
# print(names)



# text = "hello,from,python"
# words = text.split(",")
# print(words)

# words = []
# start_index = 0
# end_index = 0
# for ch in text:
#     if ch == ",":
#         words.append(text[start_index:end_index])
#         start_index = end_index + 1
#     end_index += 1
# else:
#     words.append(text[start_index:])

# print(words)

# string = "salaam khobi"

# count = 0
# for ch in string:
#     count += 1 

# print(count)

# numbers = [1, 2,3]
# names = ["sara", "matin","mehrzad"]
# for i in range(len(numbers)):
#     print(numbers[i], names[i])


# string = "salaam khobi"
# chars = []
# for ch in string:
#     if ch != " ":
#         chars.append(ch)
# print(chars)

string = "salaam python khobi python"
# print(string.count("python"))

count = 0
words = string.split()
for w in words:
    if w == "python":
        count += 1
print(count)
# name = "sara"

# for x in name:
#     print(x)

# number =  int(input("enter a number: "))
# s = 0
# for x in range(1, 6):
#     # s = s + x
#     s += x
# print(s)



# for i in range(10, 0, -1):
#     print(i)

# name = "nikan"
# for i in range(4, -1, -1):
#     print(name[i])



# for i in range(5):
#     x = int(input(f"enter number{i + 1}: "))
#     print(f"number {i + 1} is : {x}")


# for i in range(10):
#     print("hi")

# total = 0

# for i in range(1,18, 2):
#     # total = total + i
#     total += i

# print(total)

# x = int(input("enter a number: "))
# for i in range(1, 10):
#     print(x  * i, end="\t")

# total = 0
# number = input("enter a number: ")
# for x in number:
#     total += int(x)

# print(total)


# x = int(input("enter a number: "))

# for i in range(2, x):
#     if x % i == 0:
#         print("is not prime")
#         break
# else:
#     print("is prime")



# maximum = int(input("enter a number: "))
# for i in range(4):
#     n = int(input("enter a number: "))
#     if n > maximum:
#         maximum = n
# print("maximum is: ", maximum)

# print(max(1,2,3,4,5,7,6))

positive_count = 0
negative_count = 0
for i in range(3):
    n = int(input("enter a number: "))
    if n > 0:
        positive_count += 1
    elif n < 0:
        negative_count += 1
print("positive count", positive_count)
print("negative count", negative_count)
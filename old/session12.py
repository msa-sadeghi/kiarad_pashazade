# student = {}
# name = input("enter a name: ")
# family = input("enter a family: ")
# age = int(input("enter a age: "))

# student['name'] = name
# student['family'] = family
# student['age'] = age

# print(student)

# name = input("enter a name: ")
# scores =  []
# for i in range(3):
#     s = float(input("enter a score: "))
#     scores.append(s)

# student = {}
# student['name'] = name
# student['scores'] = scores

# print(student)

# s = {
#     'eng' : 'english text',
#     'fra' : 'gre text',
# }
# for l, text in s.items():
#     print(l,text)

# student = {
#            'name': 'artin',
#            'scores': [12.0, 15.0, 16.0]
#            }


# for s in student['scores']:
#     if s > 15:
#         print(s)

# print(sum(student['scores'])/len(student['scores']))

# s = 0
# for sc in student['scores']:
#     s += sc

# print(s/len(student['scores']))


# text = "hello python"

# words = text.split()
# if words[0] == "hello":
#     print("you are well")


# def greet(name):
#     print("hello", name)

# greet("sara")
# greet("artin")
# greet("arezo")
# greet("shadi")
# greet("nikan")


# def jam(a, b, c):
#     return a + b + c


# x = jam(33, 45, 67)
# if x > 100:
#     print("yes")


# def my(a,b):
#     if a > b:
#         return a
#     else:
#         return b
    
# print(my(10, 23))

# تابعی بنویس که عددی را از کارر دریافت نماید 
# عدد دریافت شده را با پنج جمع کند
# حاصل را  تحویل دهد

# print()

# def my_func(name, age):
#     d = {}
#     d['esm'] = name
#     d['sen'] = age
#     return d

# print(my_func("sara", 23))


# def find_max(num1, num2, num3):
#     m = num1
#     if num2 > m:
#         m = num2
#     if num3 > m:
#         m = num3
#     return m

# print(find_max(1,2,3))

# scores = [10, 5, 6, 3,1]

# def good_scores(scores):
#     new_list =  []
#     for s in scores:
#         if s >= 5:
#             new_list.append(s)
#     return new_list

# print(good_scores(scores))

# student1 = {
#     'name' : 'armin',
#     'grade' : 19
# }
# student2 = {
#     'name' : 'arman',
#     'grade' : 18
# }
# def concat_dict(dict1, dict2):
#     output = {}
#     for k, v in dict1.items():
#         output[k] = [v]
#     for k, v in dict2.items():
#         output[k].append(v)
#     return output
# print(concat_dict(student1, student2))

# def c_to_f(t):
#     return t * 1.8 + 32

# print(c_to_f(2))
n = int(input("enter a number: "))
for i in range(1,n):
    print(i)
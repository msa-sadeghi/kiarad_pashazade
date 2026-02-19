total = 0
all_numbers = []
for i in range(5):
    number = int(input("enter a number: "))
    all_numbers.append(number)
    total += number
print("total is :", total)
print("average is is :", total/5)
all_numbers.sort()
print(all_numbers)
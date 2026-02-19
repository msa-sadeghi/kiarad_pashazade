def positive_numbers(voroudi):
    result = 0
    for x in voroudi:
        if x > 0:
            result += x
    return result

print(positive_numbers([1,-2,3,-4,-5,6,-7,8,9]))


#تابعی بنویس که لیست نام افراد را بگیرد و فقط آنهایی که
# با
# a 
# شروع می شوند را پرینت کند
# 175 = 1 + 7^2 + 5^3
number = int(input(" Enter the number : "))

def position(num):
    str_num = str(number)
    return len(str_num)

sum = 0
original = number

while number!=0:

    sum += (number%10) ** position(number)
    number = number // 10

if sum == original:
    print(f"{original} is a disarium number ")
else:
     print(f"{original} is not a disarium number ")       


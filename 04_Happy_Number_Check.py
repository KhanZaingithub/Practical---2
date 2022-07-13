number = int(input(" Enter the number "))
original = number
while number>=10:
    sum = 0
    while number>0:
        num = number % 10
        sum = sum +(num ** 2)
        number = number//10
        print(sum)
    number = sum    
if number == 1:
    print(f"{original} is a happy number ")

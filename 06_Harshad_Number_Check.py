# 21 = 2+1
#    = 3
# 21/3 = 7
number = int(input(" Enter the number : "))
original = number
sum = 0
while number>0:
    reminder = int(number%10)
    sum = sum + reminder
    number = number // 10
if original%sum == 0:
    print(f"{original} is a harshad number ")   
else:
     print(f"{original} is not a harshad number ")    


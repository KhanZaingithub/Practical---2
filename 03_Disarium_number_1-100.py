def numberlength(n):
    length = 0
    while(n != 0):
        length = length +1
        n = n//10
    return length    

def sum(num):
    rem = sum =0
    len = numberlength(num)

    while(num>0):
        rem = num%10
        sum =sum + (rem ** len)
        num = num//10
        len = len-1
    return sum   

result = 0

print(" Disarium numbers between 1 - 100 are : ")
for i in range (1,101):
    result = sum(i)

    if(result == i):
        print(i)

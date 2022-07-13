num = int(input(" Enetr starting point : "))
num1 = int(input(" Enetr ending point : "))
while num<=num1:
    sum = 0
    temp = num
    while sum!=1 and sum !=4:
        sum = 0
        while temp !=0:
            rem = int(temp%10)
            sum = sum + (rem**2)
            temp = temp//10
        temp = sum 
    if sum == 1:
     print(num)      
    num = num + 1

#2*3 = 6
num = int(input(" Enter the starting number : "))
num1 = int(input(" Enter the last number : "))
def ispronicnumber(num):
    flag = False

    for i in range(1,num+1):
        if((i*(i+1))==num):
            flag = True
            break
    return flag    

print("The Pronic numbers are : ")       
for j in range(num,num1):
    if(ispronicnumber(j)):
        print(j)
        
        
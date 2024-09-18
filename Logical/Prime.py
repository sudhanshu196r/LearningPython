
num = int(input("Enter a number: "))

if(num==1):
    print("1 is not prime")

flag = True
i = 2
while i<=num/2:
    if(num%i==0):
        flag = False
    i+=1

if flag:
    print("Number is prime")
else:
    print("Number is not prime")
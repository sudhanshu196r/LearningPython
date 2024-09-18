

num = int(input("Enter the number: "))

i=2
while(i*i<=num):

    flag = True
    for x in range(2,i):
        if(i%x==0):
            flag = False
            break

    if flag:
        if(num%i==0):
            print(i)
    i+=1
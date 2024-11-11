'''
    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-11-2024
    @Title : Get Prime Factor

'''

import random

num = int(input("Enter no. of times to flip the coin: "))
count_head = 0
count_tail = 0
for x in range(0,num):
    random_num = random.random();
    if random_num<0.5:
        count_tail+=1
    else:
        count_head+=1

head_per = count_head*100/num
tail_per = count_tail*100/num

print(f"Head percentage: {head_per}  Tail percentage: {tail_per}")

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

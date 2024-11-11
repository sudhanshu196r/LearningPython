'''
    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-11-2024
    @Title : Harmonic Number

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

pos = int(input("Enter the Nth position: "))

sum = 0

for x in range(1,pos+1):
    sum = sum+1/x;

print("Nth Harmonic number is: ",sum)
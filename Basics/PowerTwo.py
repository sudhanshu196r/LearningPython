'''
    @Author: Sudhanshu Kumar
    @Date: 19-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 04-11-2024
    @Title : Get power of two

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

pow = int(input("Enter power N: "))

for x in range(0,pow+1):
    res = 1
    for  y in range(0,x):
        res = res*2

    print(f"2 ^ {x} = {res}")

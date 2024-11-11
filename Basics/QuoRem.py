'''
    @Author: Sudhanshu Kumar
    @Date: 20-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 11-11-2024
    @Title : Quotient and Remainder

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

num = int(input("Enter a number: "))
div = int(input("Enter divisor: "))
quo = num/div
rem = num%div

print(f"Quotient is {quo} and remainder is {rem}")


term = int(input("Enter the term: "))

first = 0
second = 1
print(first)
print(second)
i=3
while i<=term:
    temp = first+second
    first = second
    second = temp
    print(temp)
    i+=1

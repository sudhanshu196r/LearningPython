

pow = int(input("Enter power N: "))

for x in range(0,pow+1):
    res = 1
    for  y in range(0,x):
        res = res*2

    print(f"2 ^ {x} = {res}")
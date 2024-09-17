

pos = int(input("Enter the Nth position: "))

sum = 0

for x in range(1,pos+1):
    sum = sum+1/x;

print("Nth Harmonic number is: ",sum)

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))

largest = num1
if(num2>num1 and num2>num3):
    largest = num2
elif(num3>num1 and num3>num2):
    largest = num3

print("Largest is : ",largest)  
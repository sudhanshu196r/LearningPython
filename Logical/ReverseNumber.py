
'''
    @Author: Sudhanshu Kumar
    @Date: 16-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 16-09-2024
    @Title : Python program to reverse a number

'''

def reverseNum(num):
    """
        Description :
            This function is used to return reverse of a number
        Parameters :
            num: This is the number that we have to reverse
        Return :
            It returns reverse of the number
    """
    
    rev = 0
    while num>0:

        rem = num%10
        rev = rev*10+rem
        num = num//10
    
    return rev

def main():
    num = int(input("Enter a number: "))
    rev = reverseNum(num)
    print(f"Reverse of {num} is {rev}")

if __name__=="__main__":
    main()

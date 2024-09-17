'''
    @Author: Sudhanshu Kumar
    @Date: 17-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 17-09-2024
    @Title : Python program to convert from fahrenheit

'''

def fahren_to_cels(temp):
    """
    
    Description:
        logic to convert temp from fahrenheit to celsius
    Parameters:
        temp : temperature in fahrenheit
    Return:
        temperature in celsius

    """

    temp_cel = (temp-32)*5//9
    return temp_cel

def main():
    temp = int(input("Enter temperature in Fahrenheit: "))
    temp_cel = fahren_to_cels(temp)
    print(f"Temperature is {temp_cel} C")

if __name__=="__main__":
    main()

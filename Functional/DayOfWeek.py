'''
    @Author: Sudhanshu Kumar
    @Date: 17-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 17-09-2024
    @Title : Python program to find day of a week of a particular date

'''


class Util:
    @staticmethod
    def dayOfWeek(m, d, y):
        """
        Description :
            This function is used to return the day of the week
        Parameters :
            m : represents month
            d : represents date
            y : represents year
        Return :
            It returns the day of the week where 0 represents Sunday
    """
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + (31 * m0) // 12) % 7
        return d0

if __name__ == "__main__":
    # Take input from the user
    m = int(input("Enter month (1-12): "))
    d = int(input("Enter day (1-31): "))
    y = int(input("Enter year: "))

    # Call the dayOfWeek function from the Util class
    day = Util.dayOfWeek(m, d, y)

    # Print the day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
    print(f"The day of the week is: {day}")

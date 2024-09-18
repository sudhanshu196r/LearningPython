'''
    @Author: Sudhanshu Kumar
    @Date: 16-09-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 16-09-2024
    @Title : Python program to reverse a number

'''



import time


start_time=None
end_time=None
def start():
    """
    Starts the stopwatch by recording the current time.
    """
    global start_time
    start_time = time.time()
    print("Stopwatch started...")
    #print(start_time)

def stop():
    """
    Stops the stopwatch by recording the current time.
    """
    global end_time
    end_time = time.time()
    print("Stopwatch stopped...")
    #print(end_time)

def elapsed_time():
    """
    Calculates the elapsed time between the start and stop events.
    :return: Elapsed time in seconds.
    """
    #(start_time)
    #print(end_time-start_time)
    return end_time - start_time

# Main program to demonstrate the stopwatch functionality
if __name__ == "__main__":
    
    input("Press Enter to start the stopwatch...")
    start()
    
    input("Press Enter to stop the stopwatch...")
    stop()
    
    elapsed = elapsed_time()
    print(f"Elapsed time: {elapsed:.2f} seconds")

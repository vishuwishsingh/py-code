import time
import os
import pandas

"""
while True:
    if os.path.exists("New/veg.txt"):
        with open("New/veg.txt") as myfile:
            print(myfile.read())
    else:
        print("File Not Avalible")    
    time.sleep(10)
"""
while True:
    if os.path.exists("temps-today.csv"):
        pan_read = pandas.read_csv("temps-today.csv")
        print("State 1 " , pan_read.mean()["st1"])
        print("State 2 " , pan_read.mean()["st2"])
    else :
        print("No CSV File")
    time.sleep(10)


        

    
#Countdown to launch program

#--------------------------
#Import libraries
#--------------------------
import time


#--------------------------
#Subprograms
#--------------------------
def countdown():
    print("T minus ...")
    for counter in range (12, 0, -1):
        print(counter, "...")
        if counter == 9:
            print("Ignition sequence start.")
        time.sleep(1)
    print("0 ...")
    print("All engines running.")
    print("Lift off, we have lift off on Artemis 1.")
    time.sleep(1)
    print("Tower clear.")
    
#--------------------------
#Main program    
#--------------------------
countdown()
    

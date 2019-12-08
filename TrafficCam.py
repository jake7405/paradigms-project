#!/usr/bin/python3
from random import randint
from time import sleep

# This program demonstrates the logical programming paradigm
# Author: Jacob Blackstone
# Class: CSE 240 - Honors Contract
# Description: A simulation of a traffic camera

# Main Menu
print("\nTraffic camera simulator v1.0")
print("------------------------------------\n")
print("This program will simulate a speed camera at an intersection.")
print("Enter any key to begin:") 
start = input() # Pauses execution until user is ready, i.e. user presses key
cont = "y"

while cont == "y":
    print("LIMIT 50 MPH\nSCANNING...")
    sleep(3)

    violation = False   # Whether a scanned car has been detected as speeding
    speed = 0           # Speed of scanned car
    plate = 0           # Suffix of 4 digit int to represent

    # If a scan generates a speed <= 50 MPH, it will treat it as legal and continue to loop/scan
    while violation == False:
        plate = randint(1000,9999)  # Generates plate suffix
        print("\nNEW CAPTURE:")
        print("PLATE NO: ***-" + str(plate))
        speed = randint(25,80)      # Typical speeds found in an intersection
        print("SPEED: " + str(speed) + " MPH")
        
        if speed > 50:  # Triggers "speeding" logic block, breaks while loop
            violation = True
        else: sleep(4)  # Simulate a pause between scans, will loop to scan again


    # This if-else logic block handles the simulated level of
    # action against certain speeding violations
    if speed < 60:
        print("\nCAMERA ACTIVATED!")
        print("Processing info...")
        sleep(3)
        print("Positive plate match for ***-" + str(plate))
        print("Action forwarded to Police dept: $50 Fine\n")
    elif speed >= 60 and speed < 70:
        print("\nCAMERA ACTIVATED!")    # In real life as a driver, one would get flashed at this point
        print("Processing info...")
        sleep(3)                        # Simulates a delay in processing camera info
        print("Positive plate match for ***-" + str(plate))
        print("Action forwarded to Police dept: $125 Fine & Warning\n")
    elif speed >= 70 and speed < 75:
        print("\nCAMERA ACTIVATED!")
        print("Processing info...")
        sleep(3)
        print("Positive plate match for ***-" + str(plate))
        print("Action forwarded to Police dept: $300 Fine, Warning, Mandatory Traffic School\n")
    elif speed >= 75:
        print("\nCAMERA ACTIVATED!")
        print("Processing info...")
        sleep(3)
        print("Positive plate match for ***-" + str(plate))
        print("ALERT: Capture has shown vehicle to be engaging in criminal speeding")
        print("Police Dept dispatched - Further action forwarded: $1000 Fine and min. 1 month suspension")
    else: print("camera error")     # Else for redundancy
    
    cont = input("Run again? y/n: ")
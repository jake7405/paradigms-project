#!/usr/bin/python3

# This program demonstrates the imperative programming paradigm
# Author: Jacob Blackstone
# Class: CSE 240 - Honors Contract
#Description: Simulation of different mathematical operations

# For integer conversion
import math


n = 0
print("MathFuncs v1.0")
print("-----------------------\n")
try:
    n = input("Enter an integer (warning - high values may cause large outputs or long runtimes): ")
    n = int(n)
except ValueError:
    print("That is not an integer, please rerun and try again\n") # this does end the program, but provides directions by catching error
  # main menu  
print("\nA) Find greatest common denominator")
print("B) Find least common multiple")
print("C) Factorial!")
print("D) Fibonacci")
print("Any other key: Quit")
choice = input("Choose an option: ")
choice = choice.upper()


while choice == "A" or choice == "B" or choice == "C" or choice == "D":
    if choice == "A": # This calculates the GCD
        try:
            k = input("Enter another integer: ")
            k = int(k)
        except ValueError:
            print("That is not an integer, please rerun and try again\n")
    
        if n > k:
            smaller = k
        else:
            smaller = n
        for i in range(1, smaller + 1):
         if((n % i == 0) and (k % i == 0)):
            gcd = i 
        print()
        print(gcd)
        
    elif choice == "B": # This calculates the LCM
        try:
            k = input("Enter another integer: ")
            k = int(k)
        except ValueError:
            print("That is not an integer, please rerun and try again\n")
        if n > k:
            greater = n
        else:
         greater = k
        while(True):
            if((greater % n == 0) and (greater % k == 0)):
                lcm = greater
                break
            greater += 1 
        print()
        print(lcm)
        
    elif choice == "C": # This calculates a factorial (n!)
        temp = n
        while temp > 1:
            next = temp - 1
            n = n * next
            temp = temp - 1
        print()
        print(n)
            
    elif choice == "D": # This is an algorith for fibbionacci
        fibs = [0, 1, 1]                                                                                           
        for f in range(2, n):                                                                                      
            fibs.append(fibs[-1] + fibs[-2])                                                                         
        print()
        print(fibs)
    else: break
    
    try:
        n = input("\nEnter an integer: ")
        n = int(n)
    except ValueError:
        print("That is not an integer, please rerun and try again\n")
    
    print("\nA) Find greatest common divisor")
    print("B) Find least common multiple")
    print("C) Factorial!")
    print("D) Fibonacci")
    print("Any other key: Quit")
    choice = input("Choose an option: ")
    choice = choice.upper()
            
    
#!/usr/bin/python3


# This program demonstrates the functional programming paradigm
# Author: Jacob Blackstone
# Class: CSE 240 - Honors Contract
#Description: Simulates a credit card

import random # for balance generation

limit = 100.00 # The maximum that may be allocated to balance every bill cycle
balance = 0.00 # CC balance stored in global memory
APR = 1.24 # Constant

# Only ran once at start of Main()
def generate_balance():
    global limit, balance, APR
    return round(random.uniform(0, limit), 2)
    
# Simulates paying full statement balance
def pay_full():
    global limit, balance, APR
    balance = 0
    print("Balance Paid\n")

# Simulates making a minimum payment with interest (APR) assessed
def min_payment():
    global limit, balance, APR
    min_pay = balance * .25
    balance -= min_pay
    balance *= APR
    round(balance, 2)
    print("Minumum payment made, APR interest assessed\n")

# Simulates making a partial payment of any amount
# Choosing the full balance has the same effect as pay_full()
# Choosing more than the balance credits acount (negative balance)
def pay_partial(amount):
    global limit, balance, APR
    balance -= amount
    balance *= 1.1
    print("Payment of $" + str(amount) + " made, 10 percent interest assessed\n")
 
 # Simulates a new billing cycle only if balance is paid off or negative
 # Random float within limit
def bill_cycle():
    global limit, balance, APR
    balance += round(random.uniform(0, limit), 2)
    print("Bill cycle complete, payment due\n")

# Simulates a late payment including interest (APR) and a penalty
def late_payment(amount):
    global limit, balance, APR
    balance -= amount
    balance *= APR
    balance += 20
    print("Late Payment made, APR interest and $20 penalty assessed")
    
  # Simulates applying for a credit line increase - +100 increment  
def credit_increase():
    global limit, balance, APR
    limit += 100
    print("Credit line increase approved, $100 added to limit")
    
    

def Main():
    
    global limit, balance, APR
    print("This program simulates the month-to-month billing function of a credit card")
    print("-------------------------------------------------------------------------------") 
    print("Directions: You will be given a randomly generated balance within a given limit (set at $100). You may do the following:")
    print("-Pay balance\n-Pay partial amount\n-Minimum payment\n-Late payment\n-Apply for credit line increase")
    start = input("Press any key to start, Q to quit: ")
    start = start.upper()
    balance = generate_balance() # single instance of this function
    
    # main menu
    print("\nBALANCE: $" + str(round(balance,2)))
    print("LIMIT: $" + str(limit))
    print("APR: " + str(APR) + "%")
    print("LATE PENALTY: $20\n")
    ch = input("A) Pay balance\nB) Pay partial amount\nC) Minimum payment\nD) Late payment\nE) Apply for credit line increase\nF) New Bill Cycle\nQ) Quit\nChoose an option: ")
    ch = ch.upper()
        
    while ch != "Q":
        print("\n")
        if ch == "A":
            pay_full()
        elif ch == "B":
            amt = input("Enter an amount to pay off: $")
            amt = float(amt)
            pay_partial(amt)
        elif ch == "C":
            min_payment()
        elif ch == "D":
            amt = input("LATE - Enter an amount to pay off: $")
            amt = float(amt)
            late_payment(amt)
        elif ch == "E":
            credit_increase()
        elif ch == "F":
            if balance <= 0:
             bill_cycle()
            else: print("Balance not yet paid!\n")
            
        print("\nBALANCE: $" + str(round(balance, 2)))
        print("LIMIT: $" + str(limit))
        print("APR: " + str(APR) + "%")
        print("LATE PENALTY: $20\n")
        ch = input("A) Pay balance\nB) Pay partial amount\nC) Minimum payment\nD) Late payment\nE) Apply for credit line increase\nF) New bill cycle\nChoose an option: ")
        ch = ch.upper()
            
Main()
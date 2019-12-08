#!/usr/bin/python3

# This program demonstrates the object-oriented programming paradigm
# Author: Jacob Blackstone
# Class: CSE 240 - Honors Contract
# Description: A simulation of a metro station ticket vendor




# Class for ticket machine
class Machine:
    def scan(self, card):
        print("Scan successful")
        print("Current Balance: $", card.get_balance())
    
    def buy_paper_pass(self, pass_type):
        print("Now printing: ", pass_type)
        
    def buy_metro_card(self, name1, bal1):
        return MetroCard(name1, bal1)
   
# Base Class for pass
class Pass:
    # Pass Types
    available_types = ("90 Minute Transfer", "Day", "3 Day", "Week", "Month", "Semester (Students Only)", "Year")
    name = None
    
    # Default constructor
    def __init__(self):
        pass
    
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # returns passholder name
    def get_name(self):
        return self.name
    
    # sets passholder name to user input
    def set_name(self, n):
        self.name = n
        print("Name set")
        
    # prints pass info
    def print_info(self):
        print("\nNAME: ", get_name())
 
 # Think a reusable plastic card you tap for train fare
 # Inherits from Pass       
class MetroCard(Pass):

    bal = None
    passes = list()
    
    # Constructor
    def __init__(self, name, balance):
        self.name = str(name)
        self.bal = balance
   
    # prints all info about the card - overloaded
    def print_info(self):
        print("\nNAME: ", Pass.get_name(self))
        print("BALANCE: $", str(self.get_balance()))
        print("Passes on card: ", self.list_passes())
    
    # returns declining balance (double)
    def get_balance(self):
        return self.bal
    
    # tops up card balance (double)
    def add_balance(self, balance):
        self.bal += balance
        print("Balance add successful - new balance: $", str(self.bal))
    
    # adds a new pass to the card   
    def buy_pass(self, pass_type):
        self.passes.append(pass_type)
        print(pass_type, " added\n")
    
    # lists all passes stored on card
    def list_passes(self):
            print(self.passes)

# Main function          
def Main():
    available_types = ("90 Minute Transfer", "Day", "3 Day", "Week", "Month", "Semester (Students Only)", "Year")
    print("Welcome to The Simulation Metro")
    print("-----------------------")
    print("A) Buy tickets")
    print("B) Buy new MetroCard")
    print("C) Modify/top up MetroCard")
    print("D) Buy passes")
    print("Press any other key to quit")
    choice = input("Choose an option: ")
    choice = choice.upper()
    mach = Machine() # new machine object
    my_card = None # uninstantiated MetroCard object
    
    while choice == "A" or choice == "B" or choice == "C" or choice == "D":
        if choice == "A":
            p = Pass(None)
            print("A) 90 min. transfer\nB) Day\nC) 3 day")
            ch = input("\nChoose Ticket Type: ")
            ch = ch.upper()
            if ch == "A":
                mach.buy_paper_pass(p.available_types[0])
            elif ch == "B":
                mach.buy_paper_pass(p.available_types[1])
            elif ch == "C":
                mach.buy_paper_pass(p.available_types[2])
        elif choice =="B":
            name = input("\nEnter your name: ")
            bal = input("Enter a starting balance: ")
            bal = float(bal)
            p = MetroCard(name, bal)
            my_card = p
            print("Processing payment...done")
            print("Printing...\n")
        elif choice == "C":
            print("\nReading card...")
            if my_card == None:
                print("Card not activated!")
            else:
                mach.scan(my_card)
                print("A) Modify name\nB) Top up balance\nC) Display card info")
                ch = input("\nChoose an option: ")
                ch = ch.upper()
                if ch == "A":
                    nm = input("\nEnter a name for the card: ")
                    my_card.set_name(nm)
                    print("\n")
                elif ch == "B":
                    top_up = input("Enter an amout to add to your card: ")
                    top_up = float(top_up)
                    my_card.add_balance(top_up)
                elif ch == "C":
                    my_card.print_info()
        elif choice == "D":
             if my_card == None:
                print("Card not activated!")
             else: 
                 print("A) Week\nB) Month\nC) Semester (Reduced - students only)\nD) Year")
                 chc = input("Choose an option: ")
                 chc = chc.upper()
                 if chc == "A": my_card.buy_pass(my_card.available_types[3])
                 elif chc == "B": my_card.buy_pass(my_card.available_types[4])
                 elif chc == "C": my_card.buy_pass(my_card.available_types[5])
                 elif chc == "D": my_card.buy_pass(my_card.available_types[6])
        print("\nA) Buy paper tickets")
        print("B) Buy new MetroCard")
        print("C) Modify/top up MetroCard")
        print("D) Buy passes")
        choice = input("Choose an option: ")
        choice = choice.upper()   
    
    
Main() 
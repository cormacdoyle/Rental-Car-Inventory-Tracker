'''
Assignment 2: Decomposing a Programming Problem
By: Cormac Doyle
Student Number: 20152002

This program takes a list of vehicles for a rental company and allows the user
to manipulate data for viewing as well as make changes to the list, these changes include
adding vehicles, updating vehicle information, and removing vehicles.
'''

import filehandling
import functionality
import commands

'''
this function is raised when the user quits, it asks the user if they would like to save their
changes to the csv file, if yes then it runs the write function in filehandling.py, if no it quits
'''
def saveInventory(car_inventory):
    user_save = input("Would you like to save any changes?('Y' for yes, 'N' for No)\n")
    if user_save.lower() == 'n':
        quit()
    if user_save.lower() == 'y':
        filehandling.writeNewUpdate(car_inventory)
    else:
        print("Invalid Input, please try again.")
        saveInventory(car_inventory)
'''
This function asks the user if they would like to make changes or display info, which accesses commands or functionality
respectively
'''
def chooseCommand(car_inventory):
    command_prompt = input("Please input a command. ('D' for Display Info, 'M' for Make Changes, Press 'Q' to quit)\n")
    if command_prompt.lower() == "d":
        chooseInfo(car_inventory)
    elif command_prompt.lower() == "m":
        chooseChanges(car_inventory)
    elif command_prompt.lower() == "q":
        # user can quit
        saveInventory(car_inventory)
    else:
        # if something invalid is inputted an error message is raised and the function restarts
        print("Invalid Input")
        chooseCommand(car_inventory)

'''
This function gives the user access to all functionality functions
'''
def chooseInfo(car_inventory):
    command_prompt = input("What would you like to display?('A' for All Info, 'U' for Unique Vehicle', 'S' for Characteristic Search, Press 'Q' to quit)\n")
    if command_prompt.lower() == "a":
        functionality.displayAllInfo(car_inventory)
    elif command_prompt.lower() == "u":
        functionality.specificSearch(car_inventory)
    elif command_prompt.lower() == "s":
        chooseCharacteristic(car_inventory) # if they choose to do characteristic search they are brought to another menu
    elif command_prompt.lower() == "q":
        saveInventory(car_inventory)
    else:
        print("Invalid Input")
        chooseInfo(car_inventory)

'''
This function accesses all of the characteristic search functions
'''
def chooseCharacteristic(car_inventory):
    command_prompt = input("What would you like to search by?('M' for Make, 'T' for Type, 'A' for Availability, Press 'Q' to quit)\n")
    if command_prompt.lower() == 'm':
        functionality.searchByMake(car_inventory)
    if command_prompt.lower() == 't':
        functionality.searchByType(car_inventory)
    if command_prompt.lower() == 'a':
        functionality.searchByAvailability(car_inventory)
    elif command_prompt.lower() == "q":
        saveInventory(car_inventory)
    else:
        print("Invalid input, please try again")
        chooseCharacteristic(car_inventory)

'''
this function asks the user what changes they would like to make, these change functions are contained in commands.py
'''
def chooseChanges(car_inventory):
    command_prompt = input("What would you like to change?('A' for Add Vehicle, 'U' for Update Info, 'R' for Remove Vehicle, Press 'Q' to quit)\n")
    if command_prompt.lower() == "a":
        commands.addNewVehicle(car_inventory)
    elif command_prompt.lower() == "u":
        chooseUpdate(car_inventory)
    elif command_prompt.lower() == "r":
        commands.removeVehicle(car_inventory)
    elif command_prompt.lower() == "q":
        saveInventory(car_inventory)

'''
This function asks the user what information they would like to update
'''
def chooseUpdate(car_inventory):
    command_prompt = input("What would you like to update? ('O' for Odometer, 'C' for Cost, 'R' for Rental Status, Press 'Q' to quit)\n")
    if command_prompt.lower() == "o":
        commands.updateOdometer(car_inventory)
    elif command_prompt.lower() == "c":
        commands.updateCost(car_inventory)
    elif command_prompt.lower() == "r":
        commands.updateRentalStatus(car_inventory)
    elif command_prompt.lower() == "q":
        saveInventory(car_inventory)

'''
the main function runs and begins the program
'''
def main():
    car_inventory = filehandling.readData()
    chooseCommand(car_inventory)

if __name__ == "__main__":
    main()
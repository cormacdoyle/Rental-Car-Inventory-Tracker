import random
import userinterface #only userinterface module is contained in commands.py

# newID simply returns a random ID number, I decided to use a function
# because it is referenced several times
def newID():
    return random.randrange(10000,100000)

# getVehicleIDs retrieves vehicle id's given the inventory of all vehicles
def getVehicleIDs(car_inventory):
    IDs = []
    for car in car_inventory:
        IDs.append(car["VehicleID"])
    return IDs
'''
checkForIDs takes 2 parameters, the inventory of all vehicles, and recently
inputted new vehicle information, it finds the vehicle that the user is
searching for
'''
def checkForIDs(car_inventory, new_vehicle):
    new_vehicle['VehicleID'] = int(input("Enter a vehicle ID\n"))
    for vehicle in car_inventory:
        if new_vehicle['VehicleID'] == vehicle['VehicleID']:
            print("This ID is already in use, please enter a new ID number")
            checkForIDs(car_inventory, new_vehicle) #after the function is finished, the user is returned to the menu

'''
addNewVehicle take the inventory of all vehicles and asks the user for
several inputs required to record a new vehicle, it then adds this 
new vehicle to the inventory of all vehicles
'''
def addNewVehicle(car_inventory):
    newVehicle = {}
    '''
    this part of the function cross references the random ID number with existing IDs to
    ensure that a vehicle with this ID does not already exist
    '''
    newidentification = input("Would you like a new Identification number? (Y/N)\n")
    if newidentification.lower() == 'y':
        IDs = getVehicleIDs(car_inventory) 
        newVehicle['VehicleID'] = newID()
        while newVehicle["VehicleID"] in IDs:
            newVehicle['VehicleID'] = newID()
        for vehicle in car_inventory:
            if vehicle['VehicleID'] == newVehicle['VehicleID']:
                newVehicle['VehicleID'] = newID()

    elif newidentification.lower() == 'n':
        checkForIDs(car_inventory, newVehicle)

    else:
        print("Invalid input")
        addNewVehicle(car_inventory) # when the user gives an invalid input the function restarts

    newVehicle['make'] = input("What is the make of the vehicle?\n")
    newVehicle['vehicletype'] = input("What type of vehicle is it?\n")
    newOdometer(car_inventory, newVehicle)
    newRentalCost(car_inventory, newVehicle)
    newVehicleUse(car_inventory, newVehicle)
    newVehicle['availabletorent'] = "AVAILABLE" # new vehicles are automatically set to available
    car_inventory.append(newVehicle) # here, the car is added to the inventory of all vehicles
    userinterface.chooseCommand(car_inventory) # when the function is finished, the user is returned to the menu

'''
this function is referenced in addNewVehicle, it takes an input for how many times
the vehicle has been used and ensures that this value is an integer, while in most
cases new vehicles will be used 0 times, in the event that a vehicle was accidentally
deleted, this function is useful
'''
def newVehicleUse(car_inventory, newVehicle):
    new_vehicle_use = input("How many times has the vehicle been used?\n")
    try:
        newVehicle['vehicleuse'] = int(new_vehicle_use)
    except ValueError:   
        print("Invalid Input, Please try again.")
        newVehicleUse(car_inventory, newVehicle)

'''
This function is referenced in addNewVehicle, it takes newvehicle information and
the inventory of all vehicles and ensures that the rental cost entered is an integer
'''
def newRentalCost(car_inventory, newVehicle):
    new_vehicle_cost = input("What is the vehicle's daily rental price?\n")
    try:
        newVehicle['rentalcost'] = int(new_vehicle_cost)
    except ValueError:
        print("Invalid Input, Please try again.")
        newRentalCost(car_inventory, newVehicle)
'''
This function is referenced in addNewVehicle, it takes newvehicle information and
the inventory of all vehicles and ensures that the odometer value entered is an integer
'''
def newOdometer(car_inventory, newVehicle):
    new_vehicle_odometer = input("What is the Odometer reading of the car?\n")
    try:
        newVehicle['odomoterreading'] = int(new_vehicle_odometer)
    except ValueError:
        print("Invalid Input, Please try again.")
        newOdometer(car_inventory, newVehicle)

'''
This function takes the inventory of all vehicles and searches for an inputted ID,
it then checks to make sure a vehicle with this ID exists, prompts the user to input
a new odometer value, checks to make sure this value is an integer and changes reading
'''
def updateOdometer(car_inventory):
    vehicle_choice = input("Please enter the ID of the vehicle you want to update.\n")
    for vehicle in car_inventory:
        #for loop and if statement ensure a vehicle with this ID exists
        if str(vehicle["VehicleID"]) == vehicle_choice:
            # try except statement ensures value is an integer
            try:
                new_value = input("What is the vehicles new odometer reading?\n")
                vehicle['odomoterreading'] = int(new_value) 
                userinterface.chooseCommand(car_inventory)
            except ValueError:
                # it raises a value error if the input is not an integer, it then restarts the function
                print("Invalid input, Odometer value must be a number, please try again.")
                updateOdometer(car_inventory)
    # if there is no matching vehicle ID, this error message is printed and the function is run again
    print("A vehicle with this ID does not exist, please try again")
    updateOdometer(car_inventory)

'''
This function takes the inventory of all vehicles and searches for an inputted ID,
it then checks to make sure a vehicle with this ID exists, prompts the user to input
a new rental cost per day value, checks to make sure this value is an integer and changes the reading
'''
def updateCost(car_inventory):
    vehicle_choice = input("Please enter the ID of the vehicle you want to update\n")
    for vehicle in car_inventory:
        #for loop and if statement ensure a vehicle with this ID exists
        if str(vehicle['VehicleID']) == vehicle_choice:
            # try except statement ensures value is an integer
            try:
                new_value = input("What is the vehicles new cost per day?\n")
                vehicle['rentalcost'] = int(new_value)
                userinterface.chooseCommand(car_inventory)
            except ValueError:
                # it raises a value error if the input is not an integer, it then restarts the function
                print("Invalid Input, Rental Cost value must be a number, please try again.")
                updateCost(car_inventory)
    # if there is no matching vehicle ID, this error message is printed and the function is run again
    print("A vehicle with this ID does not exist, please try again")
    updateCost(car_inventory)

'''
This function takes the inventory of all vehicles and searches for an inputted ID,
it then checks to make sure this ID exists, if it does it asks the user to change
its rental status and then returns them to the menu, if it does not match then it
produces an error message and asks for ID again
'''
def updateRentalStatus(car_inventory):
    vehicle_choice = input("Please enter the ID of the vehicle you want to update.\n")
    for vehicle in car_inventory:
        # for loop searches through inventory
        if str(vehicle["VehicleID"]) == vehicle_choice:
            new_value = input("Is the vehicle available for rent?(Y/N)\n")
            if new_value.lower() == 'y':          
                vehicle['availabletorent'] = 'AVAILABLE'
                userinterface.chooseCommand(car_inventory)
            elif new_value.lower() == 'n':
                vehicle['availabletorent'] = 'RESERVED'
                userinterface.chooseCommand(car_inventory)
            else:
                # if n or y is not entered an error message is raised
                print("Invalid input, please try again.")
                updateRentalStatus(car_inventory)
    # if the inputted ID does not match an existing ID an error message is raised
    print("A vehicle with this ID does not exist, please try again")
    updateRentalStatus(car_inventory)


'''
this function searches for an inputted ID and removes the ID's corresponding dictionary
from the inventory of all vehicles which is a parameter
'''
def removeVehicle(car_inventory):
    search_item = input("Enter the ID of the vehicle you want to remove.\n")
    for vehicle in car_inventory:
        if str(vehicle['VehicleID']) == search_item:
            car_inventory.remove(vehicle)
    userinterface.chooseCommand(car_inventory)

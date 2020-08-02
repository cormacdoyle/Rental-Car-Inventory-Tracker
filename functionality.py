import userinterface

'''
given the list of all vehicles in the inventory, this function displays all of them,
it contains a counter so that the information is easy to read
'''
def displayAllInfo(car_inventory):
    counter = 0
    for vehicle in car_inventory:
        counter += 1
        print("\nVehicle ", str(counter))
        print("Make:", str(vehicle['make']))
        print("Type:", str(vehicle['vehicletype']))
        print("ID:", str(vehicle['VehicleID']))
        print("Odomoter reading:", str(vehicle['odomoterreading']))
        print("Price per day:", str(vehicle['rentalcost']))
        print("Number of vehicle uses:", str(vehicle['vehicleuse']))
        print("Available?", str(vehicle['availabletorent']))
    print("\nInfo Displayed")
    userinterface.chooseCommand(car_inventory)
'''
given a list of all vehicles in the inventory this function asks for a specific vehicles
ID and returns that vehicles information
'''
def specificSearch(car_inventory):
    search_item = input("What is the vehicle's ID number? \n")
    search_vehicle = [] # this list allows me to easily check if the vehicle exists
    for inventory_item in car_inventory:
        if search_item == str(inventory_item['VehicleID']):
            search_vehicle.append(inventory_item)
            print("Availability:", str(inventory_item['availabletorent']))
            print("Vehicle Make:", str(inventory_item['make']))
            print("Odomoter reading:", str(inventory_item['odomoterreading']))
            print("Daily Price:", str(inventory_item['rentalcost']))
            print("Vehicle Uses:", str(inventory_item['vehicleuse']))
    if search_vehicle == []:
        # if the vehicle's ID is not found this error message is raised
        print("There is no vehicle with this ID")
        userinterface.chooseCommand(car_inventory)
    userinterface.chooseCommand(car_inventory)
'''
Given a list of all vehicles and a user inputted make name, this function searches
through the vehicle's makes and returns all corresponding vehicles
'''
def searchByMake(car_inventory):
    user_make = str(input("What make would you like to search for?\n"))
    user_search_list = [] # this list allows me to easily check if the vehicle exists
    counter = 0 # this counter allows the vehicles to be displayed in an easily understandable way
    for vehicle in car_inventory:
        if user_make.lower() == vehicle['make'].lower():
            user_search_list.append(vehicle)
    if len(user_search_list) == 0:
        # if no vehicles match the input this message is raised
        print("There appears to be no vehicles by this make")
        userinterface.chooseCommand(car_inventory)
    else:
        for vehicle in user_search_list:
            # vehicles that are found are displayed in this section
            counter+=1
            print("\nVehicle", counter)
            print("Vehicle ID:", str(vehicle['VehicleID']))
            print("Make:", str(vehicle['make']))
            print("Type:", str(vehicle['vehicletype']))
            print("Rental Cost:",str(vehicle['rentalcost']))
            print("Vehicle Uses:", str(vehicle['vehicleuse']))
            print("Availability:", str(vehicle['availabletorent'])+"\n")
        userinterface.chooseCommand(car_inventory)


'''
Given a list of all vehicles and a user inputted vehicle type name, this function searches
through the vehicle's type and returns all corresponding vehicles
'''
def searchByType(car_inventory):
    user_type = str(input("What type would you like to search for?\n"))
    user_search_list = [] # this list allows me to easily check if the vehicle exists
    counter = 0 # this counter allows the vehicles to be displayed in an easily understandable way
    for vehicle in car_inventory:
        if user_type.lower() == vehicle['vehicletype'].lower():
            user_search_list.append(vehicle)
            # if the vehicle is found they are added to the list
    if len(user_search_list) == 0:
        # if no vehicles are found this message is raised
        print("There appears to be no vehicles by this type")
        userinterface.chooseCommand(car_inventory)
    else:
        for vehicle in user_search_list:
            # matching vehicles are displayed using this section
            counter+=1
            print("\nVehicle", counter)
            print("Vehicle ID:", str(vehicle['VehicleID']))
            print("Make:", str(vehicle['make']))
            print("Type:", str(vehicle['vehicletype']))
            print("Rental Cost:",str(vehicle['rentalcost']))
            print("Vehicle Uses:", str(vehicle['vehicleuse']))
            print("Availability:", str(vehicle['availabletorent'])+"\n")
        userinterface.chooseCommand(car_inventory)
'''
Given a list of all vehicles and what the vehicles availability status is, this function searches
through the vehicle's makes and returns all vehicles with a corresponding availability status
'''
def searchByAvailability(car_inventory):
    user_availability = input("Would you like to search for available or reserved vehicles?('R' for reserved, 'A' for available, Press 'Q' to quit)\n")
    user_search_list = [] # this list allows me to easily check if the vehicle exists
    counter = 0 # this counter allows the vehicles to be displayed in an easily understandable way
    for vehicle in car_inventory:
        if user_availability.lower() == "r":
            if str(vehicle['availabletorent']) == "RESERVED":
                user_search_list.append(vehicle)
        if user_availability.lower() == "a":
            if str(vehicle['availabletorent']) == "AVAILABLE":
                user_search_list.append(vehicle)
        if user_availability.lower() == 'q':
            userinterface.saveInventory(car_inventory)
    if len(user_search_list) == 0:
        print("Invalid Input, try again")
        searchByAvailability(car_inventory)
    else:
        for vehicle in user_search_list:
            # matching vehicles are displayed using this section
            counter+=1
            print("\nVehicle", counter)
            print("Vehicle ID:", str(vehicle['VehicleID']))
            print("Make:", str(vehicle['make']))
            print("Type:", str(vehicle['vehicletype']))
            print("Rental Cost:",str(vehicle['rentalcost']))
            print("Vehicle Uses:", str(vehicle['vehicleuse']))
            print("Availability:", str(vehicle['availabletorent'])+"\n")
        userinterface.chooseCommand(car_inventory)


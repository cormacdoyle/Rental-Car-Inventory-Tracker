'''
This function has the database file hard copied into it, when called it reads through this data file
and stores each line in a dictionary, which is then stored in a list
'''
def readData():
    filename = ("database1.csv")
    fileIn = open(filename, 'r')
    carData = []
    line = "start"
    while line != "":
        line = fileIn.readline().strip()
        if line != "":
            values = line.split(',')
            wordData = {}
            wordData['VehicleID'] = int(values[0])
            wordData['make'] = str(values[1].strip())
            wordData['vehicletype'] = str(values[2].strip())
            wordData['odomoterreading'] = int(values[3])
            wordData['rentalcost'] = int(values[4])
            wordData['vehicleuse'] = int(values[5])
            wordData['availabletorent'] = str(values[6].strip())
            carData.append(wordData)
    fileIn.close()
    return carData
'''
This function allows the user to save their changes to the csv file so that changes
are not deleted when the function ends, the entire vehicle inventory file is rewritten
into the csv file
'''
def writeNewUpdate(car_inventory):
    filename = ("database1.csv")
    fileIn = open(filename, 'w')
    for new_line_info in car_inventory:
        fileIn.writelines(str(new_line_info['VehicleID']) + ',' + str(new_line_info['make'])+',' + str(new_line_info['vehicletype'])+',' + str(
            new_line_info['odomoterreading'])+',' + str(new_line_info['vehicleuse']) + ',' + str(new_line_info['rentalcost']) + ',' + str(new_line_info['availabletorent'])+"\n")

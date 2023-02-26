import sys

def main():
    limits = parse_limits()
    sensor_data = []
    counter = 0
    if len(limits) > 0 and check_limits(limits):
        sensor_data = read_sensors()
        #This method print temperature under and upper limits and
        # also time when it was happend
        for row in sensor_data:
            counter+=1
            for elem in row:
                if elem < limits[0]:
                    print(elem, str(counter - 1) + ":00")
                if elem > limits[1]:
                    print(elem, str(counter - 1) + ":00")

    else:
        print("Error: Incorrect command line arguments.")

# This is the parse_limits function for getting the temperature
# limits from the command line parameters. Returns an array
# that has the limits (limits[0] has min. temperature limit and
# limits[1] has max. temperature limit). If there is an exception
# reading the command line paratmeters, the limits array is empty.
def parse_limits():
    limits = []

    try:
        limits = [int(sys.argv[1]), int(sys.argv[2])]
    except Exception:
        pass
    
    return limits

# This is the check_limits function that gets an array containing the
# limits as a parameter and checks that the lower limit is smaller
# than the higher limit. If this is the case, the function returns
# True. Otherwise, it returns False.
def check_limits(limits):
    if limits[0] < limits[1]:
        return True
    else:
        return False

# This is a stub implementation for function read_sensors
# returning a fixed sensor readings (four sensors, five readings per
# sensor) for development and testing. To be replaced with an actual
# implementation.
def read_sensors():
    result = []
    file1 = open("testdata/sensor1.txt")
    file2 = open("testdata/sensor2.txt")
    file3 = open("testdata/sensor3.txt")
    file4 = open("testdata/sensor4.txt")

    for i in range(24):
        line = []
        data1 = file1.readline()
        data2 = file2.readline()
        data3 = file3.readline()
        data4 = file4.readline()

        newList1 = data1.split(',')
        newList2 = data2.split(',')
        newList3 = data3.split(',')
        newList4 = data4.split(',')

        line.append(float(newList1[1].replace("\n", ""))) 
        line.append(float(newList2[1].replace("\n", ""))) 
        line.append(float(newList3[1].replace("\n", ""))) 
        line.append(float(newList4[1].replace("\n", ""))) 
        result.append(line)
    file1.close()
    file2.close()
    file3.close()
    file4.close()
    return result

# Other parts of the implementation such as printing the information
# for the operator are also missing and to be implemented.

if __name__ == "__main__":
    main()

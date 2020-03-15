# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part.2 
#======================================
# Read cwb weather data
cwb_filename = '107061220.csv'
data = []  # declartion of list
header = [] # declartion of list type
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames # then header will be 'station_id", 'obsTime', 'ELEV', etc
    for row in mycsv:
        data.append(row) # then data will become a list of dictionary object: data = [dictionary0, dictionary1, .....]
#=======================================

# Part. 3
#=======================================
target_id = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
target_data = [] # used to store the output data

for i in range(len(target_id)):
    temp = [] # temporarily store the data that will be sum to one
    current_target = target_id[i] # search different station_id in each interation
    for j in range(len(data)):
        """ search around the whole data """
        if (data[j]['station_id'] == current_target):
            if data[j]['HUMD'] == '-999.000' or data[j]['HUMD'] == '-99.000':
                temp.append('None')
            else:
                temp.append(float(data[j]['HUMD']))
    
    sum = 0
    all_None = True
    for j in range(len(temp)):
        if (temp[j] != 'None'):
            all_None = False
            sum = sum + temp[j]
    if all_None:
        sum = 'None'
    target_data.append([current_target, sum])

#======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================

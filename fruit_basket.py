import csv

# get filename
filename = 'basket.csv'

# empty lists for data
headers = []
rows = []

# read csv file
with open(filename) as csvfile:
    basketreader = csv.reader(csvfile)

    # save header names
    headers = next(basketreader)

    # save fruit data
    for each_row in basketreader:
        rows.append(each_row)

#print("Fields: " + str(headers))

# get all the fruits & print
fruits = []
for each_row in rows:
    fruits.append(each_row[0])

# print total number of fruit in basket
print("Number of fruit total: " + str(len(fruits)))

# get types of fruit & print
uniquefruits = set(fruits)
print("There are " + str(len(uniquefruits)) + " types of fruit: " + str(uniquefruits))
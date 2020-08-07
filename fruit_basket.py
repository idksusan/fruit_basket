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

# print total number of fruit in basket
print("There are " + str(len(rows)) + " fruits total in this basket.")

# get all the fruits & print
fruits = []
for each_row in rows:
    fruits.append(each_row[0])

# get types of fruit & print
uniquefruits = set(fruits)
print("There are " + str(len(uniquefruits)) + " types of fruit: " + ", ".join(uniquefruits) + ".")

# empty fruit lists
# TODO: extract fruit names from data
apples = []
oranges = []
grapefruit = []
pineapple = []
watermelon = []

# get individual lists of fruits
index = 0

for row in fruits:
    if fruits[index] == 'apple':
        apples.append(fruits[index])
    elif fruits[index] == 'orange':
        oranges.append(fruits[index])
    elif fruits[index] == 'grapefruit':
        grapefruit.append(fruits[index])
    elif fruits[index] == 'pineapple':
        pineapple.append(fruits[index])
    elif fruits[index] == 'watermelon':
        watermelon.append(fruits[index])
    index += 1

# get number of fruit by type & print
# TODO: order by descending
numapple = str(len(apples))
numorange = str(len(oranges))
numgrapefruit = str(len(grapefruit))
numpineapple = str(len(pineapple))
numwatermelon = str(len(watermelon))

print("In this basket there are " + numapple + " apples, " + numorange + " oranges, " + numgrapefruit + " grapefruit, " + numpineapple + " pineapple, " + numwatermelon + " watermelon.")
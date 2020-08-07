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

# map types of fruit to fruit counts
fruit_count = {}
for each_row in rows:
    if each_row[0] not in fruit_count:
        fruit_count[each_row[0]] = 1
    else:
        fruit_count[each_row[0]] = fruit_count[each_row[0]] + 1

# print number of unique fruits
print("There are " + str(len(fruit_count)) + " unique fruits in the basket.")

# sort fruits in descending order & print
print("There are ", end='')
[print(str(value) + " " + key + "s, ", end='') for (key, value) in sorted(fruit_count.items(), key=lambda x: x[1], reverse = True)]
print("in the basket.")

# map types of fruit to characteristics & print
fruit_style = {}
for each_row in rows:
    if each_row[0] not in fruit_style:
        fruit_style[each_row[0]] = each_row[2] + ", " + each_row[3]

print("These are the characteristics of fruit in the basket:")
[print(key + ": " + value) for (key, value) in fruit_style.items()]
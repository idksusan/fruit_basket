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

# map types of fruit to fruit counts
fruit_count = {}
for each_row in rows:
    if each_row[0] not in fruit_count:
        fruit_count[each_row[0]] = 1
    else:
        fruit_count[each_row[0]] = fruit_count[each_row[0]] + 1

# map types of fruit to characteristics
fruit_style = {}
for each_row in rows:
    if each_row[0] not in fruit_style:
        fruit_style[each_row[0]] = each_row[2] + ", " + each_row[3]

# check fruit age
old_fruit = []
for each_row in rows:
    if each_row[1] > str(3):
        old_fruit.append(each_row)

# count how many fruits of each type over
apple_count = 0
orange_count = 0
pineapple_count = 0
watermelon_count = 0

for each_row in old_fruit:
    if each_row[0] == 'apple':
        apple_count += 1
    elif each_row[0] == 'orange':
        orange_count += 1
    elif each_row[0] == 'pineapple':
        pineapple_count += 1
    elif each_row[0] == 'watermelon':
        watermelon_count += 1

# print total number of fruit in basket
print("There are " + str(len(rows)) + " fruits total in this basket.")

# print number of unique fruits
print("There are " + str(len(fruit_count)) + " unique fruits in the basket.")

# sort fruits in descending order & print
print("There are ", end='')
[print(str(value) + " " + key + "s, ", end='') for (key, value) in sorted(fruit_count.items(), key=lambda x: x[1], reverse = True)]
print("in the basket.")

# print fruit characteristics
print("These are the characteristics of fruit in the basket:")
[print(key + ": " + value) for (key, value) in fruit_style.items()]

# print fruit age
print("There are " + str(len(old_fruit)) + " fruits over 3 days old in the basket: ")

# print types of old fruit
print(str(apple_count) + " apples, " + str(orange_count) + " oranges, " + str(pineapple_count) + " pineapples, " + str(watermelon_count) + " watermelons.")
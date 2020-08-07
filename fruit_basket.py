import csv
import tkinter as tk

# read csv file
def read_file(filename):
    # empty lists for data
    headers = []
    rows = []
    with open(filename) as csvfile:
        basketreader = csv.reader(csvfile)

        # save header names
        headers = next(basketreader)

        # save fruit data
        for each_row in basketreader:
            rows.append(each_row)
    return rows

# find overall fruit count
def count_fruit(rows):
    fruit_count = "There are " + str(len(rows)) + " fruits total in this basket."
    return fruit_count

# map types of fruit to fruit counts
def map_fruit_types(rows):
    fruit_count = {}
    for each_row in rows:
        if each_row[0] not in fruit_count:
            fruit_count[each_row[0]] = 1
        else:
            fruit_count[each_row[0]] = fruit_count[each_row[0]] + 1
    return fruit_count

# find types of fruit
def count_fruit_types(fruit_count):
    unique_fruit_count = "There are " + str(len(fruit_count)) + " unique fruits in the basket."
    return unique_fruit_count

# map types of fruit to characteristics
def map_fruit_style(rows):
    fruit_style = {}
    for each_row in rows:
        if each_row[0] not in fruit_style:
            fruit_style[each_row[0]] = each_row[2] + ", " + each_row[3]
    return fruit_style

# check fruit age
def check_age(rows):
    old_fruit = []
    for each_row in rows:
        if each_row[1] > str(3):
            old_fruit.append(each_row)
    return old_fruit


# count how many fruits of each type over
def check_type_age(old_fruit):
    type_ages = [0, 0, 0, 0]
    for each_row in old_fruit:
        if each_row[0] == 'apple':
            type_ages[0] += 1
        elif each_row[0] == 'orange':
            type_ages[1] += 1
        elif each_row[0] == 'pineapple':
            type_ages[2] += 1
        elif each_row[0] == 'watermelon':
            type_ages[3] += 1
    return type_ages

def create_frame(rows):
    root = tk.Tk()
    root.title("Fruit Basket")

    canvas1 = tk.Canvas(root, width = 600, height = 400, relief = 'raised')
    canvas1.pack()

    l1 = Label(root, text = "Fruit Data")
    l1.grid(row = 0, column = 3, sticky = W, pady = 2)

    root.mainloop()

def main():
    rows = read_file('basket.csv')
    fruit_count = map_fruit_types(rows)
    fruit_style = map_fruit_style(rows)
    old_fruit = check_age(rows)
    type_ages = check_type_age(old_fruit)

    create_frame(rows)

    # # print total fruit
    # print(count_fruit(rows))

    # # print total unique fruit
    # print(count_fruit_types(fruit_count))

    # # sort fruits in descending order & print
    # print("There are ", end='')
    # [print(str(value) + " " + key + "s, ", end='') for (key, value) in sorted(fruit_count.items(), key=lambda x: x[1], reverse = True)]
    # print("in the basket.")

    # # print fruit characteristics
    # print("These are the characteristics of fruit in the basket:")
    # [print(key + ": " + value) for (key, value) in fruit_style.items()]

    # # print fruit age
    # print("There are " + str(len(old_fruit)) + " fruits over 3 days old in the basket: ")

    # # print types of old fruit
    # print(str(type_ages[0]) + " apples, " + str(type_ages[1]) + " oranges, " + str(type_ages[2]) + " pineapples, " + str(type_ages[3]) + " watermelons.")

    

if __name__ == "__main__":
    main()
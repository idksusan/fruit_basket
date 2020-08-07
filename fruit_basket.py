import csv

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

# sort fruit count in descending order
def sort_fruit(fruit_count):
    sorted_fruit = ""
    for (key, value) in sorted(fruit_count.items(), key=lambda x: x[1], reverse=True):
        sorted_fruit += str(value) + " " + key + "s, "
    sort_string = "There are " + sorted_fruit + "in the basket."
    return sort_string

# map types of fruit to characteristics
def map_fruit_style(rows):
    fruit_style = {}
    for each_row in rows:
        if each_row[0] not in fruit_style:
            fruit_style[each_row[0]] = each_row[2] + ", " + each_row[3]
    return fruit_style

# write fruit characteristics
def write_style(fruit_style):
    fruit_styles = ""
    for (key, value) in fruit_style.items():
        fruit_styles += key + "| " + value + "\n"
    return fruit_styles

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

def main():
    rows = read_file('basket.csv')
    fruit_count = map_fruit_types(rows)
    fruit_style = map_fruit_style(rows)
    old_fruit = check_age(rows)
    type_ages = check_type_age(old_fruit)
    sorted_fruit = sort_fruit(fruit_count)
    fruit_styles = write_style(fruit_style)

    f = open("fruit_metrics.txt", "w+")

    # print total fruit
    f.write(count_fruit(rows) + "\n")

    # print total unique fruit
    f.write(count_fruit_types(fruit_count) + "\n")

    # sort fruits in descending order & print
    f.write(sorted_fruit + "\n")

    # print fruit characteristics
    f.write("These are the characteristics of fruit in the basket:" + "\n")
    f.write(fruit_styles)

    # print fruit age
    f.write("There are " + str(len(old_fruit)) + " fruits over 3 days old in the basket: ")

    # print types of old fruit
    f.write(str(type_ages[0]) + " apples, " + str(type_ages[1]) + " oranges, " + str(type_ages[2]) + " pineapples, " + str(type_ages[3]) + " watermelons.")

    f.close()

    

if __name__ == "__main__":
    main()
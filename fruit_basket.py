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
        if (each_row[2] and each_row[3]) or (each_row[3] and each_row[2]) not in fruit_style:
            fruit_style[each_row[2] + ", " + each_row[3]] = each_row[0]
    return fruit_style

# write fruit characteristics
def write_style(fruit_style):
    fruit_styles = ""
    for (key, value) in fruit_style.items():
        fruit_styles += str(key) + ": " + str(value) + "\n"
    return fruit_styles

# check fruit age
def check_age(rows):
    old_fruit = []
    for each_row in rows:
        if each_row[1] > str(3):
            old_fruit.append(each_row)
    return old_fruit

# map old fruit to their counts
def check_type_age(old_fruit):
    type_ages = {}
    for each_row in old_fruit:
        if each_row[0] not in type_ages:
            type_ages[each_row[0]] = 1
        else:
            type_ages[each_row[0]] = type_ages[each_row[0]] + 1

    return type_ages

# write fruit ages
def write_ages(type_ages):
    fruit_ages = ""
    fruit_ages += ", ".join("{1} {0}".format(key, val) for key, val in type_ages.items())
    return fruit_ages

def main():
    rows = read_file('basket.csv')

    f = open("fruit_metrics.txt", "w+")

    # print total fruit
    f.write(count_fruit(rows) + "\n")

    # print total unique fruit
    f.write(count_fruit_types(map_fruit_types(rows)) + "\n")

    # sort fruits in descending order & print
    f.write(sort_fruit(map_fruit_types(rows)) + "\n")

    # print fruit characteristics
    f.write("These are the characteristics of fruit in the basket:" + "\n")
    f.write(write_style(map_fruit_style(rows)))

    # print fruit age
    f.write("There are " + str(len(check_age(rows))) + " fruits over 3 days old in the basket: ")

    # print types of old fruit
    f.write(write_ages(check_type_age(check_age(rows))))  

    f.close()

    print(map_fruit_style(rows))

if __name__ == "__main__":
    main()
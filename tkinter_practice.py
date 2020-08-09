import csv
from tkinter import *
import tkinter as tk

def get_rows(filename):
    # empty lists for data
    rows = []
    with open(filename) as csvfile:
        basketreader = csv.reader(csvfile)
        # save fruit data
        for each_row in basketreader:
            rows.append(each_row)
    return rows

def make_table(root, rows):
    for i in range(len(rows)):
        for j in range((len(rows[0]))):
            e = Entry(root, width=20, font = ('Arial', 10))
            e.grid(row = i, column = j)
            e.insert(END, rows[i][j])

def on_click():
    f = open("test.txt", "w+")

    f.write("Metrics go here")
    

def main():
    rows = get_rows('basket.csv')
    root = tk.Tk()
    b = tk.Button(root, text = "GET METRICS", width = 20, command = on_click)
    root.title("Fruit Basket")
    r = make_table(root, rows)
    b.grid(row = 27, column = 1, pady = 20)
    root.mainloop()

if __name__ == "__main__":
    main()
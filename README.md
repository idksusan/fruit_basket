# AAE Programming Exercise

This is a simple application that takes a csv file and returns a graphical representation of the data as well as an analysis of the metrics in a separate text file.

## Dependencies and Usage

This application uses a number of built-in Python modules including: `csv`, `tkinter`, and `sys`.

To run the application:
1. Open command prompt and navigate to the directory where `fruit_basket.py` is located.
2. To pass filename and run application:
* If file in same directory: type in `python fruit_basket.py <filename.csv>`
* IF file NOT IN same directory: type in `python fruit_basket.py <FULL PATH of filename.csv>`
3. Upon pressing enter, a window will pop up with a graph representation of the data in the csv. 
4. Press the button labeled "GET METRICS" and a text file will appear in the same directory with the analyzed metrics.

## Personal Reflections

I very much appreciated the challenge of this exercise. Being a stranger to Python, I learned a lot about the language and how scripting languages differ from strict programming languages. The flexibility of Python was both enjoyable and a challenge, as I am used to the explicit declarations of Java, but I think I have gained an appreciation for simplicity.

In structuring the application code, I did my best to adhere to the Single Responsibility Principle and made each function to have at most one task. If given more time, I would have liked to add testing and more sophistication in the GUI. 
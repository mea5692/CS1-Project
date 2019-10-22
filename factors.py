"""
File: factors.py
Description: Computes one measure of the effect that income category and
geographical region have on life expectancy, using turtle graphics to produce a
visualization of this data.
Name: Matt Agger
"""

# Import utils and turtle

from ranking import *

import turtle as t

# Define functions and procedures

def choose_color(num):
    """
    Changes the turtle's pen color based on the given number.
    :param num: the number being called.
    :return: None.
    """
    if num == 0:
        t.pencolor("red")
    elif num == 1:
        t.pencolor("orange")
    elif num == 2:
        t.pencolor("yellow")
    elif num == 3:
        t.pencolor("green")
    elif num == 4:
        t.pencolor("blue")
    elif num == 5:
        t.pencolor("indigo")
    else:
        t.pencolor("violet")

def choose_income(num):
    """
    Returns an income category based on the given number.
    :param num: the number being called.
    :return: an income category in the form of a string.
    """
    if num == 0:
        return "Low income"
    elif num == 1:
        return "Upper middle income"
    elif num == 2:
        return "Lower middle income"
    else:
        return "High income"

def choose_region(num):
    """
    Returns a region based on the given number.
    :param num: the number being called.
    :return: a region in the form of a string.
    """
    if num == 0:
        return "Sub-Saharan Africa"
    elif num == 1:
        return "South Asia"
    elif num == 2:
        return "Europe & Central Asia"
    elif num == 3:
        return "Latin America & Caribbean"
    elif num == 4:
        return "Middle East & North Africa"
    elif num == 5:
        return "North America"
    else:
        return "East Asia & Pacific"

def init_legend(title):
    """
    Initializes the turtle window by drawing the legend for the graph.
    :param title: the title of the turtle window.
    :post: the appropriate legend is drawn based on the given title.
    :return: None.
    """
    if title == "Income Category":
        for i in range(4):
            choose_color(i)
            t.write(choose_income(i), font=("Arial", 10, "bold"))
            t.fd(200)
            t.down()
            t.fd(50)
            t.up()
            t.setpos(-235, 295 - (i * 15))
    else:
        for i in range(7):
            choose_color(i)
            t.write(choose_region(i), font=("Arial", 10, "bold"))
            t.fd(200)
            t.down()
            t.fd(50)
            t.up()
            t.setpos(-235, 295 - (i * 15))

def init_graph(title):
    """
    Initializes the turtle window by resetting it, setting its size and title,
    and drawing the axes, labels, values, and legend for the graph.
    :param title: the title of the turtle window.
    :post: the appropriate turtle window title and legend are set and drawn,
           respectively, based on the given title.
    :return: None.
    """
    t.reset()
    t.setup(700, 700)
    t.title("Life Expectancy versus " + title)
    t.up()
    t.setpos(-250, -290)
    t.down()
    t.setpos(300, -290)
    t.up()
    t.setpos(305, -315)
    t.write(2015, align="center", font=("Arial", 10, "bold"))
    t.setpos(30, -330)
    t.write("Year", align="center", font=("Arial", 10, "bold"))
    t.setpos(-245, -315)
    t.write(1960, align="center", font=("Arial", 10, "bold"))
    t.setpos(-250, -290)
    t.down()
    t.setpos(-250, 250)
    t.up()
    t.setpos(-275, 245)
    for i in range(10):
        t.write(90 - (i * 10), font=("Arial", 10, "bold"))
        t.setpos(-275, 185 - (i * 60))
    t.setpos(-315, -25)
    t.write("Life\nExp.", align="center", font=("Arial", 10, "bold"))
    t.setpos(-235, 310)
    t.pensize(2)
    init_legend(title)

def median_life_exp(data, year):
    """
    Computes the median life expectancy of the countries in a given data tuple
    for a specified year.
    :param data: the data tuple being analyzed.
    :param year: the year being referenced.
    :return: the median life expectancy.
    """
    ranking_sdata = sorted_ranking_data(data, year)
    if ranking_sdata == []:
        return None
    i = len(ranking_sdata) // 2
    if len(ranking_sdata) % 2 == 0:
        return (ranking_sdata[i].value + ranking_sdata[i - 1].value) / 2
    else:
        return ranking_sdata[i].value

def plot_graph(title, data):
    """
    Plots the graph for the median life expectancies of either various income
    categories or various regions throughout the 1960-2015 time frame.
    :param title: the title of the turtle window.
    :param data: the data tuple being plotted.
    :pre: the turtle window is initialized.
    :post: the appropriate graph is drawn based on the given title.
    :return: None.
    """
    if title == "Income Category":
        for i in range(4):
            income_fdata = filter_income(data, choose_income(i))
            medianLifeExp = median_life_exp(income_fdata, 1960)
            t.setpos(-250, -290)
            choose_color(i)
            if medianLifeExp is not None:
                t.setpos(-250, (medianLifeExp * 6) - 290)
            t.down()
            for year in range(1961, 2016):
                medianLifeExp = median_life_exp(income_fdata, year)
                if medianLifeExp is not None:
                    t.setpos(((year - 1960) * 10) - 250,
                             (medianLifeExp * 6) - 290)
            t.up()
    else:
        for i in range(7):
            region_fdata = filter_region(data, choose_region(i))
            medianLifeExp = median_life_exp(region_fdata, 1960)
            t.setpos(-250, -290)
            choose_color(i)
            if medianLifeExp is not None:
                t.setpos(-250, (medianLifeExp * 6) - 290)
            t.down()
            for year in range(1961, 2016):
                medianLifeExp = median_life_exp(region_fdata, year)
                if medianLifeExp is not None:
                    t.setpos(((year - 1960) * 10) - 250,
                             (medianLifeExp * 6) - 290)
            t.up()

def main():
    """
    Reads the data and metadata files, initializes the graph for the income
    categories on the turtle window, plots the graph for the income categories
    on the turtle window, prompts the user to hit enter to continue,
    initializes the graph for the regions on the turtle window, and plots the
    graph for the regions on the turtle window.
    :return: None.
    """
    data = read_data("worldbank_life_expectancy")
    title = "Income Category"
    init_graph(title)
    plot_graph(title, data)
    input("Hit enter to continue...")
    title = "Region"
    init_graph(title)
    plot_graph(title, data)
    t.done()

# Run program code

if __name__ == '__main__':
    main()
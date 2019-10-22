"""
File: drop.py
Description: Identifies the ten worst drops in life expectancy throughout the
1960-2015 time frame, only filtering the data to remove non-country (larger
grouping) entries.
Name: Matt Agger
"""

# Import utils

from utils import *

# Define functions and procedures

def sorted_drop_data(data):
    """
    Finds the largest drops in life expectancies for the countries in a given
    data tuple, creates a Range structure for each country and its largest life
    expectancy drop info, appends them to a list, and sorts the list in
    ascending order (based on the change in life expectancy from the first
    value of a Range structure to its second value).
    :param data: the data tuple being sorted.
    :pre: countries that do not contain data for at least two years are not
          considered.
    :return: a list of Range structures, sorted in ascending order.
    """
    drop_data = []
    for key1 in data[0].country_data:
        if len(data[0].country_data[key1]) < 2:
            continue
        country = data[0].countries[key1]
        year1 = 0
        year2 = 0
        value1 = -100.0
        value2 = 0.0
        maxYr = 0
        maxVal = 0.0
        for key2 in data[0].country_data[key1]:
            if data[0].country_data[key1][key2] >= maxVal:
                maxYr = key2
                maxVal = data[0].country_data[key1][key2]
            else:
                if data[0].country_data[key1][key2] - maxVal \
                        <= value2 - value1:
                    year1 = maxYr
                    year2 = key2
                    value1 = maxVal
                    value2 = data[0].country_data[key1][key2]
        if year1 == 0:
            previousYr = 0
            previousVal = 0
            for key2 in data[0].country_data[key1]:
                currentYr = key2
                currentVal = data[0].country_data[key1][key2]
                if currentVal - previousVal <= value2 - value1:
                    year1 = previousYr
                    year2 = currentYr
                    value1 = previousVal
                    value2 = currentVal
                previousYr = currentYr
                previousVal = currentVal
        drop_data.append(Range(country, year1, year2, value1, value2))
    return sorted(drop_data, key=range_value_drop)

def main():
    """
    Reads the data and metadata files and prints the top ten worst life
    expectancy drops in the 1960-2015 time frame including the starting year
    with its value and the ending year with its value.
    :return: None.
    """
    data = read_data("worldbank_life_expectancy")
    region_fdata = filter_region(data, "all")
    income_fdata = filter_income(region_fdata, "all")
    drop_sdata = sorted_drop_data(income_fdata)
    print("Worst life expectancy drops: 1960 to 2015")
    for i in range(10):
        print(str(i + 1) + ": " + drop_sdata[i].country + " from",
              drop_sdata[i].year1, "(" + str(drop_sdata[i].value1) + ") to",
              drop_sdata[i].year2, "(" + str(drop_sdata[i].value2) + "):",
              drop_sdata[i].value2 - drop_sdata[i].value1)

# Run program code

if __name__ == '__main__':
    main()
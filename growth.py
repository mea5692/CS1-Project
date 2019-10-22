"""
File: growth.py
Description: Ranks countries by absolute growth in life expectancy over a
specified range of years, potentially filtering the data to consider only a
particular region and/or income category.
Name: Matt Agger
"""

# Import utils

from utils import *

# Define functions and procedures

def sorted_growth_data(data, year1, year2):
    """
    Creates CountryValue structures for the countries in a given data tuple and
    their life expectancy growths in a specified range of years, appends them
    to a list, and sorts the list in descending order (highest to lowest).
    :param data: the data tuple being sorted.
    :param year1: the starting year being referenced.
    :param year2: the ending year being referenced.
    :pre: countries that do not contain data for both the specified starting
          and ending year are not included in the sorted list.
    :return: a list of CountryValue structures, sorted in descending order.
    """
    growth_data = []
    if data is None:
        return growth_data
    for key in data[0].country_data:
        if year1 in data[0].country_data[key] \
                and year2 in data[0].country_data[key]:
            country = data[0].countries[key]
            value = data[0].country_data[key][year2] \
                    - data[0].country_data[key][year1]
            growth_data.append(CountryValue(country, value))
    return sorted(growth_data, key=country_value, reverse=True)

def main():
    """
    Reads the data and metadata files; prompts the user to enter a starting
    year of interest (or -1 to quit), an ending year of interest (or -1 to
    quit) a region, and an income category; prints the top ten life expectancy
    growths in the filtered data for that year range; prints the bottom ten
    life expectancy growths in the filtered data for that year range; and
    repeats the process again.
    :return: None.
    """
    data = read_data("worldbank_life_expectancy")
    year1 = int(input("Enter starting year of interest (-1 to quit): "))
    while year1 != -1:
        if year1 < 1960 or year1 > 2014:
            print("Valid starting years are 1960-2014")
        else:
            year2 = int(input("Enter ending year of interest (-1 to quit): "))
            if year2 == -1:
                break
            elif year2 <= year1 or year2 > 2015:
                print("Valid ending years are " + str(year1 + 1) + "-2015")
            else:
                region = input("Enter region (type 'all' to consider all): ")
                region_fdata = filter_region(data, region)
                if region_fdata is None:
                    print("\'" + region + "\' is not a valid region")
                else:
                    income = input("Enter income category "
                                   "(type 'all' to consider all): ")
                    income_fdata = filter_income(region_fdata, income)
                    if income_fdata is None:
                        print("\'" + income
                              + "\' is not a valid income category")
                    else:
                        growth_sdata = sorted_growth_data(income_fdata,
                                                          year1, year2)
                        print("\nTop 10 Life Expectancy Growth:",
                              year1, "to", year2)
                        for i in range(10):
                            if i == len(growth_sdata):
                                break
                            print(str(i + 1) + ": " + growth_sdata[i].country,
                                  growth_sdata[i].value)
                        print("\nBottom 10 Life Expectancy Growth:",
                              year1, "to", year2)
                        for i in range(-1, -11, -1):
                            if i == -1 - len(growth_sdata):
                                break
                            print(str(i + 1 + len(growth_sdata)) + ": "
                                  + growth_sdata[i].country,
                                  growth_sdata[i].value)
        year1 = int(input("\nEnter year of interest (-1 to quit): "))

# Run program code

if __name__ == '__main__':
    main()
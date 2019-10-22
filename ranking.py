"""
File: ranking.py
Description: Ranks countries by their life expectancy for a particular year,
potentially filtering the data to consider only a particular region and/or
income category.
Name: Matt Agger
"""

# Import utils

from utils import *

# Define functions and procedures

def sorted_ranking_data(data, year):
    """
    Creates CountryValue structures for the countries in a given data tuple and
    their life expectancies in a specified year, appends them to a list, and
    sorts the list in descending order (highest to lowest).
    :param data: the data tuple being sorted.
    :param year: the year being referenced.
    :pre: countries that do not contain data for the specified year are not
          included in the sorted list.
    :return: a list of CountryValue structures, sorted in descending order.
    """
    ranking_data = []
    if data is None:
        return ranking_data
    for key in data[0].country_data:
        if year in data[0].country_data[key]:
            country = data[0].countries[key]
            value = data[0].country_data[key][year]
            ranking_data.append(CountryValue(country, value))
    return sorted(ranking_data, key=country_value, reverse=True)

def main():
    """
    Reads the data and metadata files; prompts the user to enter a year of
    interest (or -1 to quit), a region, and an income category; prints the top
    ten life expectancies in the filtered data for that year; prints the bottom
    ten life expectancies in the filtered data for that year; and repeats the
    process again.
    :return: None.
    """
    data = read_data("worldbank_life_expectancy")
    year = int(input("Enter year of interest (-1 to quit): "))
    while year != -1:
        if year < 1960 or year > 2015:
            print("Valid years are 1960-2015")
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
                    print("\'" + income + "\' is not a valid income category")
                else:
                    ranking_sdata = sorted_ranking_data(income_fdata, year)
                    print("\nTop 10 Life Expectancy for", year)
                    for i in range(10):
                        if i == len(ranking_sdata):
                            break
                        print(str(i + 1) + ": " + ranking_sdata[i].country,
                              ranking_sdata[i].value)
                    print("\nBottom 10 Life Expectancy for", year)
                    for i in range(-1, -11, -1):
                        if i == -1 - len(ranking_sdata):
                            break
                        print(str(i + 1 + len(ranking_sdata)) + ": "
                              + ranking_sdata[i].country,
                              ranking_sdata[i].value)
        year = int(input("\nEnter year of interest (-1 to quit): "))

# Run program code

if __name__ == '__main__':
    main()
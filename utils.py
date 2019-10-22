"""
File: utils.py
Description: Contains a set of utilities which includes data structures and
functions used by other program tasks.
Name: Matt Agger
"""

# Import rit_lib

from rit_lib import *

# Define structure types for CountryData, CountryMetadata, CountryValue, Range

CountryData = struct_type("CountryData",
                   (dict, 'countries'),
                   (dict, 'country_data'))

CountryMetadata = struct_type("CountryMetadata",
                              (dict, 'regions'),
                              (dict, 'incomes'),
                              (dict, 'special_notes'),
                              (int, 'num_entities'),
                              (int, 'num_countries'))

CountryValue = struct_type("CountryValue",
                           (str, 'country'),
                           (float, 'value'))

Range = struct_type("Range",
                    (str, 'country'),
                    (int, 'year1'),
                    (int, 'year2'),
                    (float, 'value1'),
                    (float, 'value2'))

# Define functions and procedures

def country_value(countryValue):
    """
    Returns the value component of a given CountryValue structure.
    :param countryValue: the CountryValue structure being referenced.
    :return: the value component of countryValue.
    """
    return countryValue.value

def range_value_drop(rangeValues):
    """
    Returns the difference of the value2 and value1 components of a given Range
    structure.
    :param rangeValues: the Range structure being referenced.
    :return: the difference of the value2 and value1 components of rangeValues.
    """
    return rangeValues.value2 - rangeValues.value1

def read_data(filename):
    """
    Reads the data and metadata files under a given filename and stores the
    info from each file in its respective data structure.
    :param filename: the partial name of the data files being read.
    :return: a tuple containing a CountryData structure and a CountryMetadata
             structure.
    """
    file = open("data/" + filename + "_data.txt")
    file.readline()
    countries = {}
    country_data = {}
    for line in file:
        info = line.split(",")
        country_name = info[0]
        country_code = info[1]
        i = 2
        data = {}
        year = 1960
        while year < 2016:
            if info[i] != "":
                data[year] = float(info[i])
            i += 1
            year += 1
        countries[country_code] = country_name
        country_data[country_code] = data
    countryData = CountryData(countries, country_data)
    file.close()
    file = open("data/" + filename + "_metadata.txt")
    file.readline()
    regions = {}
    incomes = {}
    special_notes = {}
    num_entities = 0
    num_countries = 0
    for line in file:
        info = line.split(",", 3)
        country_code = info[0]
        region = info[1]
        income = info[2]
        special_note = info[3].strip("\"\n")
        regions[country_code] = region
        incomes[country_code] = income
        special_notes[country_code] = special_note
        num_entities += 1
        if region != "":
            num_countries += 1
    countryMetadata = CountryMetadata(regions, incomes, special_notes,
                                      num_entities, num_countries)
    file.close()
    return (countryData, countryMetadata)

def filter_region(data, region):
    """
    Filters a given data tuple to only contain countries in a specified region.
    :param data: the data tuple being filtered.
    :param region: the region being used as a filter.
    :pre: entering 'all' as the region will only filter out non-country larger
          groupings.
    :return: a tuple containing a CountryData structure and a CountryMetadata
             structure.
    """
    region_filter = []
    if region == "":
        pass
    elif region == "all":
        for key in data[1].regions:
            if data[1].regions[key] != "":
                region_filter.append(key)
    else:
        for key in data[1].regions:
            if data[1].regions[key] == region:
                region_filter.append(key)
    if region_filter == []:
        return None
    countries = {}
    country_data = {}
    regions = {}
    incomes = {}
    special_notes = {}
    num_entities = 0
    num_countries = 0
    for country_code in region_filter:
        countries[country_code] = data[0].countries[country_code]
        country_data[country_code] = data[0].country_data[country_code]
        regions[country_code] = data[1].regions[country_code]
        incomes[country_code] = data[1].incomes[country_code]
        special_notes[country_code] = data[1].special_notes[country_code]
        num_entities += 1
        num_countries += 1
    countryData = CountryData(countries, country_data)
    countryMetadata = CountryMetadata(regions, incomes, special_notes,
                                      num_entities, num_countries)
    return (countryData, countryMetadata)

def filter_income(data, income):
    """
    Filters a given data tuple to only contain countries in a specified income
    category.
    :param data: the data tuple being filtered.
    :param income: the income category being used as a filter.
    :pre: entering 'all' as the income category will only filter out
          non-country larger groupings.
    :return: a tuple containing a CountryData structure and a CountryMetadata
             structure.
    """
    income_filter = []
    if income == "":
        pass
    elif income == "all":
        for key in data[1].incomes:
            if data[1].incomes[key] != "":
                income_filter.append(key)
    else:
        for key in data[1].incomes:
            if data[1].incomes[key] == income:
                income_filter.append(key)
    if income_filter == []:
        return None
    countries = {}
    country_data = {}
    regions = {}
    incomes = {}
    special_notes = {}
    num_entities = 0
    num_countries = 0
    for country_code in income_filter:
        countries[country_code] = data[0].countries[country_code]
        country_data[country_code] = data[0].country_data[country_code]
        regions[country_code] = data[1].regions[country_code]
        incomes[country_code] = data[1].incomes[country_code]
        special_notes[country_code] = data[1].special_notes[country_code]
        num_entities += 1
        num_countries += 1
    countryData = CountryData(countries, country_data)
    countryMetadata = CountryMetadata(regions, incomes, special_notes,
                                      num_entities, num_countries)
    return (countryData, countryMetadata)

def main():
    """
    Reads the data and metadata files; prints information about the number of
    total entities, total countries, countries in each region, and countries in
    each income category; prompts the user to enter a region and prints the
    countries in that region; prompts the user to enter an income category and
    prints the countries in that income category; and continuously prompts the
    user to enter a country and prints its data until enter is hit to quit.
    :return: None.
    """
    data = read_data("worldbank_life_expectancy")
    print("Total number of entities:", data[1].num_entities)
    print("Number of countries/territories:", data[1].num_countries)
    print("\nRegions and their country count:")
    print("Middle East & North Africa:",
          filter_region(data, "Middle East & North Africa")[1].num_countries)
    print("Europe & Central Asia:",
          filter_region(data, "Europe & Central Asia")[1].num_countries)
    print("North America:",
          filter_region(data, "North America")[1].num_countries)
    print("Latin America & Caribbean:",
          filter_region(data, "Latin America & Caribbean")[1].num_countries)
    print("South Asia:",
          filter_region(data, "South Asia")[1].num_countries)
    print("East Asia & Pacific:",
          filter_region(data, "East Asia & Pacific")[1].num_countries)
    print("Sub-Saharan Africa:",
          filter_region(data, "Sub-Saharan Africa")[1].num_countries)
    print("\nIncome categories and their country count:")
    print("Lower middle income:",
          filter_income(data, "Lower middle income")[1].num_countries)
    print("Upper middle income:",
          filter_income(data, "Upper middle income")[1].num_countries)
    print("High income:",
          filter_income(data, "High income")[1].num_countries)
    print("Low income:",
          filter_income(data, "Low income")[1].num_countries)
    region = input("\nEnter region name: ")
    region_fdata = filter_region(data, region)
    if region_fdata is None:
        print("\'" + region + "\' is not a valid region name")
    else:
        print("Countries in the \'" + region + "\' region:")
        for code in region_fdata[0].countries:
            print(region_fdata[0].countries[code] + " (" + code + ")")
    income = input("\nEnter income category: ")
    income_fdata = filter_income(data, income)
    if income_fdata is None:
        print("\'" + income + "\' is not a valid income category")
    else:
        print("Countries in the \'" + income + "\' income category:")
        for code in income_fdata[0].countries:
            print(income_fdata[0].countries[code] + " (" + code + ")")
    country = input("\nEnter name of country or country code "
                    "(Enter to quit): ")
    while country != "":
        is_valid_country = False
        for key1 in data[0].countries:
            if key1 == country or data[0].countries[key1] == country:
                print("Data for " + country + ":")
                country = key1
                for key2 in data[0].country_data[country]:
                    print("Year:", key2, "\tLife expectancy:",
                          data[0].country_data[country][key2])
                is_valid_country = True
                break
        if not is_valid_country:
            print("\'" + country + "\' is not a valid country name or code")
        country = input("\nEnter name of country or country code "
                        "(Enter to quit): ")

# Run program code

if __name__ == '__main__':
    main()
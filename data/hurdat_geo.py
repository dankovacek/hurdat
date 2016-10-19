
# Atlantic hurricane database (HURDAT2) 1851-2015

## Tropical and Subtropical Cyclone Database Summary

### This dataset (known as Atlantic HURDAT2) has a comma-delimited, text format
### with six-hourly information on the location, maximum winds, central pressure,
### and (beginning in 2004) size of all known tropical cyclones and subtropical
### cyclones. More detailed information can be found on the [NHC website](http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf).


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import json
import string

#f = open('hurdat.csv', 'r')

#Helper Functions

def array_scrub(array):
    scrubbed_array = []
    for e in array:
        value = e.strip()
        if value == '-999':
            scrubbed_array += [""]
        elif value == 'NaN':
            scrubbed_array += [""]
        else:
            scrubbed_array += [value]
    return scrubbed_array

def make_wind_radii_obj(input_array):
    radii_array = array_scrub(input_array)
    # initialize empty object for wind radii extents
    wind_radii_obj = {}
    header = ['34kt', '50kt', '64kt']

    # quadrants follow NE, SE, SW, NW convention
    i = 0
    for head in header:
        wind_radii_obj[head] = make_wind_coords_obj(radii_array[i : i + 4]) 
        i += 4
    return wind_radii_obj
        
def make_wind_coords_obj(input_array):
    header = ['NE', 'SE', 'SW', 'NW']
    wind_coords = {}
    i = 0
    
    for e in header:
        wind_coords[e] = input_array[i]
        i += 1
    return wind_coords

def make_coords_obj(coords):           
    coords_obj = {}
    coords_obj['lat'] = coords[0]
    coords_obj['lon'] = coords[1]
    return coords_obj

def make_date_obj(date):
    date_obj = {}
    date_obj['year'] = date[0:4]
    date_obj['month'] = date[4:6]
    date_obj['day'] = date[-2:]
    return date_obj

hurdat = csv.reader('hurdat.csv')

# create an unordered list of entries from the csv
H_LIST = []

# initialize dictionary object of hurricanes
HC_DICT = {}

# initialize dictionary object for single hurricane entry
hurricane = {'header': 'default_header', 'data': 'default_name'} 

with open('hurdat.csv', 'rb') as csvfile:
    hurdat = csv.reader(csvfile, delimiter=",")
    for row in hurdat:
        clean_row = array_scrub(row)
        H_LIST += [clean_row]

    with open('hurdat_cleaned.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(H_LIST)
        
n = 0

# assemble a dictionary for all historical cyclone events
for i in range(len(H_LIST)):
    
    if len(H_LIST[i]) == 4:
        h_id = H_LIST[i][0]
        
        # initialize entry header as empty dict object
        HC_DICT[h_id] = {}
        HC_DICT[h_id]['name'] = H_LIST[i][1].strip()

        # number of rows of data for the current cyclone record
        num_entries = int(H_LIST[i][2])
        HC_DICT[h_id]['track_entries'] = num_entries
        entry_data = H_LIST[ i + 1 : i + num_entries + 1]
        
        for row in entry_data:
            HC_DICT[h_id]['Date'] = make_date_obj(row[0])
            HC_DICT[h_id]['Time'] = row[1]
            HC_DICT[h_id]['Record Identifier'] = row[2]
            HC_DICT[h_id]['Status of System'] = row[3]
            # coords object input follows lat, lon convention, i.e. Northing, Easting
            HC_DICT[h_id]['Coordinates'] = make_coords_obj(row[4:6])

            max_wind_speed, min_pressure = row[6].strip(), row[7].strip()

            if max_wind_speed == '-999':
                HC_DICT[h_id]['Max. Wind Speed'] = ""
            else:
                HC_DICT[h_id]['Max. Wind Speed'] = max_wind_speed

            if min_pressure == '-999':
                HC_DICT[h_id]['Min. Pressure'] = ""
            else:
                HC_DICT[h_id]['Min. Pressure']= min_pressure
                
            HC_DICT[h_id]['Wind Radii Extents'] = make_wind_radii_obj(row[8:])
            
        # increase the index to jump to the next header row
        i += num_entries

#output and save .json file

with open('result.json', 'w') as fp:
    json.dump(HC_DICT, fp)
     


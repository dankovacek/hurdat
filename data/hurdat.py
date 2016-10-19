
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
    coords_obj['lat'], coords_obj['lon'] = coords[0], coords[1]
    return coords_obj

def make_date_obj(date):
    date_obj = {}
    date_obj['year'] = int(date[0:4])
    date_obj['month'] = int(date[4:6])
    date_obj['day'] = int(date[-2:])
    return date_obj

def convert_latlon_to_decimal(coord):
    # Change coordinate notation to decimal
    # -N, E hemispheres are positive
    # -S, W hemispheres are negative
    
    if coord[-1] == 'N' or coord[-1] == 'E':
        lat_lon = float(coord[:-1])
    else:
        lat_lon = -1 * float(coord[:-1])               
    return lat_lon
    
hurdat = csv.reader('hurdat.csv')

# create an unordered list of entries from the csv
H_LIST = []
# keep separate json list without header rows
H_LIST_JSON = []

# initialize dictionary object of hurricanes
HC_DICT = {}

# initialize dictionary object for single hurricane entry
hurricane = {'header': 'default_header', 'data': 'default_name'}

header_row_titles = ['ID', 'Name', 'Tracks']
data_row_titles = ['Date', 'Time', 'Record Identifier', 'Status of System',
                   'Latitude', 'Longitude', 'Max Sustained Wind [kts]',
                   'Min Pressure [mbars]', '34kt extent NE', '34kt extent SE',
                   '34kt extent SW', '34kt extent NW', '50kt extent NE',
                   '50kt extent SE', '50kt extent SW', '50kt extent NW',
                   '64kt extent NE', '64kt extent SE', '64kt extent SW',
                   '64kt extent NW']

with open('hurdat.csv', 'rb') as csvfile:
    hurdat = csv.reader(csvfile, delimiter=",")
    for row in hurdat:
        clean_row = array_scrub(row)
        # convert lat and lon coordinates to decimal
        if len(row) > 4:            
            clean_row[4] = convert_latlon_to_decimal(clean_row[4])
            clean_row[5] = convert_latlon_to_decimal(clean_row[5])
            H_LIST_JSON += [clean_row]
            H_LIST += [clean_row]
        else:
            # insert column titles for header and data rows
            H_LIST += [header_row_titles]
            H_LIST += [clean_row]
            H_LIST_JSON += [clean_row]
            H_LIST += [data_row_titles]

    with open('hurdat_cleaned.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(H_LIST)

# assemble a dictionary for all historical cyclone events
for i in range(len(H_LIST_JSON)):

    if len(H_LIST_JSON[i]) == 4:
        # get the unique ID of the cyclone
        h_id = H_LIST_JSON[i][0]

        # initialize entry header as empty dict object
        HC_DICT[h_id] = {}
        HC_DICT[h_id]['name'] = H_LIST_JSON[i][1].strip()

        # number of rows of data for the current cyclone record
        num_entries = int(H_LIST_JSON[i][2])
        HC_DICT[h_id]['track_entries'] = num_entries
        entry_data = H_LIST_JSON[ i + 1 : i + num_entries + 1]

        for row in entry_data:
            HC_DICT[h_id]['Date'] += [make_date_obj(row[0])]
            HC_DICT[h_id]['Time'] += [row[1]]
            HC_DICT[h_id]['Record Identifier'] += [row[2]]
            HC_DICT[h_id]['Status of System'] += [row[3]]
            # coords object input follows lat, lon convention, i.e. Northing, Easting
            HC_DICT[h_id]['Coordinates'] += [make_coords_obj(row[4:6])]

            max_wind_speed, min_pressure = row[6].strip(), row[7].strip()

            if max_wind_speed == '-999':
                HC_DICT[h_id]['Max. Wind Speed'] += [""]
            else:
                HC_DICT[h_id]['Max. Wind Speed'] += [float(max_wind_speed)]

            if min_pressure == '-999':
                HC_DICT[h_id]['Min. Pressure'] += [""]
            elif min_pressure:
                HC_DICT[h_id]['Min. Pressure'] += [int(min_pressure)]
            else:
                HC_DICT[h_id]['Min. Pressure'] += ['']

            HC_DICT[h_id]['Wind Radii Extents'] += [make_wind_radii_obj(row[8:])]

        # increase the index to jump to the next header row
        i += num_entries

# output and save .json file

with open('result.json', 'w') as fp:
    json.dump(HC_DICT, fp)



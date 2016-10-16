
# Atlantic hurricane database (HURDAT2) 1851-2015

## Tropical and Subtropical Cyclone Database Summary

### This dataset (known as Atlantic HURDAT2) has a comma-delimited, text format
### with six-hourly information on the location, maximum winds, central pressure,
### and (beginning in 2004) size of all known tropical cyclones and subtropical
### cyclones. More detailed information can be found on the [NHC website](http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf).

Detailed information regarding the Atlantic Hurricane Database Re-analysis Project is available from the Hurricane Research Division.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f = open('hurdat.csv', 'r')

hurdat = pd.read_csv(f)

print hurdat[500:503]
print len(hurdat)



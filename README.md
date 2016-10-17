
# National Hurricane Center - Atlantic hurricane database (HURDAT2)

### Tropical and Subtropical Cyclone Database Summary: 1851 - 2015

![Satellite Image of Hurricane](/images/NASA_hurricane.jpg)
(Photo by Nasa, [from Unsplash](https://unsplash.com/@nasa))

## Context
This dataset (known as Atlantic HURDAT2) contains historical records
on tropical and subtropical cyclones from 1851 to 2015.

## Content
The dataset has a comma-delimited format, featuring location, maximum wind,
central pressure, and size of known tropical and subtropical cyclones.
("Size of cyclone" data is available from 2004 to 2015 only).  The cyclone
data are provided on a 6-hour interval.  The csv data is formatted into two types
of lines (or fields): header and data.  The header rows contain 4 fields,
while the data rows corresponding to the header row follow the header row
and the integer at index 3 location of the header row indicates how many data
rows correspond to the header row.

For ease of implementation with javascript libraries or other web-based applications,
the data have been formatted into a json object.  Details about the json object
structure follow the description of the csv file format.

From the [NHC documentation](http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf):

### CSV - Header Row

Example:
```
AL092011, IRENE, 39,
```
**_AL_** – *Basin*<br>
Atlantic Basin

**_09_** – *ATCF cyclone number for that year*

**_2011_** – *Year*<br>
**_IRENE_** – *Name* - (if available, or else “UNNAMED”)<br>
**_39_** – *Number of best track entries – rows – to follow*<br>

### CSV - Data Field

Example:
```
20110828, 0935, L, TS, 39.4N, 74.4W, 60, 959, 230, 280, 160, 110, 150, 150, 80, 30, 0, 0, 0, 0,
```

**_20110828_** – *Date*<br>
Year, Month, Day as (YYYYMMDD)

**_0935_** – *Time*<br>
Hours and Minutes in UTC (Universal Time Coordinate)

**_L_** – *Record Identifier*
<ul>
<li>C – Closest approach to a coast, not followed by a landfall</li>
<li>G – Genesis</li>
<li>I – An intensity peak in terms of both pressure and wind</li>
<li>L – Landfall (center of system crossing a coastline)</li>
<li>P – Minimum in central pressure</li>
<li>R – Provides additional detail on the intensity of the cyclone when rapid changes are underway</li>
<li>S – Change of status of the system</li>
<li>T – Provides additional detail on the track (position) of the cyclone</li>
<li>W – Maximum sustained wind speed</li>
</ul>

**_TS_** – **Status of system**
<ul>
<li>TD – Tropical cyclone of tropical depression intensity (< 34 knots)</li>
<li>TS – Tropical cyclone of tropical storm intensity (34-63 knots)</li>
<li>HU – Tropical cyclone of hurricane intensity (> 64 knots)</li>
<li>EX – Extratropical cyclone (of any intensity)</li>
<li>SD – Subtropical cyclone of subtropical depression intensity (< 34 knots)</li>
<li>SS – Subtropical cyclone of subtropical storm intensity (> 34 knots)</li>
<li>LO – A low that is neither a tropical cyclone, a subtropical cyclone, nor an extratropical cyclone (of any intensity)</li>
<li>WV – Tropical Wave (of any intensity)</li>
<li>DB – Disturbance (of any intensity)</li>
</ul>

**Location**<br>
**_39.4 N_** – *Latitude and Hemisphere (N or S)*<br>
**_74.4 W_** – *Longitude and Hemisphere (W or E)*

**Max. Wind Speed and Pressure**<br>
**_60_** – *Maximum sustained wind* (in _knots_)<br>
**_959_** – *Minimum Pressure* (in _millibars_)

The cyclone system is described in wind speed zones:

*34 kt (knot) wind radii maximum extents* (in _nautical miles_)<br>
**_230_** – northeastern quadrant<br>
**_280_** – southeastern quadrant<br>
**_160_** – southwestern quadrant<br>
**_110_** – northwestern quadrant

*50 kt (knot) wind radii maximum extents* (in _nautical miles_)<br>
**_150_** – northeastern quadrant<br>
**_150_** – southeastern quadrant<br>
**_80_**  – southwestern quadrant<br>
**_30_** – northwestern quadrant

*64 kt (knot) wind radii maximum extents* (in _nautical miles_)<br>
**_0_** – northeastern quadrant<br>
**_0_** – southeastern quadrant<br>
**_0_** – southwestern quadrant<br>
**_0_** – northwestern quadrant

### JSON Format

The hurricane database has been converted into a json object ('result.json').
The object keys correspond to the unique cyclone identifier(ID), while each ID's
corresponding value is itself an object containing the following fields:
<ul>
    <li>
        <span>**key**</span>
        <span>**value**</span>
    </li>
    <li>
        <span>header</span>
        <span>object: 'name' = hurricane name (if named), 'track entries' = number of measurement tracks</span>
    </li>
    <li>
        <span></span>
    </li>
    <li></li>
    <li></li>
</ul>

## Acknowledgements

[The data](http://www.nhc.noaa.gov/data/#hurdat), and the description above were derived from the [National Hurricane Center Data Archive](http://www.nhc.noaa.gov/data/), and the Center has also provided [more detailed written documentation.](http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf)

From the Documentation:
> "The National Hurricane Center (NHC) conducts a post-storm analysis of each tropical cyclone in its area of responsibility to determine the official assessment of the cyclone's history. This analysis makes use of all available observations, including those that may not have been available in real time. In addition, NHC conducts ongoing reviews of any retrospective tropical cyclone analyses brought to its attention, and on a regular basis updates the historical record to reflect changes introduced via the Best Track Change Committee (Landsea et al. 2004a, 2004b, 2008, 2012, Hagen et al. 2012,)"

-Chris Landsea, James Franklin, and Jack Beven – May 2015


## License

### CC0 1.0 Universal (CC0 1.0) - Public Domain Dedication

See the [NHC disclaimer](http://www.weather.gov/disclaimer) for more information
regarding appropriate use.

## Past Research

Analysis and Visualizations that have used the Hurdat data:
<ol>
<li><a href="https://www.computer.org/csdl/proceedings/itng/2011/4367/00/4367a072-abs.html">Interactive Visualization and Analysis of Hurricane Data</a></li>
<li><a href="https://svs.gsfc.nasa.gov/cgi-bin/search.cgi?dataset=281">Scientific Visualization Studio</a></li>
<li><a href="https://www.r-bloggers.com/generating-hurricanes-with-a-markov-spatial-process/">Generating Hurricanes with a Markov Spatial Process</a></li>
</ol>

## Inspiration

This dataset represents over a century and a half of work in measuring and
tracking cyclones.  The [D3 javascript library](https://d3js.org/) has numerous examples of ways to
represent geographc data, and this dataset seems well suited to create a meaningful
visualization of historical landfall sites in the coastal US.  Perhaps a [chloropleth](http://bl.ocks.org/mbostock/4060606)
could illustrate the most common landfall locations?

Are there any discernible trends in cyclone intensity, frequency, duration,
size, or path over time?  How about for specific locations with the
highest landfall frequency?

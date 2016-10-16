
# National Hurricane Center - Atlantic hurricane database (HURDAT2)

### Tropical and Subtropical Cyclone Database Summary - 1851-2015

![Satellite Image of Hurricane](/images/NASA_hurricane.jpg)

## Context
This dataset (known as Atlantic HURDAT2) contains historical records
on tropical and subtropical cyclones from 1851 to 2015.

## Content
The dataset has a comma-delimited format, featuring location, maximum wind,
central pressure, and size of known tropical and subtropical cyclones.
("Size of cyclone" data is available from 2004 to 2015 only).  The cyclone
data are provided on a 6-hour interval.  The data is formatted into two types
of lines (or fields): header and data.

From the [NHC documentation](http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf):

### Header Field

Example:
```
AL092011, IRENE, 39,
1234567890123456789012345768901234567
```
*Basin* – _AL_
Atlantic Basin

_09_ – *ATCF cyclone number for that year*
_2011_ – *Year*
_IRENE_ – *Name* - (if available, or else “UNNAMED”)
_39_ – *Number of best track entries – rows – to follow*

### Data Field

Example:
```
20110828, 0935, L, TS, 39.4N, 74.4W, 60, 959, 230, 280, 160, 110, 150, 150, 80, 30, 0, 0, 0, 0,
123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
```
_20110828_ – *Date*
Year, Month, Day as (YYYYMMDD)

_0935_ – *Time*
Hours and Minutes in UTC (Universal Time Coordinate)

_L_ – *Record Identifier*
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

_TS_ – *Status of system*
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

*Location*
_39.4 N_ – *Latitude and Hemisphere (N or S)*
_74.4 W _ – *Longitude and Hemisphere (W or E)*

*Max. Wind Speed and Pressure*
_60_ – *Maximum sustained wind* (in _knots_)
_959_ – *Minimum Pressure* (in _millibars_)

The cyclone system is described in wind speed zones:

*34 kt (knot) wind radii maximum extents* (in _nautical miles_)
_230_ – northeastern quadrant
_280_ – southeastern quadrant
_160_ – southwestern quadrant
_110_ – northwestern quadrant

*50 kt (knot) wind radii maximum extents* (in _nautical miles_)
_150_ – northeastern quadrant
_150_ – southeastern quadrant
_80_  – southwestern quadrant
_30_ – northwestern quadrant
_0_ (Spaces 98-101, before 16th comma) – 64 kt wind radii maximum extent in northeastern quadrant (in nautical miles)
_0_ (Spaces 104-107, before 17th comma) – 64 kt wind radii maximum extent in southeastern quadrant (in nautical miles)
_0_ (Spaces 110-113, before 18th comma) – 64 kt wind radii maximum extent in southwestern quadrant (in nautical miles)
_0_ (Spaces 116-119, before 19th comma) – 64 kt wind radii maximum extent in northwestern quadrant (in nautical miles)

## Acknowledgements

[The data](http://www.nhc.noaa.gov/data/#hurdat), and the description above were derived from the [National Hurricane
Center Data Archive](http://www.nhc.noaa.gov/data/), and the Center has also provided [more detailed written documentation.](http://www.nhc.noaa.gov/data/hurdat/hurdat2-format-atlantic.pdf)

From the Documentation:
```
"The National Hurricane Center (NHC) conducts a post-storm analysis of each tropical cyclone in its area of responsibility to determine the official assessment of the cyclone's history. This analysis makes use of all available observations, including those that may not have been available in real time. In addition, NHC conducts ongoing reviews of any retrospective tropical cyclone analyses brought to its attention, and on a regular basis updates the historical record to reflect changes introduced via the Best Track Change Committee (Landsea et al. 2004a, 2004b, 2008, 2012, Hagen et al. 2012,)"

-Chris Landsea, James Franklin, and Jack Beven – May 2015
```

## License

### CC0 1.0 Universal (CC0 1.0) - Public Domain Dedication

See the [NHC disclaimer](http://www.weather.gov/disclaimer) for more information
regarding appropriate use.

## Past Research

In brief, what other analysis has been done on this data?

## Inspiration

Why is this dataset worthy of further analysis?
What questions would you like answered by the community?
What feedback would be helpful on the data itself?

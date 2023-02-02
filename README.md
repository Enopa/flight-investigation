# Flight Investigation Challenge

Within this repository you will find my attempt at the flight hourly volume exam.

My attempt was conducted within a python virtual environment. If you wish to test any of the files, please ensure your start the environment. To do so please clone the files, and then within command line, locate the files and type 

```Scripts\activate```

This will activate the virtual environment giving you access to the necessary libraries

There are several important files within this repository with different purposes. 

### taskOne.py
This is a python file that can be run within command line using 
``` python taskOne.py ```
This program utilises the OpenSky API to download all of the flight data from Heathrow in 2018.
This flight data will be logged in the **2018_Departures_Arrivals_Heathrow.csv** file. This file can be opened in Microsoft Excel or any spreadsheet formatting software of your choice. 

## taskTwo.py
This is the second python file responsible for caclulating hourly frequencies within the 2019 flight data file sent to me in the challenge (**airport_EGLL_2019_flights**). To run this file please type in the command line:
```python taskTwo.py```
This program will output two things. In the command line a frequency table for the hourly data and a bar chart for this table. Images for both outputs can be found within the repository titled (**2019_Table_Frequencies.png** and **2019_Bar_Frequencies.png**)

## Report.pdf
This is a pdf file documenting my development and analysis for the two aforementioned tasks. This file can be opened in any pdf viewer of your choosing.


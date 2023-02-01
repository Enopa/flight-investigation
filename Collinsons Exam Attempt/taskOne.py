from opensky_api import OpenSkyApi
import requests
import sys

#Empty arrays that will hold our outputs
departure_response = []
arrivals_response = []

#Creating two variables begin time and end time, these are the beginning and end of the last week in december
begin_time = 1514160000
end_time = 1514764800


#Output files
output = open("2018_Departures_Arrivals_Heathrow.csv", "w")
output.write("icao24, firstSeen, estDepartureAirport, lastSeen, estArrivalAirport, callsign, estDepartureAirportHorizDistance, estDepartureAirportVertDistance, estArrivalAirportArrivalHorizDistance, estArrivalAirportArrivalVertDistance, departureAirportCandidatesCount, arrivalAirportCandidatesCount, type \n")

#The range indicates the number of days within the year 2018
for i in range(52):
    #We add 604,800 to each time value as that is equivalent to 7 days, the maximum the api allows us to retrieve
    begin_time += 604800
    end_time += 604800
    #URLs are parsed with calculated beginning and end times as well as the icao string for Heathrow
    arrivals_url = "https://opensky-network.org/api/flights/arrival?airport=EGLL&begin="+ str(begin_time) + "&end=" + str(end_time)  
    departures_url = "https://opensky-network.org/api/flights/departure?airport=EGLL&begin="+ str(begin_time) + "&end=" + str(end_time)  
    arrive_request = requests.get(arrivals_url)
    depart_request = requests.get(departures_url)

    arrive = arrive_request.json()
    depart = depart_request.json()


    #Outputting these results to a seperate CSV file
    for a in range(len(arrive)):
        output.write(", ".join(repr(b) for b in arrive[a].values()) + ", arrivals" + "\n")

    for c in range(len(depart)):
        output.write(", ".join(repr(d) for d in depart[c].values()) + ", departures" + "\n")

output.close()


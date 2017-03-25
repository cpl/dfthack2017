<div style="text-align:center">
    <img src ="https://i.imgur.com/NOj41XM.png"/>
</div>
</br></br></br>

Reading Busses API Guide
===
###### Making APIs great again.
---

### GET API Documentation

```
/api&key=
```
Lists documentation for the top level API calls
```
/api&key=/trip
```
Lists documentation for the trip based API calls.
### Listing trips
```
/api&key=/trip/all
```
Lists all of the trips currently in progress
```
/api&key=/trip/all&asof=
```
Lists all trips that were in progress at the provided time
```
/api&key=/trip&route=((&scheduled_time=|&actual_time=)[&stop=]|&tripId)
```
Documentation of sub options and available data, and tripId
```
/api&key=/trip/location[&time=|&timefrom=[&timeto=]]
```
Current location of the bus, and last accurate timestamp.
If time ranges provided, provide for that time.
```
/api&key=/trip/location/all
```
Equivilent to `/api&key=/trip/location&timefrom=${mindate}&timeto=${now}`
```
/api&key=/trip/expectedTimes[&stop=]
```
Provides a full list of when this bus is expected at each stop, or a given stop.
```
/api&key=/trip/driver&key=
```
Provides a link to the driver main call (/api&key=/driver&driverId=) for the relavent driver
```
/api&key=/trip/bus
```
Provides a link to the bus main call (/api&key=/bus&busId=)
```
/api&key=/trip/route
```
Provides a link back to this busses route `/api&key=/route&routeId=`
```
### Listing stops
/api&key=/stop(&stopId|&stopName)
```
Documentation of sub calls to stop
```
/api&key=/stop/all
```
A list of all the stops available
```
/api&key=/stop/nearest&latitude=&longitude=[&limit=]
```
Provides a listing of nearby stops (nice to have)
```
/api&key=/stop&stopId=/location
```
The coordinates of the bus-stop, future sub calls can find additional information on how to find this
```
/api&key=/stop/arrivals&from=&to=[&route=]
```
List of links to trips
```
/api&key=/stop/routes
```
List of all routes that ever service this stop
```
/api&key=/stop/journey&stopId=
```
Provides the time, and link to trip(s) to get to the target stop from here. Initially only handles direct routes.
### Listing routes
```
/api&key=/route/
```
Documentation of sub calls
```
/api&key=/route/all
```
List of all regually scheduled routes (sensitive to the current week)
```
/api&key=/route&routeId=/stops
```
List of all stops in the given route, as links
```
/api&key=/route&routeId=/stats[&since=]
```
Public domain stats on reliability and punctuality of the bus route
```
/api&key=/route&routeId=/trips[&before=]&limit=
```
All trips along this bus route
```
/api&key=/route&routeId=/timetable/all[&asof=]
```
A weeks timetable, relevant to the specified week
```
/api&key=/route&routeId=/timetable&timetableId=/stats&since=
```
Statistics for the running of a particular timetabled route
```
/api&key=/route&routeId=/timetable&timetableId=/trips[&before=]&limit=
```
Lists links to trips on this timetabled route, before a given timestamp

### Listing disruptions
```
/api&key=/disruptions/
```
Human readable major events currently in progress, with links to relavent items. Very open ended includeing sub options.
### Listing buses
```
/api&key=/bus/
```
Documentation of bus sections
```
/api&key=/bus&busId=&key=/remainingFuleEstimate
```
Examples of internal statistics, or parter shareing calls per bus
```
/api&key=/bus/all
```
List of all busses as links
```
/api&key=/bus/trip
```
Returns a link to the currently in progress trip
```
/api&key=/bus/all/greenUpgrade[&route=]
```
Reporting statistics example for fleet improvement
### Listing drivers
```
/api&key=/driver&key=
```
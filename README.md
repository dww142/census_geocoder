US Census Geocoder is a python wrapper to some of the functionality in the US Census Bureau Geocoding webservice.  

https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html  

Basic usage:  
```
import census_geocoder
import json


test_address = {
    'street' : '1600 Pennsylvania Avenue',
    'city' : 'Washington',
    'state' : 'DC',
    # 'zip' : '20500', zip is optional 
}
my_geocoder = census_geocoder.Geocoder(
    street = test_address['street'], 
    city = test_address['city'],
    state = test_address['state'],
    # zip_code = test_address['zip'], ### zip is optional
    # layers = ['14', '16', '18', '54', '56', '58'], ### default layers included in geography output for a geocoded address; 
    # layers = ['86'] ### if you only wanted counties in the .geographies object
    layers = census_geocoder.ALL_AVAILABLE_LAYERS, ### shortcut to get all available layers - 
)

# print(my_geocoder.available_geography_layers()) ### print all available layers from settings

my_geocoder.geocode() # call the geocoding services; 

print(my_geocoder.matched_address, my_geocoder.latitude, my_geocoder.longitude, '\n')
print(json.dumps(my_geocoder.geographies, indent=4))
```

output:  
```
1600 PENNSYLVANIA AVE NW, WASHINGTON, DC, 20500 38.898754 -77.03535 

{
    "Census Tracts GEOID": "11001980000",
    "Census Tracts": "Census Tract 9800",
    "Census Block Groups GEOID": "110019800001",
    "Census Block Groups": "Block Group 1",
    "Unified School Districts GEOID": "1100030",
    "Unified School Districts": "District of Columbia Public Schools",
    "County Subdivisions GEOID": "1100150000",
    "County Subdivisions": "Washington city",
    "Incorporated Places GEOID": "1150000",
    "Incorporated Places": "Washington city",
    "Census Divisions GEOID": "5",
    "Census Divisions": "South Atlantic Division",
    "Census Regions GEOID": "3",
    "Census Regions": "South Region",
    "Combined Statistical Areas GEOID": "548",
    "Combined Statistical Areas": "Washington-Baltimore-Arlington, DC-MD-VA-WV-PA CSA",
    "Metropolitan Divisions GEOID": "4790047894",
    "Metropolitan Divisions": "Washington-Arlington-Alexandria, DC-VA-MD-WV Metro Division",
    "Metropolitan Statistical Areas GEOID": "47900",
    "Metropolitan Statistical Areas": "Washington-Arlington-Alexandria, DC-VA-MD-WV Metro Area",
    "States GEOID": "11",
    "States": "District of Columbia",
    "Counties GEOID": "11001",
    "Counties": "District of Columbia"
}
```


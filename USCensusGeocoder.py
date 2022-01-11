'''
Python wrapper for the US Census Bureau Geocoding webservice.

Documentation:
http://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf

TODO: Separate 'Set address' from init, allow print available layers before
    setting address
TODO: Move option to set geography layers out of init (to the geocode function ?)
TODO: Make getting geography layers optional..? for performance when looking for lat/long only
'''
import json
import requests
import Settings

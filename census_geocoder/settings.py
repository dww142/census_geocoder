"""
A wrapper module for accessing the US Census Bureau's Geocoding API

Benchmarks and Vintages:
    The benchmark is the time period when we created a snapshot of our data
    (generally done twice a year).
    For example, Public_AR_Census2010 is the snapshot we took of the database in 2010.
    Public_AR_Current is the most recent snapshot we took of our dataset. (THIS IS DEFAULT)

    The vintage of geography is the census or survey that the data relates to.
     For example, Census2010_Census2010 are the address ranges from the 2010 Census
        at the time of the 2010 Census.
     You can also obtain the 2010 Census address ranges as of our most recent benchmark.
     The vintages you see available depends on the benchmark you selected.
"""

# required parameters for single address call geocoding (lat/long)
RETURN_TYPE = 'json'
SEARCH_TYPE = 'geographies/address'
# SEARCH_TYPE = 'locations/onelineaddress'
BENCHMARK = 'Public_AR_Current'
#required for geographies
VINTAGE = 'Current_Current'
BASE_URL = f'https://geocoding.geo.census.gov/geocoder/{SEARCH_TYPE}'

FORMAT = 'json'


### pulled from: https://tigerweb.geo.census.gov/ArcGIS/rest/services/TIGERweb/tigerWMS_Current/MapServer
AVAILABLE_LAYERS = {
    # 'all' : 'All Available Layers',
    '0' : 'Census Public Use Microdata Areas',
    '1' : 'Census Public Use Microdata Areas Labels (most recent)',
    '2' : 'Census ZIP Code Tabulation Areas (most recent)',
    '3' : 'Census ZIP Code Tabulation Areas Labels (most recent)',
    '4' : 'Tribal Census Tracts',
    '5' : 'Tribal Census Tracts Labels',
    '6' : 'Tribal Block Groups',
    '7' : 'Tribal Block Groups Labels',
    '8' : 'Census Tracts',
    '9' : 'Census Tracts Labels',
    '10' : 'Census Block Groups',
    '11' : 'Census Block Groups Labels',
    '12' : 'Census Blocks (most recent)',
    '13' : 'Census Blocks Labels (most recent)',
    '14' : 'Unified School Districts',
    '15' : 'Unified School Districts Labels',
    '16' : 'Secondary School Districts',
    '17' : 'Secondary School Districts Labels',
    '18' : 'Elementary School Districts',
    '19' : 'Elementary School Districts Labels',
    '20' : 'Estates',
    '21' : 'Estates Labels',
    '22' : 'County Subdivisions',
    '23' : 'County Subdivisions Labels',
    '24' : 'Subbarrios',
    '25' : 'Subbarrios Labels',
    '26' : 'Consolidated Cities',
    '27' : 'Consolidated Cities Labels',
    '28' : 'Incorporated Places',
    '29' : 'Incorporated Places Labels',
    '30' : 'Census Designated Places',
    '31' : 'Census Designated Places Labels',
    '32' : 'Alaska Native Regional Corporations',
    '33' : 'Alaska Native Regional Corporations Labels',
    '34' : 'Tribal Subdivisions',
    '35' : 'Tribal Subdivisions Labels',
    '36' : 'Federal American Indian Reservations',
    '37' : 'Federal American Indian Reservations Labels',
    '38' : 'Off-Reservation Trust Lands',
    '39' : 'Off-Reservation Trust Lands Labels',
    '40' : 'State American Indian Reservations',
    '41' : 'State American Indian Reservations Labels',
    '42' : 'Hawaiian Home Lands',
    '43' : 'Hawaiian Home Lands Labels',
    '44' : 'Alaska Native Village Statistical Areas',
    '45' : 'Alaska Native Village Statistical Areas Labels',
    '46' : 'Oklahoma Tribal Statistical Areas',
    '47' : 'Oklahoma Tribal Statistical Areas Labels',
    '48' : 'State Designated Tribal Statistical Areas',
    '49' : 'State Designated Tribal Statistical Areas Labels',
    '50' : 'Tribal Designated Statistical Areas',
    '51' : 'Tribal Designated Statistical Areas Labels',
    '52' : 'American Indian Joint-Use Areas',
    '53' : 'American Indian Joint-Use Areas Labels',
    '54' : 'Congressional Districts (most recent)', ### most recent 116
    '55' : 'Congressional Districts Labels', ### most recent  116
    '56' : 'State Legislative Districts - Upper (most recent)', ### most recent 2018
    '57' : 'State Legislative Districts - Upper Labels (most recent)',
    '58' : 'State Legislative Districts - Lower (most recent)',
    '59' : 'State Legislative Districts - Lower Labels (most recent)',
    '60' : 'Census Divisions',
    '61' : 'Census Divisions Labels',
    '62' : 'Census Regions',
    '63' : 'Census Regions Labels',
    '64' : 'Census Urbanized Areas (most recent)',
    '65' : 'Census Urbanized Areas Labels (most recent)',
    '66' : 'Census Urban Clusters (most recent)',
    '67' : 'Census Urban Clusters Labels (most recent)',
    '68' : 'Combined New England City and Town Areas',
    '69' : 'Combined New England City and Town Areas Labels',
    '70' : 'New England City and Town Area Divisions',
    '71' : 'New England City and Town Area Divisions Labels',
    '72' : 'Metropolitan New England City and Town Areas',
    '73' : 'Metropolitan New England City and Town Areas Labels',
    '74' : 'Micropolitan New England City and Town Areas',
    '75' : 'Micropolitan New England City and Town Areas Labels',
    '76' : 'Combined Statistical Areas',
    '77' : 'Combined Statistical Areas Labels',
    '78' : 'Metropolitan Divisions',
    '79' : 'Metropolitan Divisions Labels',
    '80' : 'Metropolitan Statistical Areas',
    '81' : 'Metropolitan Statistical Areas Labels',
    '82' : 'Micropolitan Statistical Areas',
    '83' : 'Micropolitan Statistical Areas Labels',
    '84' : 'States',
    '85' : 'States Labels',
    '86' : 'Counties',
    '87' : 'Counties Labels',
}

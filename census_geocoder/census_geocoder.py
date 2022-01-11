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
import settings

ALL_AVAILABLE_LAYERS = settings.AVAILABLE_LAYERS.keys()

class Geocoder:
    '''
    Default Layers: 
        Unified SD, Sec SD, Elem SD
        , 115th US House Congressional Dist
        , state house upper (senate)
        , state house lower (House)
    '''
    DEFAULT_LAYERS = ['2','14','16','18','54','56','58','60','62','84','86']
    def __init__(self, street, city, state, zip_code=None, layers=DEFAULT_LAYERS):
        '''
        '''
        self.address = {
            'street' : street,
            'city' : city,
            'state' : state,
            }

        if zip_code:
            self.address['zip'] = zip_code

        self.layers = layers
        self.layer_names = [settings.AVAILABLE_LAYERS[l] for l in self.layers]

        self.search_parameters = {
            'benchmark' : settings.BENCHMARK,
            'format' : settings.FORMAT,
            'vintage' : settings.VINTAGE,
            'layers' : ','.join(self.layers)
            }
        # result placeholders
        self.match_found = False
        self.matched_address = None
        self.latitude = None
        self.longitude = None
        self.geographies = {}

    def geocode(self):
        '''
        TODO: TESTS:
        TODO: Check/clean Required options / parameters
        TODO: validate parameters (numeric zip, 2 digit state, non-po box)
        TODO: Handle request call exception
        TODO: Check request call result
        TODO: handle bad JSON exception on JSON.loads
        TODO: result parser for good json (...)
        '''
        request_payload = {**self.address, **self.search_parameters}

        req = requests.get(settings.BASE_URL, params=request_payload)

        if req.ok:
            result = json.loads(req.content)
        else:
            result = json.loads({'result':'NA'})
        # print(json.dumps(result, indent=4))
        self.parse_geocode(result.get('result').get('addressMatches')[0])
        self.parse_geographies(result.get('result').get('addressMatches')[0].get('geographies'))   

    def parse_geocode(self, address_matches):
        '''
        Extract latitude, longitude, and matched address from the Geocoder response
        '''
        if address_matches:
            self.latitude = address_matches.get('coordinates').get('y')
            self.longitude = address_matches.get('coordinates').get('x')
            self.matched_address = address_matches.get('matchedAddress')
    
    def parse_geographies(self, geographies):
        '''
        Extract all requested geography layers from request into a dictionary. 
        '''
        for layer in self.layer_names:
            if geographies.get(layer):
                self.geographies[layer+' GEOID'] = geographies.get(layer)[0].get('GEOID')
                self.geographies[layer] = geographies.get(layer)[0].get('NAME')

    def available_geography_layers(self):
        '''
        Print the lis tof available geography layers 
        '''
        for layer in settings.AVAILABLE_LAYERS:
            print('Layer Name:', settings.AVAILABLE_LAYERS[layer], '; Layer Code:', layer)
        print('Default Layers (& Format):', self.DEFAULT_LAYERS)

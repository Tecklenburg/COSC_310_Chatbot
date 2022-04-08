# based on https://www.youtube.com/watch?v=ckPEY2KppHc

from urllib.parse import urlencode
import requests

class GoogleMapsClient(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    api_key = None
    
    def __init__(self, api_key=None, address=None, *args, **kwargs):
        '''initialize the client'''
        super().__init__(*args, **kwargs)
        if api_key == None:
            raise Exception('API key is required')
        self.api_key = api_key
        self.location_query = address
        if self.location_query != None:
            self.extract_lat_lng()
    
    def extract_lat_lng(self):
        '''extract the lat and lng for the location'''
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"address": self.location_query , "key": self.api_key}
        url_params = urlencode(params)

        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        
        if r.status_code not in range(200, 299):
            return{}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        self.lat, self.lng = latlng.get('lat'), latlng.get('lng')
        return self.lat, self.lng 
    
    def search(self, radius = 10000, keyword='Food'):
        '''search in for the keyword in the area around the given location'''
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        params = {
            'key': self.api_key,
            'location': f"{self.lat}, {self.lng}", 
            'radius': radius,
            'keyword': keyword
            }

        params_encoded = urlencode(params)
        places_endpoint = f"{endpoint}?{params_encoded}"

        r = requests.get(places_endpoint)
        if r.status_code not in range(200, 299):
            return{}
        
        return r.json()
    
    def details(self, place_id):
        '''extract details for the given place like name and address'''
        detail_base_endpoint = f"https://maps.googleapis.com/maps/api/place/details/{self.data_type}"
        detail_params = {
            "place_id": f"{place_id}",
            "fields": "name,rating,formatted_address,url",
            "key": self.api_key
        }
        detail_params_encoded = urlencode(detail_params)
        detail_url = f"{detail_base_endpoint}?{detail_params_encoded}"
        
        r = requests.get(detail_url)
        if r.status_code not in range(200, 299):
            return{}
        else:
            return r.json()
        
    
    
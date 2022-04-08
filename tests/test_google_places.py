import sys
import os
sys.path.append(os.path.abspath('../src'))

import unittest
import json

from google_maps_client import GoogleMapsClient

class TestTranslator(unittest.TestCase):
    
    def setUp(self):
        api_key = ''
        self.client = GoogleMapsClient(api_key=api_key, address='UBCO Kelowna')
        
    def test_lat_lng_correctly_set(self):
        lat = round(self.client.lat, 2)
        lng = round(self.client.lng, 2)
        
        exp_lat = 49.94
        exp_lng = -119.4
        
        self.assertEqual(lat, exp_lat)
        self.assertEqual(lng, exp_lng)
        
    def test_search_returns_json(self):
        results = self.client.search()
        data_type = type(results)
        exp_type = type({})
        
        self.assertEqual(data_type, exp_type)
        
    def test_details_returns_correct_name(self):
        details = self.client.details('ChIJz2iqxn3tfVMRy6JEIWKdTNE')
        name = details['result']['name']
        
        exp_name = 'Koi Sushi'
        
        self.assertEqual(name, exp_name)
        
if __name__ == '__main__':
    unittest.main()
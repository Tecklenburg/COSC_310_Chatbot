import requests
import uuid
import json

def translate(text, src, des, key=None):
    '''translate from src to des using the microsoft translator api, code based on their intro'''
    endpoint = "https://api.cognitive.microsofttranslator.com"
    
    # raise error if key is missing
    if key == None:
        raise Exception('No key supplied')

    # Add your location, also known as region. The default is global.
    # This is required if using a Cognitive Services resource.
    location = "canadacentral"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': src,
        'to': des
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]['translations'][0]['text']
import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
print(params)
r = requests.get(url, params=params)
print(r.json())
results = r.json()['results']
location = results[0]['geometry']['location']
location['lat'], location['lng']
#{u'status': u'REQUEST_DENIED', u'error_message': u'You must use an API key to authenticate each request to Google Maps Platform APIs. For additional information, please refer to http://g.co/dev/maps-no-account', u'results': []}
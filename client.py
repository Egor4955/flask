import requests

# response = requests.get('http://127.0.0.1:5000/advert/8/')
response = requests.post('http://127.0.0.1:5000/advert/',
                         json={'title': 'nice 12',
                               'description': 'weather forecast333333',
                               'owner': 'Gismeteo4545'}
                         )

print(response.status_code)
print(response.text)

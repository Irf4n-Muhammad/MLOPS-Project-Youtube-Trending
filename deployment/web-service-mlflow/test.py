import requests

Trending = {
    'Likes': 50000000,
    'Views': 70000000,
    'Licensed': 'Yes',
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json = Trending)
print(response.json())



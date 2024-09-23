import requests
url_name="https://en.wikipedia.org/wiki/Don_(2006_Hindi_film)"
response=requests.get(url_name)
print(response.status_code)

import requests
url = 'https://example.com/'

response = requests.get(url)

with open('example.html', 'w') as f:
  f.write(response.text)
  
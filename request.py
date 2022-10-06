import requests

# URL
url = 'http://localhost:5001/api/'

# Change the value of experience that you want to test
payload = {
	'exp':6.8
}

r = requests.post(url,json=payload)

print(r.json())

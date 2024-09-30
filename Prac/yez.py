import sys
import pip

try:
    import requests
except ImportError:
    pip.main(['install', 'requests'])
    import requests

response = requests.get("https://api.kanye.rest")
if response.status_code == 200:
    data = response.json()
    quote = data['quote'] + " -Yeezy"
    print(quote)  # Printing only the quote
else:
    print("Error: Unable to fetch data from the API.")

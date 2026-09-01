import requests

url = "https://www.bbc.com/news"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])
import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.bbc.com/news"

# Send a request to the website
response = requests.get(url)

# Check whether the request was successful
print("Status Code:", response.status_code)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

print("HTML content parsed successfully!")
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.nomadicmatt.com/",
]

for url in urls:
    try:
        response = requests.get(url)
        print(f"{url} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"{url} - ERROR: {e}")
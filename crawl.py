import requests
from bs4 import BeautifulSoup
import csv

urls = [
    "https://www.nomadicmatt.com/",
    "https://stackoverflow.com/"
]

for url in urls:
    try: 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #Extract title
        title_tag = soup.title.string.strip() if soup.title else "Missing"

        #Extract meta description
        meta_tag = soup.find("meta", attrs={"name": "description"})
        meta_description = meta_tag["content"].strip() if meta_tag else "Missing"

        # Extract H1 tag
        h1_tag = soup.find("h1")
        h1_text = h1_tag.get_text(strip=True) if h1_tag else "Missing"

        print(f"\n{url}")
        print(f"Status: {response.status_code}")
        print(f"Title: {title_tag}")
        print(f"Meta Description: {meta_description}")
        print(f"H1: {h1_text}")

    except Exception as e:
        print(f"\n{url}")
        print(f"ERROR: {e}")
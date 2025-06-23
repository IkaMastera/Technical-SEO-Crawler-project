import requests
from bs4 import BeautifulSoup
import csv

urls = [
    "https://www.nomadicmatt.com/",
    "https://stackoverflow.com/",
]

results = []

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

        results.append({
            "URL": url,
            "Status Code": response.status_code,
            "Title": title_tag,
            "Meta Description": meta_description,
            "H1": h1_text
        })

    except Exception as e:
        results.append({
            "URL": url,
            "Status Code": "Error",
            "Title": "Error",
            "Meta description": "Error",
            "H1": str(e)
        })

# Write results to a CSV file
with open("seo_audit.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("SEO audit complete: Results saved to seo_audit.csv")
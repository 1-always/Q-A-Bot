import requests 
import BeautifulSoup
import json

urls = [
    "https://learn.salesforcecasts.com/"  # Add all pages you want to crawl
]

data = {}

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove scripts and styles
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator=" ")
    text = ' '.join(text.split())  # basic cleaning
    data[url] = text

# Save raw text
with open("data/raw_text.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Crawling complete!")

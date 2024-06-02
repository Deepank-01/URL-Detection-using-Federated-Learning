from bs4 import BeautifulSoup
import requests

# Function to extract HTML document from the given URL
def getHTMLdocument(url):
    # Request HTML document of the given URL
    response = requests.get(url)
    # Ensure the request was successful
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve HTML:", response.status_code)
        return None

# Assign URL to scrape
url_to_scrape = "https://www.rgipt.ac.in/en/article/home"

# Create document
html_document = getHTMLdocument(url_to_scrape)

if html_document:
    # Create BeautifulSoup object
    soup = BeautifulSoup(html_document, 'html.parser')

    # Find all anchor tags with "href" attributes starting with "https://"
    for link in soup.select('a[href^="https://"]'):
        print(link['href'])
else:
    print("No HTML document retrieved.")

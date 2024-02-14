import requests
from bs4 import BeautifulSoup

def get_links_with_response(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags (links) in the HTML
        links = [a['href'] for a in soup.find_all('a', href=True) if 'https' in a['href'] and 'thunkable' in a['href']]

        # Print the links and their corresponding HTTP response codes
        for link in links:
            try:
                link_response = requests.head(link)
                print(f"Link: {link} | Response Code: {link_response.status_code}")
            except requests.ConnectionError:
                print(f"Link: {link} | Failed to connect")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}. The website may be down or unreachable.")


# Lets check the make it happen website for thunkable links:
website_url = "https://www.makeithappen.club/winners"
get_links_with_response(website_url)

import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from send_email import send_email

def get_links_with_response(url):
    failed_links = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags (links) in the HTML
        links = [(a['href'], a) for a in soup.find_all('a', href=True) if 'https' in a['href'] and 'thunkable' in a['href']]

        # Check the status code of each link
        for link_url, link in links:
            try:
                app_name = link.find_parent('div', class_='list-item-content').find('h2').get_text()
                link_response = requests.head(link_url)
                app_details = f"App Name: {app_name} | Link: {link_url} | | Response Code: {link_response.status_code}"
                print(app_details)
                if link_response.status_code != 200:
                    failed_links.append(app_details)
            except requests.ConnectionError:
                print(f"{app_details} | Failed to connect")
                failed_links.append(f"{app_details} | Failed to connect")
    except requests.ConnectionError:
        print(f"Failed to connect to {url}. The website may be down or unreachable.")

    if failed_links:
        send_email(failed_links)
    else:
        print(f"No failed links!")

# Lets check the make it happen website for thunkable links:
website_url = "https://www.makeithappen.club/winners"
get_links_with_response(website_url)

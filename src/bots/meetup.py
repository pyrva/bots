from urllib.parse import urljoin

import requests

MEETUP_API_URL = 'https://api.meetup.com/'

def events(group: str):
    """Retrieve future events from meetup."""
    url = urljoin(MEETUP_API_URL, f'{group}/events')
    response = requests.get(url)
    return response.json()

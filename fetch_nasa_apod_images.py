import os
import requests
from dotenv import load_dotenv

from process_img import download_img


def fetch_nasa_apod_images():
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/planetary/apod?'
    response = requests.get(url, params={'api_key': nasa_api_key, 'count': 5})
    img_urls = response.json()
    for img_url in img_urls:
        download_img(img_url['hdurl'], 'images')


if __name__ == '__main__':
    load_dotenv()
    fetch_nasa_apod_images()

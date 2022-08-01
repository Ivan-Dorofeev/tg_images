import os
import requests
from dotenv import load_dotenv

from process_img import download_img


def fetch_nasa_apod_images():
    images_count = 5
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/planetary/apod?'
    response = requests.get(url, params={'api_key': nasa_api_key, 'count': images_count})
    response.raise_for_status()
    img_urls = response.json()
    for img_url in img_urls:
        download_img(img_url['hdurl'], 'images')


if __name__ == '__main__':
    fetch_nasa_apod_images()

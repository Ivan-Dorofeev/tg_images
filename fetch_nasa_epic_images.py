import datetime
import os
import requests
from dotenv import load_dotenv

from process_img import download_img


def fetch_nasa_epic_images():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(url, params={'api_key': nasa_api_key, 'date': datetime.datetime.today()})
    response.raise_for_status()
    for image_info in response.json()[:5]:
        date_img = image_info['date'].split(" ")[0].replace('-', '/')
        name_img = '/png/' + image_info['image'] + '.png'
        response_img = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{date_img}{name_img}',
                                    params={'api_key': nasa_api_key})
        response.raise_for_status()
        img_url = response_img.url
        download_img(img_url, 'images')


if __name__ == '__main__':
    fetch_nasa_epic_images()

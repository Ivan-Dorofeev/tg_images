import datetime
import os
import requests
from dotenv import load_dotenv

from process_img import download_img


def fetch_nasa_epic_images():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response_images = requests.get(url, params={'api_key': nasa_api_key, 'date': datetime.datetime.today()})
    response_images.raise_for_status()
    for image in response_images.json()[:5]:
        img_date = image['date'].split(" ")[0].replace('-', '/')
        img_name = '/png/{}.png'.format(image['image'])
        img_response = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{img_date}{img_name}',
                                    params={'api_key': nasa_api_key})
        img_response.raise_for_status()
        img_url = img_response.url
        download_img(img_url, 'images')


if __name__ == '__main__':
    fetch_nasa_epic_images()

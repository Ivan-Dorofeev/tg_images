import os
from urllib.parse import unquote

import requests
from dotenv import load_dotenv


def download_img(url, path_to_save):
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    img_extension, *_ = os.path.splitext(url)[1].split('?')
    img_name, *_ = os.path.split(url)[1].split('.')
    unquote_img_name = unquote(img_name)
    full_img_name = unquote_img_name + img_extension

    filename = os.path.join(path_to_save, full_img_name)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_nasa_apod_images():
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/planetary/apod?'
    response = requests.get(url, params={'api_key': nasa_api_key, 'count': 5})
    img_urls = response.json()
    for img_url in img_urls:
        download_img(img_url['hdurl'], 'images')
    return 'Done!'


if __name__ == '__main__':
    load_dotenv()
    print(fetch_nasa_apod_images())

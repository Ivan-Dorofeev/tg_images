import datetime
import os.path
from dotenv import load_dotenv
import requests
from urllib.parse import unquote


def download_img(url, path_to_save):
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    img_extension = os.path.splitext(url)[1].split('?')[0]
    img_name = os.path.split(url)[1].split('.')[0]
    unquote_img_name = unquote(img_name)
    full_img_name = unquote_img_name + img_extension

    filename = os.path.join(path_to_save, full_img_name)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def spacex_images():
    response = requests.get('https://api.spacexdata.com/v5/launches')
    for i in response.json()[:5]:
        img_url = i['links']['patch']['large']
        download_img(img_url, 'spacex_images')


def nasa_10_img():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/planetary/apod?'
    response = requests.get(url, params={'api_key': nasa_api_key, 'count': 10})
    img_urls = response.json()
    for img_url in img_urls:
        download_img(img_url['hdurl'], 'nasa_images')


def nasa_img_epic():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response_data_list = requests.get(url, params={'api_key': nasa_api_key, 'date': datetime.datetime.today()})
    for img_data in response_data_list.json()[:5]:
        date_and_name_img = img_data['date'].split(" ")[0].replace('-', '/') + '/png/' + img_data['image'] + '.png'
        response_img = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{date_and_name_img}',
                                    params={'api_key': nasa_api_key})
        img_url = response_img.url
        download_img(img_url, 'nasa_images/epic')


if __name__ == '__main__':
    # spacex_images()
    nasa_img_epic()

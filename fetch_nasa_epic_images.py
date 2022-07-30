import datetime
import os
from urllib.parse import unquote

import requests
from dotenv import load_dotenv


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


def nasa_epic_images():
    nasa_api_key = os.environ['NASA_API_KEY']
    url = 'https://api.nasa.gov/EPIC/api/natural'
    response_data_list = requests.get(url, params={'api_key': nasa_api_key, 'date': datetime.datetime.today()})
    for img_data in response_data_list.json()[:5]:
        date_and_name_img = img_data['date'].split(" ")[0].replace('-', '/') + '/png/' + img_data['image'] + '.png'
        response_img = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{date_and_name_img}',
                                    params={'api_key': nasa_api_key})
        img_url = response_img.url
        download_img(img_url, 'images')
    return 'Done!'


if __name__ == '__main__':
    load_dotenv()
    print(nasa_epic_images())

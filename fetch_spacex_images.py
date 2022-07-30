import argparse
import os
from urllib.parse import unquote

import requests


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


def spacex_images(id_launch):
    if id_launch:
        response = requests.get(f'https://api.spacexdata.com/v3/launches/{id_launch}')
        img_url = response.json()['links']['flickr_images'][0]
        download_img(img_url, 'spacex_images')
        return 'Done!'
    else:
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        if not hasattr(response.json()['links'], 'flickr_images'):
            return "Извините, нет фото последнего запуска на сайте"
        else:
            img_url = response.json()['links']['flickr_images'][0]
            download_img(img_url, 'images')
            return 'Done!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинку запуска по ID. Если нет ID качает картинку последнего запуска'
    )
    parser.add_argument(
        '-id', '--id_launch',
        help='ID запуска'
    )
    args = parser.parse_args()
    print(spacex_images(args.id_launch))

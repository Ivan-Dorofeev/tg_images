import argparse
import os
from urllib.parse import unquote

import requests


def download_img(url, path_to_save):
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    img_extension, *_ = os.path.splitext(url)[1].split('?')
    img_name, *_ = os.path.split(url)[1].split('.')
    unquote_img_name = unquote(img_name)
    filename = os.path.join(path_to_save, f'{unquote_img_name}+{img_extension}')

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def spacex_images(id_launch):
    version = 'v5' if id_launch == "latest" else'v3'
    response = requests.get(f'https://api.spacexdata.com/{version}/launches/{id_launch}')
    if 'flickr_images' not in response.json()['links'].keys():
        return "Извините, нет фото"
    else:
        img_url, *_ = response.json()['links']['flickr_images']
        download_img(img_url, 'images')
        return 'Done!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа скачивает картинку запуска по ID. Если нет ID качает картинку последнего запуска'
    )
    parser.add_argument(
        '-id', '--id_launch',
        default='latest',
        help='ID запуска'
    )
    args = parser.parse_args()
    print(spacex_images(args.id_launch))

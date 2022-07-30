import argparse
import requests

from process_img import download_img


def spacex_images(id_launch):
    version = 'v5' if id_launch == "latest" else 'v3'
    response = requests.get(f'https://api.spacexdata.com/{version}/launches/{id_launch}')
    if 'flickr_images' not in response.json()['links'].keys():
        return "Извините, нет фото"
    else:
        img_url, *_ = response.json()['links']['flickr_images']
        download_img(img_url, 'images')


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
    spacex_images(args.id_launch)

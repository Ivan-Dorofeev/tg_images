import os.path

import requests


def download_img(url, path_to_save):
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    name_file_from_url = url.split('/')[-1]
    filename = os.path.join(path_to_save, name_file_from_url)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v5/launches')
    for i in response.json()[:5]:
        img_url = i['links']['patch']['large']
        download_img(img_url, 'img')


if __name__ == '__main__':
    # download_img('https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg', 'images')
    fetch_spacex_last_launch()

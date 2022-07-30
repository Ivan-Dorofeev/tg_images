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

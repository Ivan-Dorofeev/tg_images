import os
from urllib.parse import unquote, urlparse

import requests


def download_img(url, path_to_save):
    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    *_, file_from_url = urlparse(url).path.split('/')
    img_name, img_extension = file_from_url.split('.')
    unquote_img_name = unquote(img_name)
    filepath = os.path.join(path_to_save, f'{unquote_img_name}.{img_extension}')

    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)

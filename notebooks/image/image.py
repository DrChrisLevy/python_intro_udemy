import requests


def get_image_content(image_url):
    image_content = requests.get(url=image_url).content
    return image_content

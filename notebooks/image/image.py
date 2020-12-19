import requests
from PIL import Image
from io import BytesIO


def get_image_content(image_url):
    image_content = requests.get(url=image_url).content
    return image_content


def image_content_to_bytesio(image_content):
    return BytesIO(image_content)


def pillow_image_from_bytesio(bytesio):
    return Image.open(bytesio)


def pil_image_from_url(image_url):
    image_content = get_image_content(image_url)
    bytesio = image_content_to_bytesio(image_content)
    img = pillow_image_from_bytesio(bytesio)
    return img

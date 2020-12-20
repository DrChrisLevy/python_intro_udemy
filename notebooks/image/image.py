import requests
from PIL import Image
from io import BytesIO
import os


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


def download_images(image_urls, folder_path):
    """
    Download images from the web to you local file system.
    :param image_urls: (list) of strings with the image urls.
    :param folder_path: (str) to the folder/path where images are saved/downloaded.
    :return: (list) of dicts with information about each image.
    """
    os.makedirs(folder_path, exist_ok=True)
    image_info = []
    for i, image_url in enumerate(image_urls):
        img = pil_image_from_url(image_url)
        width, height = img.size
        image_format = img.format
        image_path = os.path.join(folder_path, f'{i}.jpg')
        img.save(image_path)
        image_info.append({
            'image_url': image_url,
            'width': width,
            'height': height,
            'format': image_format,
            'file_name': image_path
        })
    return image_info



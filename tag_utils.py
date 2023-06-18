import json

from PIL import Image

import placeholder
from params import XP_COMMENT
from placeholder import Placeholder


def add_comments(image_path, description):
    image = Image.open(image_path)

    exif_data = image.getexif()
    exif_data[XP_COMMENT] = description.encode("utf16")

    image.save(image_path, exif=exif_data)


def get_comment(image_page):
    image = Image.open(image_page)

    exif_data = image.getexif()

    return exif_data[XP_COMMENT].decode('utf16')


def add_placeholders(placeholders):
    placeholders_inner_json = json.dumps(placeholders)
    print(placeholders_inner_json)
    pass

p1 = Placeholder(x=1,y=2, width=3, height=4)
p2 = Placeholder(x=5,y=6, width=7, height=8)
lst = [p1,p2]
add_placeholders(lst)


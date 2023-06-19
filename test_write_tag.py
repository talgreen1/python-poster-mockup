from PIL import Image

from params import PLACEHOLDERS_JSON, XP_COMMENT, PLACEHOLDERS_TEMPLATE, PLACEHOLDERS_TEMPLATE_START, \
    PLACEHOLDERS_TEMPLATE_END
from placeholder import Placeholder

import json


def write_comment(image_path, comment):
    image = Image.open(image_path)
    # XPComment = 0x9C9C
    exifdata = image.getexif()
    exifdata[XP_COMMENT] = comment.encode("utf16")

    image.save(image_path, exif=exifdata)


def get_comment(image_page):
    image = Image.open(image_page)

    # XPComment = 0x9C9C

    exifdata = image.getexif()

    return exifdata[XP_COMMENT].decode('utf16')


def write_placeholders(placeholders: [Placeholder], image_path: str):
    PLACEHOLDERS_JSON['placeholders'] = placeholders
    placeholders_json = json.dumps(PLACEHOLDERS_JSON)

    placeholder_comment = PLACEHOLDERS_TEMPLATE.format(json=placeholders_json)

    write_comment(image_path, placeholder_comment)


def find_placeholders_in_comment_text(comment:str):
    start_index = comment.find(PLACEHOLDERS_TEMPLATE_START)
    if start_index == -1:
        return None

    end_index = comment.find(PLACEHOLDERS_TEMPLATE_END,start_index )
    return comment[start_index+len(PLACEHOLDERS_TEMPLATE_START):end_index ]


test_comment = 'This is some comments.... placeholders:<<{"placeholders": [{"x": 1, "y": 2, "high": 3, "width": 4}, {"x": 5, "y": 6, "high": 7, "width": 8}]}>>'
a = find_placeholders_in_comment_text(test_comment)
print(a)


# p1 = {'x': 1, 'y': 2, 'high': 3, 'width': 4}
# p2 = {'x': 5, 'y': 6, 'high': 7, 'width': 8}
# write_placeholders([p1, p2], None)
# # add_description('./photos/template.jpg', 'New desk')
# # print(get_comment('./photos/template.jpg'))

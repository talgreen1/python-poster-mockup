import os

from PIL import ImageChops
from PIL import Image

from file_utils import get_all_files, create_folder_if_not_exists
from placeholder import Placeholder
from tag_utils import get_placeholders
from os import listdir
from os.path import isfile, join


def insert_image_to_mockup(mock_image_path, insert_image_path, output_image_path, placeholder: Placeholder):
    background_image = Image.open(mock_image_path)
    insert_image = Image.open(insert_image_path)
    insert_image_new_size = (int(placeholder.width), int(placeholder.height))
    insert_image_position = (int(placeholder.x), int(placeholder.y))
    # insert_image_position = (100,0)

    insert_image = insert_image.resize(insert_image_new_size)
    # insert_image_alpha = insert_image.convert("RGBA")
    background_image.paste(insert_image, insert_image_position)
    background_image.save(output_image_path)


def insert_images_to_mockup(mock_image_path, insert_images_path: [str], output_image_path):
    placeholders = get_placeholders(mock_image_path)
    background_image = Image.open(mock_image_path)

    if not insert_images_path:
        return

    for placeholder in placeholders:
        if not insert_images_path:
            break
        insert_image_path = insert_images_path.pop(0)
        insert_image = Image.open(insert_image_path)
        insert_image_new_size = (int(placeholder.width), int(placeholder.height))
        insert_image_position = (int(placeholder.x), int(placeholder.y))

        insert_image = insert_image.resize(insert_image_new_size)
        # insert_image_alpha = insert_image.convert("RGBA")
        background_image.paste(insert_image, insert_image_position)

    create_folder_if_not_exists(output_image_path)
    background_image.save(output_image_path)


def insert_images_to_mockups(mock_images_folder: [str],
                            insert_images_folder: [str],
                            output_image_path: str,
                            output_image_name_template: str,
                            mock_images_folder_scan_recursively: bool = True,
                            insert_images_folder_scan_recursively: bool = True,
                            ):
    mock_images = get_all_files(mock_images_folder, mock_images_folder_scan_recursively)
    insert_images = get_all_files(insert_images_folder, insert_images_folder_scan_recursively)

    for index, mock_image in enumerate(mock_images):
        output_image_full_name = os.path.join(output_image_path, output_image_name_template.format(counter=index+1))
        insert_images_to_mockup(mock_image, insert_images, output_image_full_name)








insert_images_to_mockups('\\\\GreenNas\\Backup\\Etsy\\Mockups Template\\3x4 - With Placeholders\\Babies', './photos/items', './photos/output', '{counter:02d}-Mockup{counter}.jpg')

# Example usage
# background_image_path = './photos/template.jpg'  # Path to the background image
# insert_image_path = './photos/item1.png'  # Path to the image to be inserted (with alpha channel)
# output_image_path = './photos/output.jpg'  # Path to save the resulting image
# new_size = (200, 200)  # New size for the insert image
# insert_position = (100, 100)  # Coordinates to paste the smaller image
# blend_mode = "dissolve"  # Specify the desired blending mode ("dissolve", "transparent", or "normal")
#
# insert_image_to_mockup(background_image_path, insert_image_path, output_image_path, new_size, insert_position,
#                         blend_mode)

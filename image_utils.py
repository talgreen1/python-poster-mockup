from PIL import ImageChops
from PIL import Image

from placeholder import Placeholder
from tag_utils import get_placeholders


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
        # insert_image_position = (100,0)

        insert_image = insert_image.resize(insert_image_new_size)
        # insert_image_alpha = insert_image.convert("RGBA")
        background_image.paste(insert_image, insert_image_position)

    background_image.save(output_image_path)

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

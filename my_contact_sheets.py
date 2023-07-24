from PIL import Image, ImageOps

from file_utils import get_all_files


def create_contact_sheet(images_path, output_size: int = 1000):
    images = get_all_files(images_path)
    contact_sheet = Image.new('RGB', (output_size, output_size), (255, 255, 255))

    rows = 0
    cols = 0

    margin = output_size * 0.1

    if len(images) == 2:
        rows = 1
        cols = 2
    thumb_height = int(output_size / rows - (2 * rows * margin))
    img = Image.open(images[0])
    thumb_width = int(thumb_height * img.width / img.height)
    image_index = 0
    x=0
    for r in range(rows):
        y = (output_size - thumb_height) / 2
        for c in range(cols):
            x = x+(x*thumb_width) + margin
            img = Image.open(images[image_index])
            img = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            image_index += 1
            contact_sheet.paste(img, (int(x) + int(margin), int(y)))


    # x = 0
    # for image_filepath in images:
    #     img = Image.open(image_filepath)
    #     # img = img.resize((500,500))
    #     img.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
    #
    #     # border_size = 20  # You can adjust this value to control the width of the border
    #     # border_color = (255, 255, 255)  # (R, G, B) value for white color
    #     #
    #     # img = ImageOps.expand(img, border=border_size, fill=border_color)
    #
    #     # shadow_offset = (10, 10)  # Adjust these values to control the offset of the shadow
    #     # shadow_color = (0, 0, 0, 100)  # (R, G, B, alpha) value for black color with transparency (alpha)
    #
    #     contact_sheet.paste(img, (x + int(margin), 0))
    #     x += 100

    contact_sheet.save('./my_contact_sheet.jpg')


create_contact_sheet('./photos/items/4/2')

from PIL import Image, ImageOps

from file_utils import get_all_files


def create_contact_sheet(images_path, output_size: int = 1000):
    images = get_all_files(images_path)
    contact_sheet = Image.new('RGB', (output_size, output_size), (255, 255, 255))

    rows = 0
    cols = 0

    # margin = output_size * 0.02
    margin = 20
    img = Image.open(images[0])
    num_of_images = len(images)
    if len(images) == 2:
        rows = 1
        cols = 2
    elif len(images) == 3:
        rows = 1
        cols = 3
    elif len(images)== 4:
        rows = 2
        cols = 2

    # if cols >= rows:
    #     thumb_width = int((output_size - ((num_of_images+1) * margin)) / num_of_images)
    #     thumb_height = int(thumb_width * img.height / img.width)

    thumb_width = int((output_size - ((cols + 1) * margin)) / cols)
    thumb_height = int(thumb_width * img.height / img.width)

    if rows > 1:
        thumb_height_1 = int((output_size - ((rows + 1) * margin)) / rows)
        thumb_width_1 = int(thumb_height_1 * img.width / img.height)

        if thumb_height_1 < thumb_height:
            thumb_width = thumb_width_1
            thumb_height = thumb_height_1

    # thumb_height = int(output_size / rows - (2 * rows * margin))
    # thumb_width = int(thumb_height * img.width / img.height)
    img = Image.open(images[0])
    image_index = 0

    x_margin = (output_size - (cols * thumb_width)) / (cols + 1)
    y_margin = (output_size - (rows * thumb_height)) / (rows + 1)
    y=0
    for r in range(rows):
        x = 0
        # y = (output_size - (thumb_height *(r+1) )) / 2

        for c in range(cols):
            img = Image.open(images[image_index])
            img = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            image_index += 1
            print(f'x: {int(x) + int(x_margin)}, y:{int(y)}')
            # contact_sheet.paste(img, (int(x) + int(x_margin), int(y)))
            contact_sheet.paste(img, (int(x) + int(x_margin), int(y) + int(y_margin)))
            x = (x + thumb_width) + x_margin
        y = (y + thumb_height) + y_margin


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


create_contact_sheet('photos/items/4')

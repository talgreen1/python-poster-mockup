from PIL import Image, ImageOps, ImageFilter

from file_utils import get_all_files


def create_contact_sheet(images_path, output_size: int = 1000, margin=0.03):
    images = get_all_files(images_path)
    contact_sheet = Image.new('RGBA', (output_size, output_size), (255, 255, 255))

    cols_per_row = []


    margin = output_size * margin

    img = Image.open(images[0])
    num_of_images = len(images)
    if len(images) == 1:
        cols_per_row = [1]
    elif len(images) == 2:
        cols_per_row = [2]
    elif len(images) == 3:
        cols_per_row = [3]
    elif len(images) == 4:
        cols_per_row = [2, 2]
    elif len(images) == 5:
        cols_per_row = [3, 2]

    rows = len(cols_per_row)
    cols = max(cols_per_row)
    thumb_width = int((output_size - ((cols + 1) * margin)) / cols)
    thumb_height = int(thumb_width * img.height / img.width)

    if rows > 1:
        thumb_height_1 = int((output_size - ((rows + 1) * margin)) / rows)
        thumb_width_1 = int(thumb_height_1 * img.width / img.height)

        if thumb_height_1 < thumb_height:
            thumb_width = thumb_width_1
            thumb_height = thumb_height_1

    img = Image.open(images[0])
    image_index = 0

    y_margin = (output_size - (rows * thumb_height)) / (rows + 1)

    y = 0
    for r in range(rows):
        x = 0
        x_margin = (output_size - (cols_per_row[r] * thumb_width)) / (cols_per_row[r] + 1)
        for c in range(cols_per_row[r]):
            img = Image.open(images[image_index])
            img = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            image_index += 1
            # print(f'x: {int(x) + int(x_margin)}, y:{int(y)}')

            ############################################################# Add shadow
            shadow_color = (0, 0, 0, 100)  # RGBA color for the shadow
            shadow_offset = (10, 10)  # Offset of the shadow (x, y)

            shadow_image = Image.new("RGBA", img.size, (0, 0, 0, 100))  # RGBA color and transparency
            # contact_sheet.paste(shadow_image, (shadow_offset[0], shadow_offset[1]), shadow_image)
            shadow_image = shadow_image.filter(ImageFilter.GaussianBlur(5))
            shadow_image = Image.alpha_composite(shadow_image, shadow_image)


            contact_sheet.paste(shadow_image,
                                (int(x) + int(x_margin) + shadow_offset[0], int(y) + int(y_margin) + shadow_offset[1]),
                                shadow_image)
            blurred_shadow = contact_sheet.filter(ImageFilter.GaussianBlur(5))
            # contact_sheet = Image.alpha_composite(contact_sheet, blurred_shadow)
            ###################################################################


            contact_sheet.paste(img, (int(x) + int(x_margin), int(y) + int(y_margin)))
            x = (x + thumb_width) + x_margin
        y = (y + thumb_height) + y_margin

    contact_sheet.save('./my_contact_sheet.png')


create_contact_sheet('photos/items/4')

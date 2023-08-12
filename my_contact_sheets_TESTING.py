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
            # Create a shadow image
            shadow = Image.new('RGBA', img.size, (0, 0, 0, 128))  # Adjust shadow color and transparency as needed

            # Apply Gaussian blur to the shadow image
            shadow_blurred = shadow.filter(ImageFilter.GaussianBlur(10))  # Adjust blur radius as needed

            # Paste the blurred shadow onto the contact sheet
            contact_sheet.paste(shadow_blurred, (int(x) + int(x_margin) + 10, int(y) + int(y_margin) + 10))

            # Paste the original image onto the contact sheet
            # contact_sheet.paste(img, (x, y), img)

            # Display or save the contact sheet
            # contact_sheet.show()
            # contact_sheet.save('output_contact_sheet.png')  # Save the contact sheet if needed
            ###################################################################


            contact_sheet.paste(img, (int(x) + int(x_margin), int(y) + int(y_margin)))
            x = (x + thumb_width) + x_margin
        y = (y + thumb_height) + y_margin

    contact_sheet.save('./my_contact_sheet.png')


create_contact_sheet('photos/items/4')

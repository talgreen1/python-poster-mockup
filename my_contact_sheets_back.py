from PIL import Image, ImageOps

from file_utils import get_all_files


def create_contact_sheet(images_path, output_size: int = 1000):
    images = get_all_files(images_path)
    contact_sheet = Image.new('RGB', (output_size, output_size), (255, 255, 255))

    rows_cols = []
    rows = 0
    cols = 0

    # margin = output_size * 0.02
    margin = 20
    img = Image.open(images[0])
    num_of_images = len(images)
    if len(images) == 1:
        # rows = 1
        cols = 1
        rows_cols = [1]
    elif len(images) == 2:
        # rows = 1
        cols = 2
        rows_cols = [2]
    elif len(images) == 3:
        # rows = 1
        cols = 3
        rows_cols = [3]
    elif len(images) == 4:
        # rows = 2
        cols = 2
        rows_cols = [2, 2]
    elif len(images) == 5:
        # rows = 2
        cols = 3
        rows_cols = [3, 2]

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

    # x_margin = (output_size - (cols * thumb_width)) / (cols + 1)
    # y_margin = (output_size - (rows * thumb_height)) / (rows + 1)
    # y=0
    # for r in range(rows):
    #     x = 0
    #     for c in range(cols):
    #         img = Image.open(images[image_index])
    #         img = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
    #         image_index += 1
    #         # print(f'x: {int(x) + int(x_margin)}, y:{int(y)}')
    #
    #         contact_sheet.paste(img, (int(x) + int(x_margin), int(y) + int(y_margin)))
    #         x = (x + thumb_width) + x_margin
    #     y = (y + thumb_height) + y_margin

    # x_margin = (output_size - (cols * thumb_width)) / (cols + 1)
    y_margin = (output_size - (rows * thumb_height)) / (rows + 1)

    y = 0
    for r in range(len(rows_cols)):
        x = 0
        x_margin = (output_size - (rows_cols[r] * thumb_width)) / (rows_cols[r] + 1)
        for c in range(rows_cols[r]):
            img = Image.open(images[image_index])
            img = img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            image_index += 1
            # print(f'x: {int(x) + int(x_margin)}, y:{int(y)}')

            contact_sheet.paste(img, (int(x) + int(x_margin), int(y) + int(y_margin)))
            x = (x + thumb_width) + x_margin
        y = (y + thumb_height) + y_margin

    contact_sheet.save('./my_contact_sheet.jpg')


create_contact_sheet('photos/items/5')

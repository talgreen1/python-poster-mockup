from PIL import Image

from file_utils import get_all_files


def create_contact_sheet(images_path, output_size: int = 1000):
    images = get_all_files((images_path))
    contact_sheet = Image.new('RGB', (output_size, output_size))

    x=0
    for image_filepath in images:
            img = Image.open(image_filepath)
            img = img.resize(500,500)
            contact_sheet.paste(img,(x,0))
            x +=100

    contact_sheet.save('./my_contact_sheet.jpg')


create_contact_sheet('../../photos/items/4')

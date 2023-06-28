# import argparse
import typer
from typing_extensions import Annotated

from image_utils import insert_image_to_mockup
from placeholder import Placeholder
from tag_utils import get_placeholders, write_placeholders

app = typer.Typer()


# 480.5,601,445,630;1128.5,600,445,630

# @app.command()
# def print_placeholders(image_path: str = Annotated[str, typer.Option("--image-path", "-i")]):
#     '''
#     Prints the placeholders which are stored in the image
#     '''
#     print(get_placeholders(image_path))


@app.command()
def print_placeholders(
        image_path: Annotated[str, typer.Option("--image-path", "-i", help="A full path to the image file.")]):
    print(get_placeholders(image_path))


@app.command()
def set_placeholders(
        image_path: Annotated[str, typer.Option("--image-path", "-i", help="A full path to the image file.")],
        placeholder_list_string: Annotated[str, typer.Option("--placeholders", "-p",
                                                             help='A list of placeholders. A placeholder is set of 4 numbers: x,y,width and height,comma seperated. If you have more then 1 placeholder, seperate them with  ";" For example: "480.5,601,445,630;1128.5,600,445,630". Placeholders text must be inside " "')]):
    '''
    Set placeholder(s) to an image
    '''
    current_placeholder = get_placeholders(image_path)

    if current_placeholder:
        print(f"There are placeholder in this photo. Do you want to overwrite? type 'yes' for overwrite")
        answer = input()
        if answer.lower() != 'yes':
            return

    placeholder_list = []
    placeholder_params_list = placeholder_list_string.split(';')
    placeholder_params_list = [p.split(',') for p in placeholder_params_list]

    placeholder_params_list_float = []
    # placeholder_values = [p.split(',') for p in placeholder_params_list]
    for values in placeholder_params_list:
        placeholder_params_list_float.append(([float(val) for val in values]))

    for placeholder in placeholder_params_list_float:
        kwargs = dict(zip(Placeholder.get_init_param_names(), placeholder))
        placeholder_list.append(Placeholder(**kwargs))

    write_placeholders(image_path=image_path, placeholders=placeholder_list)


def add_image_to_mockup(mockup_path: Annotated[str, typer.Option("--mockup-path", "-i",
                                                                 help="A full path to the mockup image - The image that contains the placeholders")],
                        image_path: Annotated[str, typer.Option("--image-path", "-i",
                                                                help="A full path to an image file, that should be added to the mockup image")],
                        output_image_path: Annotated[str, typer.Option("--output-image-path", "-o",
                                                                       help="full path to the output image (the result image)")],
                        mockup_index: Annotated[str, typer.Option("--image-path", "-i",
                                                                  help="The index of the placeholder inside the mockup path, incase there are more than one placeholder")] = 0,
                        ):
    placeholders = get_placeholders(mockup_path)
    insert_image_to_mockup(mock_image_path=mockup_path, insert_image_path=image_path, placeholder=placeholders[mockup_index],
                           output_image_path=output_image_path)


# if __name__ == "__main__":
#     app()

background_image_path = './photos/template.jpg'  # Path to the background image
insert_image_path = './photos/item1.png'  # Path to the image to be inserted (with alpha channel)
output_image_path = './photos/output.jpg'  # Path to save the resulting image

# add_image_to_mockup(mockup_path='./photos/template.jpg', image_path='./photos/item1.png',
#                     output_image_path="./photos/output.jpg")

# print_placeholder(u'./photos/template.jpg')
# set_placeholders(u'./photos/template.jpg', '259,286,445,630;906,286,445,630')
add_image_to_mockup(mockup_path='./photos/template.jpg', image_path='./photos/item1.png',
                    output_image_path="./photos/output.jpg", mockup_index=1)


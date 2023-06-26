# import argparse
import typer
from typing_extensions import Annotated

from placeholder import Placeholder
from tag_utils import get_placeholders, write_placeholders

app = typer.Typer()


# @app.command()
# def print_placeholders(image_path: str = Annotated[str, typer.Option("--image-path", "-i")]):
#     '''
#     Prints the placeholders which are stored in the image
#     '''
#     print(get_placeholders(image_path))


@app.command()
def print_placeholders(image_path: Annotated[str, typer.Option("--image-path", "-i", help="A full path to the image file.")]):
    print(get_placeholders(image_path))

@app.command()
def set_placeholders(image_path: Annotated[str, typer.Option("--image-path", "-i", help="A full path to the image file.")],
                     placeholder_list_string: Annotated[str, typer.Option("--placeholders", "-p", help="A list of placeholders")]):
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
    for placeholder in placeholder_params_list:
        kwargs = dict(zip(Placeholder.get_init_param_names(), placeholder))
        placeholder_list.append(Placeholder(**kwargs))

    write_placeholders(image_path=image_path, placeholders=placeholder_list)


if __name__ == "__main__":
    app()

# print_placeholder(u'./photos/template.jpg')
# set_placeholder(u'./photos/template.jpg', '11,222,3, 4;5,6,7,8')

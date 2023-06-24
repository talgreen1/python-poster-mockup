# import argparse
import typer

from tag_utils import get_placeholder

# def parse_args():
#     parser = argparse.ArgumentParser(description='Process some integers.')
#     parser.add_argument('-action', required=True, help='Available Options: save_placeholders')
#     parser.add_argument('-placeholders', required=False, help='list of placeholders details for the mock image.')
#     parser.add_argument('-mock_image_path', type=str,
#                         help='Path for the mock image')
#
#     args = parser.parse_args()
#     print(args.action)

# parse_args()
app = typer.Typer()


@app.command()
def print_placeholder(image_path: str):
    print(get_placeholder(image_path))


if __name__ == "__main__":
    app()

import argparse
def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-action', required=True, help='Available Options: save_placeholders')
    parser.add_argument('-placeholders', required=False, help='list of placeholders details for the mock image.')
    parser.add_argument('-mock_image_path', type=str,
                        help='Path for the mock image')

    args = parser.parse_args()
    print(args.accumulate(args.integers))\

parse_args()
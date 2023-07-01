import os


def get_all_files(folder_path, recursive=True):
    all_files = []
    if recursive:
        for root, directories, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                all_files.append(file_path)
    else:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                all_files.append(file_path)
    return all_files


def create_folder_if_not_exists(path):
    folder = os.path.dirname(path)  # Extract the folder path from the full path

    if not os.path.exists(folder):
        os.makedirs(folder)

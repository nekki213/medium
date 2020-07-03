import os
import pathlib
import shutil

sep = os.path.sep

def get_file_list(working_folder: str):
    current_directory = pathlib.Path(working_folder)
    filelist = []
    for current_file in current_directory.iterdir():
        if current_file.name[-4:] == 'html':
            filelist.append(str(current_file.absolute()))
    return filelist


def join_file(file_write, filelist):
    with open(file_write, 'wb') as file_w:
        for file in filelist:
            print(file)
            with open(file, 'rb') as file_r:
                shutil.copyfileobj(file_r, file_w)


if __name__ == "__main__":
    # root folder
    root_folder = os.getcwd() + sep
    root_directory = pathlib.Path(root_folder)
    for item in root_directory.iterdir():
        if item.is_dir():
            file_write = str(item)[-1:] + '.html'
            working_folder = str(item) + sep
            print(str(item))
            file_list = get_file_list(working_folder)
            join_file(file_write, file_list)

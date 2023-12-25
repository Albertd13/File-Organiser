import pathlib
import json


def init_file():
    dir_config_filepath = pathlib.Path('my_classification.json')
    if not dir_config_filepath.is_file():
        suffix_categorisation = {
                                     'Images_Gifs': ['png', 'jpg', 'jpeg', 'gif', 'jfif', 'svg'],
                                     'Audio': ['mp3', 'wav', 'aac', 'wma'],
                                     'Video': ['mp4'],
                                     'Docs': ['doc', 'docx', 'pdf', 'odt', 'md', 'txt', 'xlsx'],
                                     'Coding': ['py', 'html', 'css', 'js', 'cpp', 'cxx', 'c', 'cc'],
                                     'Application_Executables': ['exe', 'msi', 'jar'],
                                     'Archives_Compressed': ['zip', 'rar', 'tar'],
                                     'Emails': ['eml'],
                                     'File_URL_Shortcuts': ['lnk', 'url'],
                                     'Data_Files': ['json', 'csv', 'xml']
                                }
        with open(dir_config_filepath, 'w') as f:
            json.dump(suffix_categorisation, f, indent=4)

    with open(dir_config_filepath, 'r') as f:
        suffix_categorisation = json.load(f)
    cat_rev = {}
    for dir_name in suffix_categorisation:
        for file_suffix in suffix_categorisation[dir_name]:
            cat_rev[file_suffix] = dir_name
    return cat_rev

# gets
def path_input():
    while True:
        path = pathlib.Path(input('Enter full path of directory to sort:'))
        if path.is_dir():
            return path
        else:
            print('Path invalid or does not exist')



def main():
    cat_rev = init_file()
    dir_path = path_input()
    for file in dir_path.iterdir():
        try:
            cat_dir = dir_path / cat_rev[file.suffix[1:]]
        except KeyError:  # handles file suffixes not in json file
            if file.is_dir():  # skips over directories
                continue
            cat_dir = dir_path / 'Others'

        # if category's dir already created, move file inside, else create dir
        if not cat_dir.is_dir():
            cat_dir.mkdir()
        file.rename(cat_dir / file.name)


if __name__ == '__main__':
    main()





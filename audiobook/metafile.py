import os
from  collections import OrderedDict
import yaml
from yaml import dump, Dumper
from audiobook.consts import META_FILE_NAME, PROMO_TEXT
from audiobook.exceptions import ExInitialized

meta_data_template = OrderedDict([
    ('title', ''),
    ('authors', []),
    ('ISBN', ''),
    ('ASIN', ''),
    ('cover', ''),
    ('tags', []),
    ('rating', 0.0),
    ('language', 'English'),
    ('published', ''),
    ('description', ''),
])


def init(current_directory: str, meta_data: OrderedDict) -> None:
    file_path = os.path.join(current_directory, META_FILE_NAME)
    if not os.path.exists(file_path):
        with open(file_path, "w") as meta_file:
            yaml_data = dump(meta_data, Dumper=Dumper,
                             default_flow_style=False)
            meta_file.write(
                '# {promo_text}\n'.format(promo_text=PROMO_TEXT))
            meta_file.write(yaml_data)
        return
    raise ExInitialized("The current directory is already initialized")


def scan_direcory(directory: str):
    walk_dir = os.path.abspath(directory)
    for root, subdirs, files in os.walk(walk_dir):
        file_name = os.path.join(root, META_FILE_NAME)
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                book = yaml.load(file)
                book['file_name'] = file_name
                yield(book)

# http://stackoverflow.com/a/31609484/17734
def setup_yaml():
    represent_dict_order = lambda self, data:  self.represent_mapping(
        'tag:yaml.org,2002:map', data.items())
    yaml.add_representer(OrderedDict, represent_dict_order)


setup_yaml()

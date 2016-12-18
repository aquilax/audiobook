import os
from  collections import OrderedDict
import yaml
from yaml import dump, Dumper
from audiobook.consts import META_FILE_NAME
from audiobook.exceptions import ExInitialized

meta_data = OrderedDict([
    ('title', ''),
    ('authors', ['']),
    ('ISBN', ''),
    ('cover', ''),
    ('tags', ['']),
    ('rating', 0),
    ('language', 'English'),
])


def init(current_directory: str) -> None:
    file_path = os.path.join(current_directory, META_FILE_NAME)
    if not os.path.exists(file_path):
        with open(file_path, "w") as meta_file:
            yaml_data = dump(meta_data, Dumper=Dumper,
                             default_flow_style=False)
            meta_file.write(yaml_data)
        return
    raise ExInitialized("The current directory is already initialized")


# http://stackoverflow.com/a/31609484/17734
def setup_yaml():
    represent_dict_order = lambda self, data:  self.represent_mapping(
        'tag:yaml.org,2002:map', data.items())
    yaml.add_representer(OrderedDict, represent_dict_order)


setup_yaml()

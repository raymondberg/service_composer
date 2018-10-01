import os
import yaml

from .util import SERVICES_ROOT

def _load_yaml_file(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def _all_yaml_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in [f for f in filenames if f.endswith('.yaml')]:
            yield os.path.join(dirpath, filename)

def _define_undocumented(undocumented_list):
    return {k: {'kind': 'undocumented', 'depends_on': []} for k in undocumented_list}

def load_definitions(root_dir=SERVICES_ROOT):
    definitions = {}
    for filepath in _all_yaml_files(root_dir):
        new_definitions = _load_yaml_file(filepath)

        for key in set(definitions.keys()) & set(new_definitions.keys()):
            print('Ignoring Duplicate key {} found in {}'.format(key, filepath))

        if '__undocumented' in new_definitions:
            new_definitions.update(_define_undocumented(new_definitions['__undocumented']))
            del new_definitions['__undocumented']

        for v in new_definitions.values():
            v['definition_file'] = filepath

        definitions = {
            **new_definitions,
            **definitions,
        }

    return definitions

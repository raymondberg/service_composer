from .loader import load_definitions
from .util import SERVICES_ROOT

def _build_hierarchy(definitions, root_node_name):
    try:
        root_node = definitions[root_node_name].copy()
    except KeyError:
        print('Unable to locate node {}'.format(root_node_name))
        root_node = {'kind': 'undefined', 'depends_on': []}
    root_node['name'] = root_node_name
    root_node['depends_on'] = { d_key: _build_hierarchy(definitions, d_key) for d_key in root_node['depends_on'] }
    return root_node

def build_hierarchies(root_dir=SERVICES_ROOT):
    definitions = load_definitions(root_dir)
    return { k: _build_hierarchy(definitions, k) for k,d in definitions.items() if isinstance(d, dict) and d['kind'] == 'root' }

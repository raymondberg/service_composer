from flask import Flask, render_template

from ..hierarchy import build_hierarchies
from ..loader import load_definitions

web_viewer = Flask(__name__)
web_viewer.definitions = load_definitions()
web_viewer.hierarchies = build_hierarchies()

print('Loaded {} definitions; {} hierarchies'.format(len(web_viewer.definitions),len(web_viewer.hierarchies)))

@web_viewer.route('/')
def hello():
    return render_template('index.html', definitions=web_viewer.definitions, hierarchies=web_viewer.hierarchies)

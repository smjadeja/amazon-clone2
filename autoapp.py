from amazon.app import create_app
from flask.helpers import get_debug_flag
from amazon.settings import DevConfig, Prodconfig

CONFIG = DevConfig if get_debug_flag() else Prodconfig

app = create_app(CONFIG)


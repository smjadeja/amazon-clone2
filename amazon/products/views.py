from flask import Blueprint

blueprint = Blueprint('products',__name__)

@blueprint.route('/')
def products():
    return 'products page'

from flask import Blueprint

__author__ = "abhishekmadhu"

item_blueprint = Blueprint('items', __name__)


@item_blueprint.route('/item/<string:name>')
def item_page():
    pass


@item_blueprint.route('/load')
def load_item():
    """
    Loads an item and returns a JSON representation of it.
    :return:
    """
from flask import Blueprint

# Import the required controllers
from controllers.crud_controllers import (
    greet_func,
    farewell_func,
    read_func,
    create_func,
    update_func,
    delete_func,
)

# Create a Blueprint for the Simple Crud routes
crud_router = Blueprint("default", __name__)

# Routes with comments


crud_router.route("/greet/<username>", methods=["GET"])(greet_func)

crud_router.route("/farewell/<username>", methods=["GET"])(farewell_func)


crud_router.route("/read", methods=["GET"])(read_func)

crud_router.route("/create", methods=["POST"])(create_func)

crud_router.route("/update/<int:id>", methods=["PATCH"])(update_func)

crud_router.route("/delete/<int:id>", methods=["DELETE"])(delete_func)

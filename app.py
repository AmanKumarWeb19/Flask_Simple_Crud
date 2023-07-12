import os
from flask import Flask
from flask_cors import CORS

# All routes imported
from routes.crud_routes import crud_router


app = Flask(__name__)

app.debug = True

# Enable CORS for all routes
CORS(app)

# Default routes
@app.route('/')
def default_routes():
    return '<h1 style="color:blue;text-align:center">Welcome to Flask Project!</h1>'

# Register the routes blueprint
app.register_blueprint(crud_router, url_prefix='/default')


if __name__ == '__main__':
    port = os.environ.get("PORT") or 8080
    app.run(host='0.0.0.0', port=port)
from flask import Flask
from app.routes.api_routes import api_routes

app = Flask(__name__)
app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.config.from_pyfile('config.py')
    app.run()
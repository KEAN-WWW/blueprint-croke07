# application/app.py
from flask import Flask
from .bp.homepage import homepage  # relative import from application/bp/homepage

def create_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)  # mount blueprint at "/"
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# expose the factory name the tests expect
init_app = create_app

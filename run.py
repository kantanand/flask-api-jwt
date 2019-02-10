# /run.py
from os import environ

from src.app import create_app

if __name__ == '__main__':
    env_name = environ.get('FLASK_ENV', 'development')
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app = create_app(env_name)
    # run app
    app.run(HOST, PORT)

# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from server.api import app
import os

manager = Manager(app)
@manager.command
def freeze():
    print('Output installed packages into requirements.txt')
    cmd = "./venv/bin/pip freeze >deploy/requirements.txt"
    os.system(cmd)


if __name__ == "__main__":
    server = Server(host="0.0.0.0", port=5000, threaded=True)
    manager.run()

"""server.py, main server file. What brings everything together.
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

from os import listdir, path
from functools import wraps
import re
from flask import Flask, request, Response, render_template, Markup, url_for
import configuration

app = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == config['credentials']['username'] and password == config['credentials']['password']


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


def get_logs_list():
    return [i.replace('.log', '') for i in listdir(config['log_path']) if i.endswith('.log')]


def get_logfile(logfile, lastline=0):

    _split = re.compile(r'[\0%s]' % re.escape(''.join(
                                              [path.sep, path.altsep or ''])))

    fname = path.join(config['log_path'], _split.sub('', logfile) + '.log')

    with open(fname, "r") as f:
        f.seek(0, 2)           # Seek @ EOF
        fsize = f.tell()        # Get Size
        f.seek(max(fsize - 1024, 0), 0)  # Set pos @ last n chars
        lines = f.readlines()       # Read to end
        return lines[(0 - int(lastline)):]
    return 'Error! File not found.'


@app.route('/')
@requires_auth
def index():
    return render_template('index.html',
                           title="Raspberry-GPIO-ZMQ",
                           logs=get_logs_list())


@app.route('/<logfile>/<int:lastline>')
@requires_auth
def log(logfile, lastline=0):
    return render_template('index.html',
                           title="Raspberry-GPIO-ZMQ",
                           logname=logfile,
                           logdata=get_logfile(logfile,
                                               lastline))

def run(config_path = './config/'):
    config = configuration.load(config_path)
    app.run(host=config['host_http'], port=config['port_http'])
if __name__ == "__main__":
    run()

import flask
import configparser
import os
import json

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'xinfodesk.conf')

app = flask.Flask(__name__)

config = configparser.ConfigParser()
config.read(CONFIG_PATH)

def _read_info(id_):
    # read from data_dir
    data_dir = config.get('data', 'data_dir')
    info_path = os.path.join(data_dir, f"{id_}.json")

    if os.path.exists(info_path):
        with open(info_path, 'r') as f:
            return json.load(f)

    return None

@app.route('/')
def index():
    return flask.send_file('static/index.html')

@app.route('/info/<id_>', methods=['GET'])
def get_info(id_):
    # Placeholder for fetching info based on ID
    info = _read_info(id_)
    if info is not None:
        return flask.jsonify(info)
    else:
        return flask.jsonify({"error": "Info not found"}), 404
    
@app.route('/info/<id_>', methods=['POST'])
def update_info(id_):
    # Placeholder for updating info based on ID
    data = flask.request.json
    data_dir = config.get('data', 'data_dir')
    info_path = os.path.join(data_dir, f"{id_}.json")

    with open(info_path, 'w') as f:
        json.dump(data, f)

    return flask.jsonify({"ok": True, "status": "Info updated successfully"})


if __name__ == '__main__':
    host = config.get('server', 'host')
    port = config.getint('server', 'port')
    debug = config.getboolean('server', 'debug')

    app.run(host=host, port=port, debug=debug)

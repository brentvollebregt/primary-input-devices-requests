from flask import Flask, jsonify, request
import platform
import argparse
import socket
import string
import random

import control

# Arguments
parser = argparse.ArgumentParser(description='A simple server that allows you to control the mouse and keyboard.')
parser.add_argument('-key', action="store", type=str, default='')
parser.add_argument('-ip', action="store", type=str, default=socket.gethostbyname(socket.gethostname()))
parser.add_argument('-port', action="store", type=int, default=8080)
args = parser.parse_args()

app = Flask(__name__)
token = ''.join([random.choice(string.printable) for i in range(64)])

def check_token(provided_token):
    return provided_token == token

@app.route("/info", methods=['GET'])
def info_route():
    return jsonify({
        "os" : platform.system(),
        "release" : platform.release(),
        "user": platform.node(),
        "security" : args.key != ''
    })

@app.route("/get_token", methods=['POST'])
def get_token_route():
    if args.key == '':
        return jsonify({'success': True, 'token': token})
    else:
        if request.json['key'] == args.key:
            return jsonify({'success': True, 'token': token})
        else:
            return jsonify({'success': False, 'token': token})

@app.route("/check_token", methods=['POST'])
def check_token_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    return jsonify({'success' : True})

@app.route("/keyboard/type", methods=['POST'])
def keyboard_type_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.keyboard_type(request.json['key'])
    return jsonify({'success' : action})

@app.route("/keyboard/press", methods=['POST'])
def keyboard_press_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.keyboard_press(request.json['key'])
    return jsonify({'success': action})

@app.route("/keyboard/release", methods=['POST'])
def keyboard_release_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.keyboard_release(request.json['key'])
    return jsonify({'success': action})

@app.route("/mouse/position", methods=['GET', 'POST'])
def mouse_position_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    if request.method == 'GET':
        action = control.mouse_position()
        return jsonify({'success': True, 'position' : action})
    else:
        action = control.mouse_position( (int(request.json['x']), int(request.json['y'])) )
        return jsonify({'success': action})

@app.route("/mouse/move", methods=['POST'])
def mouse_move_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.mouse_move(request.json['x'], request.json['y'])
    return jsonify({'success': action})

@app.route("/mouse/click", methods=['POST'])
def mouse_click_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.mouse_click(request.json['button'], request.json['amount'])
    return jsonify({'success': action})

@app.route("/mouse/press", methods=['POST'])
def mouse_press_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.mouse_press(request.json['button'])
    return jsonify({'success': action})

@app.route("/mouse/release", methods=['POST'])
def mouse_release_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.mouse_release(request.json['button'])
    return jsonify({'success': action})

@app.route("/mouse/scroll", methods=['POST'])
def mouse_scroll_route():
    if not check_token(request.json['token']):
        return jsonify({'success' : False, 'reason' : 'Invalid Token'})

    action = control.mouse_scroll(request.json['dx'], request.json['dy'])
    return jsonify({'success': action})

app.run(args.ip, args.port)

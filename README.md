<h1 align="center">Primary Input Devices Requests</h1>
<p align="center">A server that controls the mouse and keyboard based off a request.</p>

## Getting Started

### Prerequisites
 - Python : Python 2.7 or Python 3.4+

### Installing
1. Clone/download this repo
2. Open cmd/terminal and cd to the project
3. Execute ```pip install -r requirements.txt```

## Running the Application
Run ```server.py```. The server will start up in the background with the local ip of the host and 8080 as the port.
 - To declare the ip of the server, pass the -ip flag followed by an ip address
 - To declare the port of the server, pass the -port flag followed by a port number
 - To restrict access to gaining a token from the server, you can provide a -key flag followed by a string.

## Using the Application
1. Run ```server.py``` passing any arguments wanted. This could be done on startup with a batch file or something similar.
2. Acquire the servers token by sending a post request to /get_token. If you passed a key when starting th server, include this key in the data with 'key' as the key.
3. Make requests to the server passing this key and any other necessary data.

#### Here is an example:
```python
>>> import requests

# Get Token
>>> r = requests.post('http://192.168.1.181:8080/get_token', json={'key':'keyDeclaredOnStartUp'})
>>> token = r.json()['token']
>>> token
'!}%b_fz29=u.0~9%g6L|)I\t3j3Sm-htR"6.u!2R\x0cX>Efjvn9DXJ!LX+O91 }BF6:'

# Check Token
>>> requests.post('http://192.168.1.181:8080/check_token', json={'token': token}).json()
{'success': True}

# Get Mouses Position Using Token
>>> requests.get('http://192.168.1.181:8080/mouse/position', json={'token':token}).json()
{'success': True, 'position': [-537, 752]}

# Press the Character 'a'
>>> requests.post('http://192.168.1.181:8080/keyboard/press', json={'token':token, 'key': 'a'}).json()
{'success': True}
```

### Current Routes

| Location | Method | Parameters | Description |
|----------|--------|------------|-------------|
| /info | GET |  | Gets data about the host and will say if a key is required |
| /get_token | POST | key (only if declared on startup) | Gives a token when no key required or the correct key is passed |
| /check_token | POST | token | Will return if a token is valid |
| /keyboard/type | POST | token, key | Type a key (press and release once) |
| /keyboard/press | POST | token, key | Press and hold a key |
| /keyboard/release | POST | token, key | Release a key |
| /mouse/position | GET | token | Returns the position of the mouse |
| /mouse/position | POST | token, x, y | Sets the position of the mouse |
| /mouse/move | POST | token, x, y | Moves the mouse relative to its current position |
| /mouse/click | POST | token, button, amount | Click a mouse button a specified amount of times |
| /mouse/press | POST | token, button | Press and hold a mouse button |
| /mouse/release | POST | token, button | Release a mouse button |
| /mouse/scroll | POST | token, dx, dy | Scroll the mouse horizontally and or vertically |

*Special keys and mouse buttons can be found at the top of [control.py](https://github.com/brentvollebregt/primary-input-devices-requests/blob/master/control.py#L11-52)*
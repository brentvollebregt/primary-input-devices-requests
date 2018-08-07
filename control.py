import string
from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

keyboard_controller = KeyboardController()
mouse_controller = MouseController()

character_keys = [char for char in string.digits] + [char for char in string.ascii_letters] + [char for char in string.punctuation]
action_keys = {
    "backspace" : Key.backspace,
    "caps_lock" : Key.caps_lock,
    "cmd" : Key.cmd,
    "ctrl" : Key.ctrl,
    "delete" : Key.delete,
    "down" : Key.down,
    "end" : Key.end,
    "enter" : Key.enter,
    "esc" : Key.esc,
    "f1" : Key.f1,
    "f2" : Key.f2,
    "f3" : Key.f3,
    "f4" : Key.f4,
    "f5" : Key.f5,
    "f6" : Key.f6,
    "f7" : Key.f7,
    "f8" : Key.f8,
    "f9" : Key.f9,
    "f10" : Key.f10,
    "f11" : Key.f11,
    "f12" : Key.f12,
    "home" : Key.home,
    "insert" : Key.insert,
    "left" : Key.left,
    "menu" : Key.menu,
    "num_lock" : Key.num_lock,
    "page_up" : Key.page_up,
    "pause" : Key.pause,
    "print_screen" : Key.print_screen,
    "right" : Key.right,
    "scroll_lock" : Key.scroll_lock,
    "shift" : Key.shift,
    "space" : Key.space,
    "tab" : Key.tab,
    "up" : Key.up
}
mouse_buttons = {
    'left' : Button.left,
    'right' : Button.right,
    'middle' : Button.middle
}

def keyboard_type(key):
    if key in character_keys:
        keyboard_controller.type(key)
    elif key in action_keys:
        keyboard_controller.press( action_keys[key] )
        keyboard_controller.release( action_keys[key] )
    else:
        return False
    return True

def keyboard_press(key):
    if key in character_keys:
        keyboard_controller.press(key)
    elif key in action_keys:
        keyboard_controller.press( action_keys[key] )
    else:
        return False
    return True

def keyboard_release(key):
    if key in character_keys:
        keyboard_controller.release(key)
    elif key in action_keys:
        keyboard_controller.release( action_keys[key] )
    else:
        return False
    return True

def mouse_position(position_vector=None):
    if position_vector is None:
        return mouse_controller.position
    else:
        mouse_controller.position = position_vector
        return True

def mouse_move(x, y):
    mouse_controller.move(x, y)
    return True

def mouse_click(button, amount):
    mouse_controller.click(mouse_buttons[button], amount)
    return True

def mouse_press(button):
    mouse_controller.press(mouse_buttons[button])
    return True

def mouse_release(button):
    mouse_controller.release(mouse_buttons[button])
    return True

def mouse_scroll(dx, dy):
    # Can't get side scroll to work and dy can be very unpredictable. So much for "The units of scrolling is undefined" from pynput
    mouse_controller.scroll(dx, dy)
    return True
# inputLog.py
from pynput import keyboard, mouse

class InputListener:
    def __init__(self, state):
        self.state = state

    def start(self):
        keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press
        )
        keyboard_listener.start()

        mouse_listener = mouse.Listener(
            on_move=self.on_mouse_move,
            on_scroll=self.on_scroll
        )
        mouse_listener.start()

    def on_key_press(self, key):
        self.state.keyboard_aktif(key)

    def on_mouse_move(self, x, y):
        self.state.mouse_aktif(x, y)

    def on_scroll(self, x, y, dx, dy):
        self.state.scroll_aktif(dx, dy)

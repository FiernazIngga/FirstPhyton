# state.py

class InputState:
    def __init__(self):

        # Untuk typing keyboard
        self.typing = False
        self.key = None

        # Untuk gerakan mouse
        self.mouse_move = False
        self.mouse_pos = (0, 0)

        # Untuk scroll kebawah atau atas
        self.scrollAktif = False
        self.scroll = (0, 0)

    def keyboard_aktif(self, key):
        self.typing = True
        self.key = key

    def mouse_aktif(self, x, y):
        self.mouse_move = True
        self.mouse_pos = (x, y)

    def scroll_aktif(self, dx, dy):
        self.scrollAktif = True
        self.scroll = (dx, dy)

    def reset(self):
        self.typing = False
        self.mouse_move = False
        self.scrollAktif = False

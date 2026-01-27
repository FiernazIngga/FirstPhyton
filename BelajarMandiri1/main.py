# main.py
import time
import os
os.system("cls")

from state import InputState
from inputLog import InputListener

class Application:
    def __init__(self):
        self.state = InputState()
        self.listener = InputListener(self.state)

    def run(self):
        print("Running...")
        self.listener.start()

        try:
            while True:
                time.sleep(0.01)

                if self.state.typing:
                    print(f"Hai ngetik {self.state.key}")

                if self.state.mouse_move:
                    x, y = self.state.mouse_pos
                    print(f"Posisi mouse: ({x}, {y})")

                if self.state.scrollAktif:
                    dx, dy = self.state.scroll
                    print(f"Scroll: ({dx}, {dy})")

                self.state.reset()

        except KeyboardInterrupt:
            print("Program diberhentikan")


if __name__ == "__main__":
    app = Application()
    app.run()
# =========================
# Contoh Lengkap Penggunaan pynput
# Keyboard & Mouse Listener + Controller
# =========================

from pynput import keyboard, mouse
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

# 1. Bagian Listener Keyboard
def klikKeyKeyboard(key):
    """
    Fungsi ini dijalankan setiap ada tombol ditekan.
    'key' bisa berupa karakter biasa ('a','b', dll) atau special key (Key.space, key.enter, dll)
    """
    print(f"[Keyboard] Tombol ditekan: {key}")

def lepasKeyKeyboard(key):
    """
    Fungsi ini dijalankan setiap tombol dilepas
    """
    print(f"[Keyboard] Tombol dilepas: {key}")
    # contoh exit program kalau tekan ESC
    if key == Key.esc:
        print("ESC ditekan, keluar program...")
        return False  # menghentikan listener
    
# 2. Bagian Listener Mouse
def klikMouse(x, y, tombol, ditekan):
    """
    Fungsi ini dijalankan saat mouse di klik
    :param x, y: posisi kursor
    :param tombol: tombol yang diklik (Button.left / Button.right / Button.middle)
    :param ditekan: True berarti ditekan, False berarti dilepas
    """
    if ditekan:
        print(f"[Mouse] Klik di ({x}, {y}) dengan tombol {tombol}")
    else:
        print(f"[Mouse] Lepas tombol {tombol} di ({x}, {y})")

def gerak(x, y):
    """
    Fungsi ini dijalankan saat mouse digerakan
    :param x, y: adalah posisi dari kursor
    """
    print(f"[Mouse] Kursor bergerak ke ({x}, {y})")

def scroll(x, y, dx, dy):
    """
    Fungsi ini dijalankan saat scroll wheel mouse digunakan
    - dx, dy = arah scroll horizontal / vertikal
    """
    print(f"[Mouse] Scroll di {x}, {y} dengan delta {dx}, {dy}")

# 3. Bagian Controller (Keyboard & Mouse)
kb = KeyboardController()
ms = MouseController()

# Contoh fungsi kontrol otomatis
def auto_type():
    """
    Contoh: ketik kalimat otomatis, tunggu sebentar
    """
    kb.type("Halo! Aku teman virtualmu.\n")
    time.sleep(1)
    kb.press(Key.enter)
    kb.release(Key.enter)

def auto_click():
    """
    Contoh: klik kiri mouse di posisi saat ini
    """
    ms.click(Button.left, 1)  # klik kiri sekali

# 4. Menjalankan Listener

# - Keyboard listener
keyboard_listener = keyboard.Listener(
    on_press= klikKeyKeyboard,
    on_release= lepasKeyKeyboard
)

# - Mouse Listener
mouse_listener = mouse.Listener(
    on_click= klikMouse,
    on_move= gerak,
    on_scroll= scroll
)

# start listener di background
keyboard_listener.start()
mouse_listener.start()

# 5. Loop utama
# Di sini kita bisa menambahkan logika yangHalo! Aku teman virtualmu.

# misal mendeteksi idle dan merespons
try:
    idle_seconds = 0
    while True:
        time.sleep(1)
        idle_seconds += 1

        # contoh: auto respons setelah 5 detik idle
        if idle_seconds == 5:
            print("[System] Terlihat idle, aku mengetik sesuatu untukmu...")
            # auto_type() # Ini untuk auto ketik
            # auto_click() # Ini untuk auto klik
            idle_seconds = 0  # reset idle timer
except KeyboardInterrupt:
    print("Program dihentikan manual")  
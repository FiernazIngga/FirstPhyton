# inputLog.py
from pynput import keyboard, mouse
from state import keyboardAktif, mouseAktif, scrollAktif

def mulai_melihat_input_user():
    """
    Fungsi ini menjalankan listener untuk keyboard dan mouse.
    Listener akan memanggil fungsi keyboardAktif atau mouseAktif
    saat user melakukan aktivitas.
    """

    # Listener keyboard: setiap tombol ditekan, set state typing = True
    keyboard_listener = keyboard.Listener(
        on_press=lambda key: keyboardAktif(key)
    )
    keyboard_listener.start()  # jalankan listener di background

    # Listener mouse: setiap mouse digerakkan, set state mouse_move = True dan update posisi
    mouse_listener = mouse.Listener(
        on_move=lambda x, y: mouseAktif(x, y),
        on_scroll=lambda x, y, dx, dy:scrollAktif(dx, dy)
    )
    mouse_listener.start()  # jalankan listener di background

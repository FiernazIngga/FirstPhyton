state = {
    "typing": False,
    "key": None,
    "mouse_move": False,
    "mouse_pos": (0, 0),
    "scroll": (0, 0),
    "scrollAktif": False
}

def keyboardAktif(key):
    state["typing"] = True,
    state["key"] = key

def scrollAktif(x, y):
    state["scrollAktif"] = True,
    state["scroll"] = (x, y)

def mouseAktif(x, y):
    state["mouse_move"] = True
    state["mouse_pos"] = (x, y)

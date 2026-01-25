import time
import os
os.system("cls")

from state import state
from inputLog import mulai_melihat_input_user

def main_loop():
    # while True:
    #     time.sleep(0.1)

    #     # Tentukan status
    #     if state["typing"] and state["mouse_move"]:
    #         status = f"ngetik + gerakin mouse {state['mouse_pos']}"
    #     elif state["typing"]:
    #         status = "ngetik"
    #     elif state["mouse_move"]:
    #         status = f"gerakin mouse {state['mouse_pos']}"
    #     else:
    #         status = "diem"

    #     print(f"\rStatus: {status}    ")

    #     # Reset state tiap loop, kecuali posisi mouse
    #     state["typing"] = False
    #     state["mouse_move"] = False

    try:
        while True:
            time.sleep(0.01) # Delat 1 detik tiap loop

            if state['typing']:
                print(f"Hai ngetik {state['key']}")
            
            if state['mouse_move']:
                x,y = state['mouse_pos']
                print(f"Posisi mouse: ({x}, {y})")

            if state['scrollAktif']:
                x,y = state['scroll']
                print(f"Posisi scroll: ({x}, {y})")

            state["typing"] = False
            state["mouse_move"] = False
            state["scrollAktif"] = False
            
    except KeyboardInterrupt:
        print("Program diberhentikan")

if __name__ == "__main__":
    print("Running...")
    mulai_melihat_input_user()
    main_loop()
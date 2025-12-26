import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_4, KC.KP_5, KC.KP_6, KC.KP_7, KC.KP_8]
]

if __name__ == '__main__':
    keyboard.go()

# i will update the code and make a software once it arrives!

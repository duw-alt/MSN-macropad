import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import OLED

# Initialize the keyboard
keyboard = KMKKeyboard()

# Macros
macros = Macros()
keyboard.modules.append(macros)

# Rotary encoder
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# OLED 
oled = OLED()
keyboard.modules.append(oled)


# Pins
PINS = [board.D7, board.D8, board.D9]  # 3 switches

# Key scanning 
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keymap
keyboard.keymap = [
    [
        KC.A,  # Button 1
        KC.B,  # Button 2
        KC.MACRO("Hello world!"),  # Button 3
    ]
]


# Start the keyboard
if __name__ == "__main__":
    keyboard.go()




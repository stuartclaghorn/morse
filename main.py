morse_code = {
    "A" : ".-",
    "B": "-...",
    "C": ".. .",
    "D": "-..",
    "E": ".",
    "F": ".-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": "-.-.",
    "K": "-.-",
    "L": "--",
    "M": "- -",
    "N": "- .",
    "O": ". .",
    "P": ".....",
    "Q": "..-.",
    "R": ". ..",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": ".-..",
    "Y": ".. ..",
    "Z": "... .",
}
def get_msg():
    msg = input("What is your message?: ").upper()
    return msg

def to_morse(msg):
    morse_msg = ""
    for ch in msg:
        morse_msg += morse_code[ch]
        morse_msg += " "
    return morse_msg


msg = get_msg()
print(f"Your message is: {msg}")
print(f"Your morse message is: {to_morse(msg)}")


import sys

# Braille dictionary for letters, numbers, and special symbols
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', 'cap': '.....O', 'num': '.O.OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse dictionary for Braille to English conversion
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def is_braille(s):
    return all(c in 'O.' for c in s)

def translate_to_braille(text):
    result = []
    for char in text:
        if char.isupper():
            result.append(braille_dict['cap'])
            char = char.lower()
        if char.isdigit():
            result.append(braille_dict['num'])
        result.append(braille_dict[char])
    return ''.join(result)

def translate_to_english(braille):
    result = []
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == braille_dict['cap']:
            i += 6
            symbol = braille[i:i+6]
            result.append(reverse_braille_dict[symbol].upper())
        elif symbol == braille_dict['num']:
            i += 6
            while i < len(braille) and braille[i:i+6] in reverse_braille_dict:
                result.append(reverse_braille_dict[braille[i:i+6]])
                i += 6
            continue
        else:
            result.append(reverse_braille_dict[symbol])
        i += 6
    return ''.join(result)

def main():
    input_text = sys.argv
    if is_braille(input_text):
        print(translate_to_english(input_text))
    else:
        print(translate_to_braille(input_text))

if __name__ == "__main__":
    main()

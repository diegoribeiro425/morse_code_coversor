string_to_morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.---.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
}


class MorseConverter:
    def __init__(self, string: str):
        self.string = string
        self.morse_list = []
        self.invalid_char = ''
        self.morse_string = ''
        self.is_valid = True

    def string_to_morse(self):
        upper_case = self.string.upper()
        for char in upper_case:
            if char == ' ':
                char = '/'
                self.morse_list.append(char)
                continue
            elif char not in string_to_morse:
                self.invalid_char = char
            try:
                self.morse_list.append(string_to_morse[char])
            except KeyError:
                print(f'Input Error. Cannot translate the character: {self.invalid_char}')
                self.is_valid = False

    def converter(self):
        self.string_to_morse()
        if self.is_valid:
            for element in self.morse_list:
                self.morse_string = self.morse_string + ' ' + element
            return self.morse_string
        else:
            return ''

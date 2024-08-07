from morse_code import MorseConverter
import os

repeat = True
ascii_art = r"""
___  ___                      _____           _        _____                           _             
|  \/  |                     /  __ \         | |      |  __ \                         | |            
| .  . | ___  _ __ ___  ___  | /  \/ ___   __| | ___  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \ | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |  | | (_) | |  \__ \  __/ | \__/\ (_) | (_| |  __/ | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|  |_/\___/|_|  |___/\___|  \____/\___/ \__,_|\___|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   


"""


def clear_console():
    if os.name == 'nt':  # Windows
        result = os.system('cls')
        if result != 0:
            print("Failed to clear console. The command returned:", result)
    else:  # Linux e macOS
        os.system('clear')


while repeat:
    print(ascii_art)
    text = input('Type a text to convert to morse code: ')
    print('--------------------------------------------------------------------------------------')
    morse_converter = MorseConverter(text)
    morse_code = morse_converter.converter()
    print(f'Morse Code Output:\n {morse_code}')
    print('--------------------------------------------------------------------------------------')
    again = input('Do you want another go? (y/n): ').lower()
    if again == 'n':
        repeat = False
    clear_console()

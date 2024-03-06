import re

class Morse_Translator:
    def __init__(self):
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.', ' ': '/'
        }

    # Encode the message
    def morse_encode(self, user_message):
        result = ""
        for letter in user_message:
            if letter in self.morse_dict:
                result += self.morse_dict[letter] + " "

        return result

    # Decode the message
    def morse_decode(self, user_message):
        decoded_text = ""
        reverse_morse_dict = {value: key for key, value in self.morse_dict.items()}
        morse_words = user_message.split("/")

        for word in morse_words:
            morse_char = word.split(" ")
            for char in morse_char:
                decoded_text += reverse_morse_dict.get(char, "")
            decoded_text += " "

        return decoded_text.strip().lower()

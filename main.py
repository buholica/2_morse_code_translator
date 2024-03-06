import re
from translator import Morse_Translator

end = False
morse_translator = Morse_Translator()


def capitalize_first_word(decoded_text):
    """Return the decoded message with capitalized words after '.', '!', '?'."""
    pattern = r'(?<=[.!?])\s*'
    sentences = re.split(pattern, decoded_text)

    capitalized_sentence = ""
    for sentence in sentences:
        if sentence:
            sentence = " " + sentence[0].capitalize() + sentence[1:]
            capitalized_sentence += sentence

    return capitalized_sentence


while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Please type your message:\n").upper()
    if direction == "encode":
        morse_coded_message = morse_translator.morse_encode(message)
        print(f"The Morse coded message is: {morse_coded_message}")
    else:
        morse_decoded_message = morse_translator.morse_decode(message)
        print(f"The Morse decoded message is: {capitalize_first_word(morse_decoded_message)}")

    restart = input("Do you want to restart the Morse Translator? Type 'yes' or 'no'.\n").lower()
    if restart == 'no':
        end = True
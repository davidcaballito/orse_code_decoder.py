MORSE_CODE_DICT = { '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', ' ': ' '}
def decode_morse_code(message):
    words = message.split('   ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''
        for letter in letters:
            decoded_word += MORSE_CODE_DICT[letter]
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

message = input('Enter the Morse code message: ')
decoded_message = decode_morse_code(message)
print('Decoded message: ', decoded_message)

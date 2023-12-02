# letter : str
# letter.isascii()
# letter.isspace()

def clear_text(text: str):
    clear = ''.join([letter for letter in text.lower() if ord(letter) in range(97, 123) or letter.isspace()])
    return clear.lower()


result = clear_text('This is a sample, вапвап 3453456')
print(result)
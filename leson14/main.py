# def say(word, n=2, ending=''):
#     """
#     Repeat the given word multiple times with an optional ending.

#     :param word: The word to repeat.
#     :param n: The number of times to repeat the word (default is 2).
#     :param ending: The optional ending to append to each repetition (default is an empty string).
#     :return: The repeated word with the specified ending.
    
#     Examples:
#     >>> say('Hello')
#     'Hello Hello'
#     >>> say('Hi', 5)
#     'Hi Hi Hi Hi Hi'
#     >>> say('cat', 3, '(=^.^=)')
#     'cat (=^.^=)cat (=^.^=)cat (=^.^=)'
#     """
#     repeated_word = f'{word} {ending}' * n
#     return repeated_word.strip()
    
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)

def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words
#
# def sort_words(words):
#     """Sorts the words."""
#     return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off"""
    print words
    word = words.pop(2)
    return word

def print_last_word(words):
    """prints the last word after popping it off"""
    word = words.pop(-1)
    print word

# def sort_sentence(sentence):
#     """Takes in a full sentence and returns the sorted words."""
#     words = break_words(sentence)
#     return sort_words(words)

def print_first_and_last(sentence,local_list):
    words = break_words(sentence)
    print print_first_word(local_list)
    print_last_word(local_list)
    return words

# def print_first_and_last_sorted(sentence):
#     """Prints the first and last words of the sentence"""
#     words = sort_sentence(sentence)
#     print_first_word(words)
#     print_last_word(words)

sentence = "All the good thing comes big"
my_list = ["A", "B", "C", "D"]

# print break_words(sentence)
# print sort_words(sentence)
print print_first_and_last(sentence, my_list)
# print print_first_word(__list__)



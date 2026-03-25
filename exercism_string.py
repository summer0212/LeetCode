def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    new_word = "un" + word
    return new_word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    # print(prefix)
    new_word = prefix 
    for word in range(1, len(vocab_words)):
        new_word = new_word + " " + "::" + " " + prefix + vocab_words[word]

    print(new_word)

def remove_suffix_ness(word):
    nw_word = word[:-4]
    last_element = nw_word[len(nw_word)- 1]
    if last_element == 'i':
        str = nw_word.replace(last_element, "y")
        return str
    else:
        return nw_word
    
def adjective_to_verb(sentence, index):
    if index == -1:
        char_array = sentence.split()
        adjective = char_array[index]
        adjective = adjective[:-1]
        verb = adjective + "en"
        return verb
    
    else:
        char_array = sentence.split()
        adjective = char_array[index]
        verb = adjective + "en"
        return verb

# print(add_prefix_un("manageable"))
# make_word_groups(['auto', 'didactic', 'graph', 'mate'])
# print(remove_suffix_ness("sadness"))
print(adjective_to_verb('I need to make that bright.', -1 ))

"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = list(map(lambda word: prefix + word, vocab_words[1:]))
    words = [prefix] + words
    return (" :: ").join(words)


def remove_suffix_ness(word):
    w = word.replace("ness", "")

    if w[-1] == "i":
        return w[:-1] + "y"
    return w


def adjective_to_verb(sentence, index):
    words = sentence.split(" ")
    return words[index].replace(".", "") + "en"

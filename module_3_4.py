from re import search


def single_root_words(root_word,  *other_words):
    same_words = []
    for i in range(len(other_words)):
        if search(root_word.lower(), other_words[i].lower()) is not None or search(other_words[i].lower(), root_word.lower()) is not None:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

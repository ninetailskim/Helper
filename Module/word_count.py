import re
from functools import reduce

def count_word(lines):
    print(lines)
    # declare a word list
    all_words = []
    pattern = re.compile(r'\w+\W*\w+|\w+')
    # extract all words from lines
    lines = lines.split('\n')
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words = line.split(' ')

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"

            word = (pattern.search(word)).group() if pattern.search(word) else None
            # check if word is not empty
            if word:
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    def st(dic, k):
        if not k in dic:  
            dic[k] = 1  
        else:  
            dic[k] +=1  
        return dic
    counter = sorted(reduce(st, all_words, {}).items(), key=lambda d: d[1], reverse=True)
    return counter
# -*- coding: utf-8 -*-
import re
from functools import reduce
import csv
import json
import _pickle as pickle

def main(filename):
    # read file into lines
    f = open(filename)
    lines = f.readlines()

    # declare a word list
    all_words = []
    pattern = re.compile(r'\w+\W*\w+|\w+')
    # extract all words from lines
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
    #print(counter)
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('wordcount.csv', 'w', newline='') as cf:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(cf)
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        #for key in counter:
        writer.writerows(counter)

    # dump to a json file named "wordcount.json"
    with open('wordcount.json','w') as json_file:
        json.dump(counter, json_file)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    #print(type(counter))
    with open('wordcount.pkl','wb') as f:
        pickle.dump(counter, f)
    #print(type(counter))
    #with open('wordcount.pkl','rb') as f:
        #tes = pickle.load(f)
        #print(tes == counter)


if __name__ == '__main__':
    main("i_have_a_dream.txt")
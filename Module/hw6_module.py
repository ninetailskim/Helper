# -*- coding: utf-8 -*-
from word_count import count_word


def main(filename):
    text = open(filename).read()
    count_stat = count_word(text)
    for word, count in count_stat:
        print(word, count)


if __name__ == '__main__':
    main('i_have_a_dream.txt')

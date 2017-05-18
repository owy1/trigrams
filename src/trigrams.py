"""This module mutates texts into new forms."""

import io
import os
import random
import sys

PATH = os.path.join(os.path.dirname(__file__), 'test.txt')


def get_txt(filename=PATH):
        """Read file."""
        f = io.open(filename, encoding='utf-8')
        text = f .read()
        f.close()
        return text


def trigrams(text):
        """Convert text to dictionary."""
        trigrams = []
        tridict = {}
        text = text.split()
        c = 2
        while c < len(text) - 2:
                a_key = []
                a_key.append(text[c])
                a_key.append(text[c + 1])
                a_key1 = " ".join(a_key)
                trigrams.append((a_key1, text[c + 2]))
                c += 1
        for idx in trigrams:
                tridict[idx[0]] = []
        for idx in trigrams:
                tridict[idx[0]].append(idx[1])
        return tridict


def main(address=PATH, length=200):
    """Generate new text."""
    dct = trigrams(get_txt(address))
    word0 = next(iter(dct))
    word1, word2 = word0.split(" ")[0], word0.split(" ")[1]
    newtxt = word1 + " " + word2
    for i in range(2, length):
        try:
            word3 = random.sample(dct[word1 + " " + word2], 1)[0]
        except KeyError:
            word2, word3 = word0.split(" ")[0], word0.split(" ")[1]
        newtxt += " " + word3
        word1, word2 = word2, word3
        if i % 15 == 0:
            newtxt += '\n'
        if i % 90 == 0:
            newtxt += '\n'
    return newtxt


if __name__ == "__main__":  # pragma: no cover
    try:
        print(main(sys.argv[1], int(sys.argv[2])))
    except IndexError:
        print(main())

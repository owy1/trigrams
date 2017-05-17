"""This module mutates texts into new forms."""

import random
import io


def get_txt(filename='sherlock.txt'):
        """Read file."""
        f = io.open(filename, encoding='utf-8')
        text = f .read()
        f.close()
        return text


def trigrams(text):
        """Convert tex to dictionary."""
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


def gen_txt(word1="on", word2="the", length=200):
        """Generate new text."""
        dct = trigrams(get_txt())
        newtxt = word1 + " " + word2
        for i in range(2, length):
                word3 = random.sample(dct[word1 + " " + word2], 1)[0]
                newtxt += " " + word3
                word1, word2 = word2, word3
        return newtxt

print(gen_txt())
# print(trigrams(get_txt()))

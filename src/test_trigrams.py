'''This module test trigrams.'''
import pytest


def test_trigrams():
    '''Test for conversion to dictionary.'''
    from trigrams import trigrams
    assert trigrams("afaerear aefaerqwer awerqwerwer rf te te tet tetaf") == True


def test_gen_txt():
    '''Test for proper text length.'''
    pass


def test_get_txt():
    '''Test if we get text from file.'''
    pass


def text_main():
    '''Test if given sys argument result are as expected.'''
    pass

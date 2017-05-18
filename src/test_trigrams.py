"""This module test trigrams."""
import os


PATH = os.path.join(os.path.dirname(__file__), 'test.txt')


def test_trigrams():
    """Test for conversion to dictionary."""
    from trigrams import get_txt
    from trigrams import trigrams
    assert len(trigrams(get_txt())) == 197 \
        and trigrams(get_txt())['Holmes she'] == ['is']


def test_main_0_0():
    """Test for proper text length."""
    from trigrams import main
    assert main(PATH, 20).find('Holmes she is') != -1


def test_main_0_1():
    """Test for KeyError handling."""
    from trigrams import main
    assert main(PATH, 1000).find('Holmes she is') != -1


def test_get_txt():
    """Test if we get text from file."""
    from trigrams import get_txt
    assert get_txt().split(' ')[0] == 'To' \
        and get_txt().split(' ')[-1] == 'memory.\n'

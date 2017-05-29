"""This module test trigrams."""
import os


PATH = os.path.join(os.path.dirname(__file__), 'test.txt')


def test_create_trigrams_dict():
    """Test for conversion to dictionary."""
    from trigrams import get_text
    from trigrams import create_trigrams_dict
    assert len(create_trigrams_dict(get_text())) == 197 \
        and create_trigrams_dict(get_text())['Holmes she'] == ['is']


def test_main_0_0():
    """Test for proper text length."""
    from trigrams import main
    assert main(PATH, 20).find('Holmes she is') != -1


def test_main_0_1():
    """Test for KeyError handling."""
    from trigrams import main
    assert main(PATH, 1000).find('Holmes she is') != -1


def test_get_text():
    """Test if we get text from file."""
    from trigrams import get_text
    assert get_text().split(' ')[0] == 'To' \
        and get_text().split(' ')[-1] == 'memory.\n'


def test_generate_trigrams_string():
    """Test for generating a string from create_trigrams_dict."""
    from trigrams import generate_trigrams_string
    from trigrams import create_trigrams_dict
    from trigrams import get_text
    dct = create_trigrams_dict(get_text())
    substring = "she is always THE woman"
    newtxt = generate_trigrams_string(dct, 200)
    assert (substring in newtxt) is True

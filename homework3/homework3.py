from unittest import TestCase
from collections import Counter


def generate_phrase(characters, phrase):
    for char in characters:
        if char in phrase and Counter(characters) >= Counter(phrase):
            return True
        else:
            return False


class TestFunction(TestCase):

    # Check if it returns true when the characters can generate the string

    def test_valid_result_returns_true(self):
        result = generate_phrase('kitnia%', 'nikita%')
        self.assertTrue(result)

    # Check if it returns false when the characters cannot generate the string

    def test_non_result_returns_false(self):
        result = generate_phrase('bhdnek', 'nikita')
        self.assertFalse(result)

    # Check if it returns false when there are not enough characters

    def test_not_enough_returns_false(self):
        result = generate_phrase('cbacba', 'aabbccc')
        self.assertFalse(result)

    # Check if it returns True when characters include capital, number and spaces

    def test_special_characters_returns_true(self):
        result = generate_phrase('odeCristFirslG1   ', 'Code First Girls1')
        self.assertTrue(result)

import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    def test_translate_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_null_input(self):
        self.assertEqual(french_to_english(" "), " ")

class TestEnglishToFrench(unittest.TestCase):
    def test_translate_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_null_input(self):
        self.assertEqual(english_to_french(" "), " ")

unittest.main()
import unittest

from translator import french_to_english, english_to_french

class frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english(), '') # test when null is given. 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'

class englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french(), '') # test when null is given.
        self.assertEqual(english_to_french('Hello'), 'Bonjour' ) # test when 'Hello' is given as input the output is 'Bonjour'

unittest.main()

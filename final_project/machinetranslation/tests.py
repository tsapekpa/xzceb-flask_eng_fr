import unittest

from translator import french_to_english, english_to_french

class frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(), 'Vous devez fournir du texte') # test when null is given. 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'

class englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(), 'You need to provide text') # test when null is given.
        self.assertEqual(english_to_french('Hello'), 'Bonjour' ) # test when 'Hello' is given as input the output is 'Bonjour'

unittest.main()

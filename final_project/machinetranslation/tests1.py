import unittest
"""
Unit tests to test englishToFrench and frenchToEnglish
"""
# # tests.py by Pushapwant
"""
The following does not work when I issue python tests1.py command
from machinetranslation  import englishToFrench, frenchToEnglish 
from machinetranslation.translatory import frenchToEnglish, englishToFrench 
from . import englishToFrench, frenchToEnglish
"""
#The following works in the machinetranslation directory
from translatory import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        # C.1.1 test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # C.1.2 test when 'Hello' is given as input the output is not 'Bye'.
        self.assertNotEqual(englishToFrench('Hello'), 'Bye')


class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        # C.2.1 test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # C.2.2 test when 'Bonjour' is given as input the output is not 'Bye'.
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bye')


unittest.main()

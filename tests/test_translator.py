import sys
import os
sys.path.append(os.path.abspath('../src'))

import unittest
import json

from translator import translate

class TestTranslator(unittest.TestCase):
    
    def setUp(self):
        self.key = ''
        
    def test_translation_german_english(self):
        translation = translate('Hallo', 'de', 'en', self.key)
        expect = 'Hello'
        self.assertEqual(translation, expect)
    
    def test_translation_german_french(self):
        translation = translate('Salut', 'fr', 'en', self.key)
        expect = 'Hello'
        self.assertEqual(translation, expect)
        
if __name__ == '__main__':
    unittest.main()  
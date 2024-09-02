import unittest
from main import *

class TestFixedMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = FixedMatrix()

    def test_get_value(self):
        self.assertEqual(self.matrix.get_value(0, 0), 1)
        self.assertEqual(self.matrix.get_value(1, 5), 1)

    def test_set_value(self):
        self.matrix.set_value(0, 0, 0)
        self.assertEqual(self.matrix.get_value(0, 0), 0)

    def test_extract_word(self):
        word = self.matrix.extract_word(0)
        self.assertEqual(word, '1001101101101110')

    def test_function_one(self):
        result = self.matrix.function_one('1100', '1010')
        self.assertEqual(result, '1000')

    def test_function_fourteen(self):
        result = self.matrix.function_fourteen('1100', '1010')
        self.assertEqual(result, '0111')

    def test_function_three(self):
        result = self.matrix.function_three('1100', '1010')
        self.assertEqual(result, '1100')

    def test_function_twelve(self):
        result = self.matrix.function_twelve('1100', '1010')
        self.assertEqual(result, '0011')

    def test_add_ab(self):
        new_word = self.matrix.add_ab('100')
        self.assertTrue(new_word.startswith('100'))

    def test_update_word(self):
        self.matrix.update_word(0, '1010101010101010')
        updated_word = self.matrix.extract_word(0)
        self.assertEqual(updated_word, '1010101010101010')
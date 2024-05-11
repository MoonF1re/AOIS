import unittest

from main import *

class TestBinaryConversions(unittest.TestCase):
    def test_decimal_to_binary_positive_number(self):
        number = 10
        binary = twos_complement(number)
        self.assertEqual(binary, '01010')

    def test_decimal_to_binary_positive_number_2(self):
        number = 34
        binary = twos_complement(number)
        self.assertEqual(binary, '0100010')

    def test_decimal_to_binary_zero(self):
        number = 0
        binary = twos_complement(number)
        self.assertEqual(binary, '0')

    def test_direct_complement_positive_number(self):
        number = 10
        direct = direct_complement(number)
        self.assertEqual(direct, '01010')

    def test_inverse_complement_negative_number(self):
        number = -10
        inverse = inverse_complement(number)
        self.assertEqual(inverse, '10101')

    def test_add(self):
        number1 = 13
        number2 = 4
        result = add(number1, number2)
        self.assertEqual(result, '010001')

    def test_substract(self):
        number1 = 10
        number2 = 5
        result = substract(number1, number2)
        self.assertEqual(result, '0101')

    def test_multiply(self):
        number1 = 10
        number2 = 5
        result = multiply(number1, number2)
        self.assertEqual(result, '0110010')

    def test_division(self):
        number1 = 10
        number2 = 5
        result = divide_binary(number1, number2)
        self.assertEqual(result, ('10', '000'))

    def test_decimal_to_IEEE(self):
        number = 3.446
        ieee = decimal_to_ieee754(number)
        self.assertEqual(ieee, '01000000010111001000101101000011')

    def test_add_in_IEEE(self):
        number1 = 10.5
        number2 = 4.65
        result = add_ieee754(decimal_to_ieee754(number1), decimal_to_ieee754(number2))
        self.assertEqual(result, '01000001011100100110011001100110')


if __name__ == '__main__':
    unittest.main()

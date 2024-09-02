from main import *
import unittest

class TestLogicFunctions(unittest.TestCase):

    def test_replace_symbols(self):
        self.assertEqual(replace_symbols('a & b'), 'a  and  b')
        self.assertEqual(replace_symbols('a | b'), 'a  or  b')
        self.assertEqual(replace_symbols('!a'), ' not a')
        self.assertEqual(replace_symbols('a -> b'), 'a  <=  b')
        self.assertEqual(replace_symbols('a ~ b'), 'a  ==  b')

    def test_evaluate(self):
        self.assertTrue(evaluate('a & b', (True, True)))
        self.assertFalse(evaluate('a & b', (True, False)))
        self.assertTrue(evaluate('a | b', (True, False)))
        self.assertTrue(evaluate('!a', (False,)))
        self.assertTrue(evaluate('a -> b', (False, True)))
        self.assertFalse(evaluate('a ~ b', (True, False)))

    def test_generate_truth_table(self):
        expression = 'a & b'
        terms_num, entries = generate_truth_table(expression)
        expected_entries = [
            ((0, 0), False),
            ((0, 1), False),
            ((1, 0), False),
            ((1, 1), True)
        ]
        self.assertEqual(terms_num, 2)
        self.assertEqual(entries, expected_entries)

    def test_build_sdnf_cnf(self):
        entries = [
            ((0, 0), False),
            ((0, 1), False),
            ((1, 0), False),
            ((1, 1), True)
        ]
        terms_num = 2
        sdnf, cnf = build_sdnf_cnf(entries, terms_num)
        self.assertEqual(sdnf, 'a & b')
        self.assertEqual(cnf, '(a | b) & (a | !b) & (!a | b)')

    def test_combine_terms(self):
        self.assertEqual(combine_terms([1, 1, 0], [1, 1, 1]), [1, 1, '-'])
        self.assertEqual(combine_terms([1, 1, 0], [1, 0, 0]), [1, '-', 0])
        self.assertIsNone(combine_terms([1, 1, 0], [0, 0, 0]))

    def test_find_prime_implicants(self):
        minterms = [[1, 1, 0], [1, 1, 1], [1, 0, 0]]
        prime_implicants = find_prime_implicants(minterms)
        expected = {(1, 1, '-'), (1, '-', 0)}
        self.assertEqual(prime_implicants, expected)

    def test_essential_prime_implicants(self):
        prime_implicants = {(1, 1, '-'), (1, '-', 0)}
        minterms = [[1, 1, 0], [1, 1, 1]]
        essential = essential_prime_implicants(prime_implicants, minterms)
        expected = {(1, 1, '-')}
        self.assertEqual(essential, expected)

    def test_quine_mccluskey(self):
        entries = [
            ((1, 1, 0), True),
            ((1, 1, 1), True),
            ((1, 0, 0), False),
            ((0, 0, 0), False)
        ]
        terms_num = 3
        essential, remaining = quine_mccluskey(entries, terms_num)
        expected_essential = {(1, 1, '-')}
        expected_remaining = []
        self.assertEqual(essential, expected_essential)
        self.assertEqual(remaining, expected_remaining)

    def test_format_implicant(self):
        implicant = [1, '-', 0]
        terms_num = 3
        formatted = format_implicant(implicant, terms_num)
        self.assertEqual(formatted, '!a & !c')

    def test_to_decimal(self):
        self.assertEqual(to_decimal((1, 0, 1)), 5)
        self.assertEqual(to_decimal((0, 0, 1)), 1)

    def test_create_kmap(self):
        entries = [
            ((1, 1, 0), True),
            ((1, 1, 1), True),
            ((1, 0, 0), False),
            ((0, 0, 0), False)
        ]
        terms_num = 3
        kmap = create_kmap(entries, terms_num)
        expected_kmap = [
            [None, None, None, None],
            [None, None, 1, 1],
            [None, None, None, None],
            [None, None, None, None]
        ]
        self.assertEqual(kmap, expected_kmap)

    def test_karno_minimize(self):
        terms_num, entries = generate_truth_table("(a & b)")
        self.assertEqual( karno_minimize(entries, terms_num, is_sdnf=True), True)

    def test_quine_mccluskey_with_chart(self):
        terms_num, entries = generate_truth_table("(a & b)")
        self.assertEqual(quine_mccluskey_with_chart(entries, terms_num, is_sdnf=True), ({(1, 1)}, [], {}))

    def test_print_prime_implicant_chart(self):
        terms_num, entries = generate_truth_table("(a & b)")
        essential_implicants, remaining_minterms, chart = quine_mccluskey_with_chart(entries, terms_num, is_sdnf=False)
        self.assertEqual(print_prime_implicant_chart(chart), True)

    def test_print_truth_table(self):
        terms_num, entries = generate_truth_table("(a & b)")
        self.assertEqual(print_truth_table(entries, terms_num), True)

    def test_print_result(self):
        terms_num, entries = generate_truth_table("(a & b)")
        essential_implicants, remaining_minterms, chart = quine_mccluskey_with_chart(entries, terms_num, is_sdnf=True)
        self.assertEqual(print_result(essential_implicants, terms_num, is_sdnf=True), True)

if __name__ == '__main__':
    unittest.main()
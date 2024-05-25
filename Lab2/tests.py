import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_sdnf(self):
        user_input = "(a & b)"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf, cnf = build_sdnf_cnf(tt_entries, terms_num)
        self.assertEqual(sdnf, "a & b")

    def test_cnf(self):
        user_input = "(a & b)"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf, cnf = build_sdnf_cnf(tt_entries, terms_num)
        self.assertEqual(cnf, "(a | b) & (a | !b) & (!a | b)")

    def test_sdnf2(self):
        user_input = "(a | b) & !c"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf, cnf = build_sdnf_cnf(tt_entries, terms_num)
        self.assertEqual(sdnf, "!a & b & !c | a & !b & !c | a & b & !c")  # add assertion here

    def test_cnf2(self):
        user_input = "(a | b) & !c"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf, cnf = build_sdnf_cnf(tt_entries, terms_num)
        self.assertEqual(cnf, "(a | b | c) & (a | b | !c) & (a | !b | !c) & (!a | b | !c) & (!a | !b | !c)")

    def test_index_form(self):
        user_input = "(a & b)"
        terms_num, tt_entries = generate_truth_table(user_input)
        indexed_form = ''.join(str(int(result)) for _, result in tt_entries)
        self.assertEqual(indexed_form, "0001")

    def test_index_form2(self):
        user_input = "(a | b) & c"
        terms_num, tt_entries = generate_truth_table(user_input)
        indexed_form = ''.join(str(int(result)) for _, result in tt_entries)
        self.assertEqual(indexed_form, "00010101")

    def test_index_form3(self):
        user_input = "(a & b)"
        terms_num, tt_entries = generate_truth_table(user_input)
        indexed_form = ''.join(str(int(result)) for _, result in tt_entries)
        self.assertEqual(indexed_form_to_decimal(indexed_form), 1)

    def test_index_form4(self):
        user_input = "(a | b) & c"
        terms_num, tt_entries = generate_truth_table(user_input)
        indexed_form = ''.join(str(int(result)) for _, result in tt_entries)
        self.assertEqual(indexed_form_to_decimal(indexed_form), 21)

    def test_sdnf_index(self):
        user_input = "(a -> b) & !c"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf_indexes, cnf_indexes = build_index_forms(tt_entries)
        self.assertEqual(sdnf_indexes, [0, 2, 6])

    def test_cnf_index(self):
        user_input = "(a -> b) & !c"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf_indexes, cnf_indexes = build_index_forms(tt_entries)
        self.assertEqual(cnf_indexes, [1, 3, 4, 5, 7])


    def test_sdnf_index2(self):
        user_input = "(!a | b) | c"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf_indexes, cnf_indexes = build_index_forms(tt_entries)
        self.assertEqual(sdnf_indexes, [0, 1, 2, 3, 5, 6, 7])

    def test_cnf_index2(self):
        user_input = "(!a | b) | c"
        terms_num, tt_entries = generate_truth_table(user_input)
        sdnf_indexes, cnf_indexes = build_index_forms(tt_entries)
        self.assertEqual(cnf_indexes, [4])

    def test_replace(self):
        user_input = "(a & b)"
        self.assertEqual(replace_symbols(user_input), "(a  and  b)")

if __name__ == '__main__':
    unittest.main()

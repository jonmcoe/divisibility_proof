from unittest import TestCase

from util import *


class UtilTestCase(TestCase):

    def test_int_to_digits_list_decimal(self):
        self.assertEquals(int_to_digits_list(10, 123), [1,2,3])

    def test_int_to_digits_list_hex(self):
        self.assertEqual(int_to_digits_list(16, 123), [7,11])

    def test_sum_digits_decimal(self):
        self.assertEqual(sum_digits([1,2,3,4,5]), 15)

    def test_sum_digits_hex(self):
        self.assertEqual(sum_digits([3,15]), 18)

    def test_make_mod_matcher_decimal(self):
        mod_matcher_true = make_mod_matcher(10, 3)
        self.assertTrue(mod_matcher_true(457983452))

        mod_matcher_false = make_mod_matcher(10, 7)
        self.assertFalse(mod_matcher_false(34589343))

    def test_make_mod_matcher_hex(self):
        mod_matcher_true = make_mod_matcher(16, 15)
        self.assertTrue(mod_matcher_true(457983452))

        mod_matcher_false = make_mod_matcher(16, 7)
        self.assertFalse(mod_matcher_false(34589343))

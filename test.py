from unittest import TestCase

from util import *


class UtilTestCase(TestCase):

    def test_int_to_string_decimal(self):
        self.assertEquals(int_to_string(10, 123), '123')

    def test_int_to_string_hex(self):
        self.assertEqual(int_to_string(16, 123), '7B')

    def test_sum_digits_decimal(self):
        self.assertEqual(sum_digits('12345'), 15)

    def test_sum_digits_hex(self):
        self.assertEqual(sum_digits('3F'), 18)

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

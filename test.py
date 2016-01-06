from unittest import TestCase

from util import *


class UtilTestCase(TestCase):

	def test_int_to_string(self):
		self.assertEquals(int_to_string(10, 123), '123')

	# TODO: write more

import string


DIGITS = string.digits + string.ascii_uppercase
MAX_BASE = len(DIGITS)


def make_mod_matcher(base, divisor):
	def f(n):
		return n % divisor == sum_digits(int_to_string(base, n)) % divisor
	return f


def int_to_string(base, n):
	ans = ""
	if n == 0:
		return '0'
	while n > 0:
		ans = DIGITS[n % base] + ans
		n //= base
	return ans




def sum_digits(s):
	return sum([int(i, MAX_BASE) for i in s])

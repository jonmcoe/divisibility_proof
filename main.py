import itertools

from util import make_mod_matcher

"""
Intended to test a generalization of the following rule:

A number is divisible by 3 iff the sum of its digits (base 10) is divisible by 3

Generalized for any base, divisor is a any kth (integer k) root of base-1

TODO: write this formally

"""

EXPECT_TRUE = [(2,1)]+list(itertools.chain(
	*[ #TODO: indentation?
		[
			(b, int((b-1)**(1/k)))
			for k in itertools.takewhile(lambda i: ((b-1)**(1/i)).is_integer(), range(1,10))
		]
		for b in range(3,36)
	]
))
EXPECT_FALSE = [
    (10, 4),
    (10, 27)
]
RANGE = range(10**5)

for case in EXPECT_TRUE + EXPECT_FALSE:
    check_mod_match = make_mod_matcher(case[0], case[1])
    match = all((check_mod_match(i) for i in RANGE))
    str_dict = {
        'b': case[0],
        'd': case[1],
        'm': match
    }
    print("Base {b}\t Divisor {d}:\t{m}".format(**str_dict))

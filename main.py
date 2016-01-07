import itertools

from util import make_mod_matcher

"""
Intended to test a generalization of the following rule:

A number is divisible by 3 iff the sum of its digits (base 10) is divisible by 3

Generalized for any base, divisor is a any kth (integer k) root of base-1

TODO: write this formally

"""

MAX_BASE = 50
EXPECT_TRUE = [(2, 1)] + list(itertools.chain(
    *[  # TODO: indentation?
        [
            (base, divisor)
            for divisor in range(2,base)
            if (base-1) % divisor == 0  # naive factorization. could be more performant
        ]
        for base in range(3, MAX_BASE)
    ]
))
EXPECT_FALSE = [
    (10, 4),
    (10, 27)
]
N_RANGE = range(10 ** 5)

for case in EXPECT_TRUE + EXPECT_FALSE:
    check_mod_match = make_mod_matcher(case[0], case[1])
    match = all((check_mod_match(i) for i in N_RANGE))
    str_dict = {
        'b': case[0],
        'd': case[1],
        'm': match
    }
    print("Base {b}\t Divisor {d}:\t{m}".format(**str_dict))

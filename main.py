from util import make_mod_matcher

"""
Intended to test a generalization of the following rule:

A number is divisible by 3 iff the sum of its digits (base 10) is divisible by 3

Generalized for any base, divisor is a any kth (integer k) root of base-1

TODO: write this formally

"""

EXPECT_TRUE = [ #TODO: generate this list
    (28, 3),
    (10, 9),
    (10, 3),
    (9, 8),
    (9, 4),
    (9, 2),
    (5, 4),
    (5, 2),
    (4, 3),
    (3, 2),
    (2, 1)
]
EXPECT_FALSE = [
    (10, 4),
    (10, 27)
]
RANGE = range(10**6)

for case in EXPECT_TRUE + EXPECT_FALSE:
    check_mod_match = make_mod_matcher(case[0], case[1])
    match = all((check_mod_match(i) for i in RANGE))
    str_dict = {
        'b': case[0],
        'd': case[1],
        'm': match
    }
    print("Base {b}\t Divisor {d}: {m}".format(**str_dict))

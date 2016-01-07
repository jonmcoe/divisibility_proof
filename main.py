import itertools

from util import make_mod_matcher

"""
Intended to test a generalization of the following rule:

A number is divisible by 3 iff the sum of its digits (base 10) is divisible by 3

Generalized for any base, divisor is any divisor of base-1

Formally:
In a given base b, a value x and the sum of its digits are congruent modulo
any divisor of (b-1)

"""

MAX_BASE = 50
EXPECT_TRUE = itertools.chain.from_iterable(
    [[(2,1)]] +
    [
        [
            (base, divisor)
            for divisor in range(2,base)
            if (base-1) % divisor == 0  # naive factorization. could be more performant
        ]
        for base in range(3, MAX_BASE)
    ]
)
EXPECT_FALSE = [
    (10, 4),
    (10, 27)
]


def _check_pair_and_print(base, divisor, expected):
    check_mod_match = make_mod_matcher(base, divisor)
    test_range = range(max(10**5, base**2))
    match = all((check_mod_match(i) for i in test_range))

    str_dict = {
        'b': base,
        'd': divisor,
        'm': match
    }
    print("Base {b}\t Divisor {d}:\t{m}".format(**str_dict))
    assert match == expected


if __name__ == '__main__':

    for case in EXPECT_TRUE:
        _check_pair_and_print(case[0], case[1], True)

    for case in EXPECT_FALSE:
        _check_pair_and_print(case[0], case[1], False)

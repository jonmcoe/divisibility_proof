def make_mod_matcher(base, divisor):
    def f(n):
        return n % divisor == sum_digits(int_to_digits_list(base, n)) % divisor
    return f


def int_to_digits_list(base, n):
    ans = []
    if n == 0:
        return [0]
    while n > 0:
        ans = [n % base] + ans
        n //= base
    return ans


sum_digits = sum

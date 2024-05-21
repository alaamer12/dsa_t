import timeit


def find_even_numbers(start, stop):
    even_numbers = []
    for i in range(start, stop):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


def optimized_find_even_numbers(start, stop):
    return [i for i in range(start, stop) if i % 2 == 0]


def optimized_find_even_numbers_with_binary(start, stop):
    return [i for i in range(start, stop) if i & 1 == 0]


def optimized_find_even_numbers_with_filter(start, stop):
    return (filter(lambda x: x % 2 == 0, range(start, stop)))


def optimized_find_even_numbers_with_filter_with_binary(start, stop):
    return (filter(lambda x: x & 1 == 0, range(start, stop)))


def optimized_find_even_numbers_with_map(start, stop):
    return (map(lambda x: x % 2 == 0, range(start, stop)))


def is_even(x):
    return True if x == 0 else (False if x == 1 else is_even(x - 2))


# def optimized_find_even_numbers_with_reccursion_with_filter(start, stop):
#     return list(filter(is_even, range(start, stop)))

print(timeit.timeit("find_even_numbers(1, 50000000)", setup="from __main__ import find_even_numbers", number=1))
print(
    timeit.timeit("optimized_find_even_numbers(1, 50000000)", setup="from __main__ import optimized_find_even_numbers",
                  number=1))
print(timeit.timeit("optimized_find_even_numbers_with_binary(1, 50000000)",
                    setup="from __main__ import optimized_find_even_numbers_with_binary", number=1))
print(timeit.timeit("optimized_find_even_numbers_with_filter(1, 50000000)",
                    setup="from __main__ import optimized_find_even_numbers_with_filter", number=1))
print(timeit.timeit("optimized_find_even_numbers_with_filter_with_binary(1, 50000000)",
                    setup="from __main__ import optimized_find_even_numbers_with_filter_with_binary", number=1))
print(timeit.timeit("optimized_find_even_numbers_with_map(1, 50000000)",
                    setup="from __main__ import optimized_find_even_numbers_with_map", number=1))
# print(timeit.timeit("optimized_find_even_numbers_with_reccursive(1, 50000000)", setup="from __main__ import optimized_find_even_numbers_with_reccursive", number=1))
# print(timeit.timeit("optimized_find_even_numbers_with_reccursion_with_filter(1, 50000000)", setup="from __main__ import optimized_find_even_numbers_with_reccursion_with_filter", number=1))


""" with []
4.545819700004358
4.219711300000199
3.829754399994272
6.100002792663872e-06
2.9000002541579306e-06
"""

""" with list()
4.4063872000042466
4.306931699997222
4.128048499995202
6.023642299995117
5.200231999995594
"""

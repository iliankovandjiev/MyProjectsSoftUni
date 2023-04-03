from math import sqrt
from typing import List


def get_primes(data: List[int]):
    for el in data:
        if el <= 1:
            continue
        for num in range(2, int(sqrt(el)) + 1):
            if el % num == 0:
                break
        else:
            yield el



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
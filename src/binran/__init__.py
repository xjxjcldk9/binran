import argparse
import random
from math import ceil, log2

parser = argparse.ArgumentParser()
parser.add_argument('n', type=int)
args = parser.parse_args()


def binran(n):
    digits = ceil(log2(n))

    gen_int = n+1
    while gen_int > n:
        bin_num = ''
        for i in range(digits):
            bin_num += str(random.randrange(2))
        gen_int = int(bin_num, 2) + 1
    return gen_int


def run_binran():
    result = binran(args.n)
    print(result)

import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

from functools import reduce

def find_previous_number(target, number):
    return (target // number) * number

def find_next_number(target, number):
    return find_previous_number(target, number) + number

def find_next_mod(target, number, remainder):
    while True:
        if target % number == remainder:
            return target
        target += 1

# This function computes GCD
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def chinese_remainder(divisors, remainders):
    M = prod(divisors)
    as_ = list(map(lambda d: int(M/d), divisors))
    eea_result = list(map(lambda tup: extended_gcd(*tup), zip(as_, divisors)))
    is_ = [result[0] % div for result, div in zip(eea_result, divisors)]
    Z = sum(map(prod, zip(is_, remainders, as_)))
    X = Z % M
    return X

def prod(nums):
    return reduce(lambda a, b: a * b, nums, 1)

def extended_gcd(a, b):
    # EEA
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return Bezout coefficient 1, 2, and the gcd
    return old_s, old_t, old_r

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

"""
"""
def problem_part1(earliest_time, bus_time):
    def next_number_greater(target, id):
        return (target // id) * id + id

    bus_time = [int(x) for x in bus_time if x != "x"]
    possibles = list(map(lambda x: next_number_greater(earliest_time, x), bus_time))
    print(possibles)
    minimum = min(possibles)
    print(minimum, bus_time[possibles.index(minimum)])
    return (minimum - earliest_time) * bus_time[possibles.index(minimum)]

"""
this question is about inverse mod: wow CSCI 60 flashback coming through.
"""
def problem_part2(earliest_time, bus_time):
    ret = [(int(bus_time[0]), 0)]

    for index, value in enumerate(bus_time):
        if index == 0 or value == "x":
            continue
        ret.append((int(value), index))

    divisors, remainders = [], []
    for value, index in ret:
        remainders.append((-index) % value)
        divisors.append(value)

    solution = chinese_remainder(divisors, remainders)

    return solution

def day13_main():
    print("2020 AOC Challenge Day 13: Shuttle Search")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    earliest_time = int(raw_texts[1])
    bus_times = [x for x in raw_texts[2].split(",")]

    part1_answer = problem_part1(earliest_time, bus_times)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(earliest_time, bus_times)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day13_main()
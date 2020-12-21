import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join


directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"
PROBLEM_LAST = 2020
PROBLEM_LAST_PT2 = 30000000
FIRST_ENCOUNTER = 0

"""
"""
def problem_part1(numbers, limit=PROBLEM_LAST):
    mapping = {}
    # how do we get current number? based on past number
    ret = []
    for i, number in enumerate(numbers):
        mapping[number] = (i, None)
        ret.append(number)

    ret.append(0)
    # if 0 in mapping:
    #     previous, _ = mapping[0]
    #     mapping[0] = len(numbers), previous
    # else:
    #     mapping[0] = (len(numbers, None))

    for index in range(len(numbers), limit-1):
        current_number = ret[-1]

        # Do not update mapping with last number.
        if current_number in mapping:
            current, previous = mapping[current_number]
            mapping[current_number] = (len(ret) - 1, current)
            current, previous = mapping[current_number]
            next_number = current - previous
            ret.append(next_number)
        else:
            next_number = FIRST_ENCOUNTER
            mapping[current_number] = (len(ret)-1, None)
            ret.append(next_number)
    return ret[-1]

"""
"""
def problem_part2(numbers):
    return problem_part1(numbers, PROBLEM_LAST_PT2)

def day15_main():
    print("2020 AOC Challenge Day 15: Docking Data")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    ret = None
    for line in raw_texts:
        if not line:
            continue
        ret = line.split(",")

    ret = [int(x) for x in ret]

    part1_answer = problem_part1(ret)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(ret)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day15_main()
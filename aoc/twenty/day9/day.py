import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

group_size = 25

"""
"""
def problem_part1(bags):
    holding = {}
    ret = None

    for i, i_value in enumerate(bags):
        for j in range(1, group_size+1):
            if i+j >= len(bags):
                break
            j_value = bags[i+j]
            summation = i_value + j_value
            holding[summation] = holding.get(summation, []) + [(i, i+j)]

    for i, value in enumerate(bags):
        if i < group_size-1:
            continue

        if value in holding:
            potentials = holding[value]
            is_valid = False
            for mi, mx in potentials:
                if (i-25) <= mi and mx <= i:
                    is_valid = True
                    break
            if not is_valid:
                return value
        else:
            return value

    return ret

"""
Embarrassed about using brute force, but can't think of better way atm
"""
def problem_part2(numbers, target):
    index = 1
    last_index = numbers.index(target)
    ret = []
    is_done = False

    for i in range(last_index):
        temp = []
        for j in range(i+1, last_index):
            if sum(temp) == target:
                ret = temp
                is_done = True
                break
            if sum(temp) > target:
                break

            temp.append(numbers[j])

        if is_done:
            break

    print (ret)
    return min(ret) + max(ret)

def day9_main():
    print("2020 AOC Challenge Day 7: Handy Haversacks")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = []

    for line in raw_texts:
        if line == "":
            continue
        lines.append(int(line))

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines, part1_answer)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day9_main()
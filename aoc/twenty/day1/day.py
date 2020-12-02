import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"
target_number = 2020

"""
"""
def problem_part1(lines):
    seen = set()
    answer = None
    for number in lines:
        if number in seen:
            answer = number * (target_number - number)
            break
        else:
            seen.add(target_number - number)
    return answer

"""
"""
def problem_part2(lines):
    seen = set()
    mapping = {}
    answer = None

    for index, number in enumerate(lines):
        for inner_index in range(len(lines)):
            summation = number + lines[inner_index]
            seen.add(target_number - summation)
            mapping[summation] = (number, lines[inner_index])

    for number in lines:
        if number in seen:
            number1 = mapping[target_number-number][0]
            number2 = mapping[target_number-number][1]
            answer = number * number1 * number2
            break

    return answer

def day1_main():
    print("2020 AOC Challenge Day 1: Report Repair")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)

    lines = [int(number) for number in raw_texts]

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day1_main()
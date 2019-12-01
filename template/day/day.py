import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def problem_part1(lines):
    return 

def problem_part2(lines):
    return

def day_main():
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day_main()
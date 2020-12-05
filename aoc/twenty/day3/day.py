import os
import functools

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

tree = '#'
free_space = "."

"""
I thought for some reason thing was suppose to be transposed.
I am stupid. :(
"""
def problem_part1(lines, right=3, down=1):
    row, col = 0, 0
    count = 0
    row_max = len(lines)
    col_max = len(lines[0])

    while True:
        if row >= row_max:
            break

        if lines[row%row_max][col%col_max] == tree:
            count += 1

        row, col = row + down, col + right

    return count

"""
"""
def problem_part2(lines):
    parameters = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    ret = []
    for i, j in parameters:
        ret.append(problem_part1(lines, i, j))
    return functools.reduce(lambda x, y: x * y, ret)

def day3_main():
    print("2020 AOC Challenge Day 3: Toboggan Trajectory")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day3_main()
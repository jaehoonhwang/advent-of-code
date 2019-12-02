import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def rocket_equation_part1(fuels):
    return sum(list(map(lambda x: (x // 3) - 2, fuels)))

def convert_fuel(fuel):
    start = fuel
    curr = 0
    while start >= 0:
        start = (start // 3) - 2 
        if start < 0:
            break
        curr += start 

    return curr

def rocket_equation_part2(fuels):
    return sum(list(map(lambda x: convert_fuel(x), fuels)))

def day1_main():
    print("2019 AOC Challenge Day1")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    fuels = list(map(lambda x: int(x), lines))

    part1_answer = rocket_equation_part1(fuels)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = rocket_equation_part2(fuels)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day1_main()
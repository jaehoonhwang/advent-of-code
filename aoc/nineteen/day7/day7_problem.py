import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

from aoc.nineteen.day5.day5_problem import handle_opcode
from aoc.nineteen.day5.day5_problem import parse_input

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def run_program(lines, input_value):
    return handle_opcode(lines, input_value)

def get_possible_combination(number):
    def dfs(curr, possible, ret):
        if len(possible) == 1:
            curr += possible[0]
            ret.append(curr)
            return 
            
        for i, digit in enumerate(possible):
            dfs(curr + digit, possible[:i] + possible[i+1:], ret)

    string = str(number)
    ret = []

    dfs("", string, ret)

    return ret

def problem_part1(lines):
    # number = "01234"
    # combinations = get_possible_combination(number)
    curr_max = float('-inf')
    
    output = 0
    for phase_setting in "43210":
        shallow_lines = lines[:]
        current_input = 0 if phase_setting == "4" else output
        output = handle_opcode(shallow_lines, current_input)
    
def problem_part2(lines):
    return

def day7_main():
    print("2019 AOC Challenge Day 7")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    lines = parse_input(lines)

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day_main()
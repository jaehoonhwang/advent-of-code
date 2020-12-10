import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

ACCUMULATOR = "acc"
NO_OPERATION = "nop"
JUMP = "jmp"

valid_commands = [ACCUMULATOR, NO_OPERATION, JUMP]

"""
"""
def problem_part1(instructions):
    mapping = {ACCUMULATOR: 0,}
    line_number = 0
    # line_number, accumulator
    seen_line = set()

    while True:
        command, value = instructions[line_number]
        if line_number in seen_line:
            break
        seen_line.add(line_number)

        if command == ACCUMULATOR:
            mapping[ACCUMULATOR] += value
            line_number += 1
        elif command == NO_OPERATION:
            line_number += 1
        elif command == JUMP:
            line_number += value
        else:
            raise NotImplementedError("{} operation has not been operation".format(command))

    return mapping[ACCUMULATOR]

def run_program(instructions):
    mapping = {ACCUMULATOR: 0,}
    line_number = 0
    # line_number, accumulator
    seen_line = set()
    while line_number < len(instructions):
        command, value = instructions[line_number]
        if line_number in seen_line:
            break
        seen_line.add(line_number)

        if command == ACCUMULATOR:
            mapping[ACCUMULATOR] += value
            line_number += 1
        elif command == NO_OPERATION:
            line_number += 1
        elif command == JUMP:
            line_number += value
        else:
            raise NotImplementedError("{} operation has not been operation".format(command))

    return mapping[ACCUMULATOR] if line_number == len(instructions) else None
"""
If you are having trouble doing this, follow thee example, it's summation of bags at each stage not
the product :(
"""
def problem_part2(instructions):
    ret = None
    for i, (command, value) in enumerate(instructions):
        if command == ACCUMULATOR:
            continue

        if command == JUMP:
            instructions[i] = (NO_OPERATION, value)
            ret = run_program(instructions)
            if ret is None:
                instructions[i] = (command, value)
            else:
                break
        elif command == NO_OPERATION:
            instructions[i] = (JUMP, value)
            ret = run_program(instructions)
            if ret is None:
                instructions[i] = (command, value)
            else:
                break
    return ret

def day8_main():
    print("2020 AOC Challenge Day 8: Handheld Halting")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = []

    for line in raw_texts:
        if line == "":
            continue
        split_line = line.split(" ")
        lines.append((split_line[0], int(split_line[1])))

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day8_main()
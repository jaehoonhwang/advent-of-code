import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def read_opcode(line):
    def add(a, b, output_index):
        line[output_index] = line[a] + line[b]

    def multiply(a, b, output_index):
        line[output_index] = line[a] * line[b]

    def halt(index):
        return 
    
    valid_opcode = {
        1: add,
        2: multiply,
        99: halt,
    }
    
    i = 0

    while i < len(line) and line[i] != 99:
        op_code, a, b, output_index = line[i], line[i+1], line[i+2], line[i+3]
        if op_code == 99:
            break
        valid_opcode[op_code](a, b, output_index)
        i += 4

def get_fresh_input():
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    numbers = lines[0].split(",")
    numbers = list(map(lambda x: int(x), numbers))

    return numbers

def problem_part1(lines):
    lines[1], lines[2] = 12, 2
    read_opcode(lines)
    return lines[0]

def problem_part2():
    target = 19690720

    for i in range(100):
        for j in range(100):
            print ("curr i: {}, j: {}".format(i, j))
            curr_line = get_fresh_input()
            curr_line[1], curr_line[2] = i, j

            read_opcode(curr_line) 
            if curr_line[0] == target:
                return 100 * i + j
    return

def day2_main():
    print("2019 AOC Challenge Day2")

    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    numbers = lines[0].split(",")
    numbers = list(map(lambda x: int(x), numbers))

    part1_answer = problem_part1(numbers)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2()
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day_main()
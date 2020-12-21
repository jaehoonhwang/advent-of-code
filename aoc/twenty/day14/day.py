import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join


directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"
MASK_KEY = "mask"
MASK_LENGTH = 32
MASK_NOOP = "X"
MASK_UNCHANGED = "0"
MASK_OVERWRITE = "1"

def mask_it(mask, value):
    binary_number = '{:036b}'.format(value)
    current = ""
    for i, ch in enumerate(mask):
        if ch is MASK_NOOP:
            current += binary_number[i]
        else:
            current += mask[i]
    return int(current, 2)

def mask_it2_electric_boogaloo(mask, value):
    binary_number = '{:036b}'.format(value)
    current = ""
    ret = []

    for i, ch in enumerate(mask):
        if ch is MASK_NOOP:
            current += MASK_NOOP
        elif ch is MASK_OVERWRITE:
            current += mask[i]
        else:
            current += binary_number[i]

    noop_index = [index for index, x in enumerate(current) if x == MASK_NOOP]
    noop_count = len(noop_index)

    if not noop_index:
        return [current]

    for i in range(2**noop_count):
        binary = '{:0' + str(noop_count) + 'b}'
        binary = binary.format(i)
        count = 0
        value = ""
        for j, ch in enumerate(current):
            if ch is MASK_NOOP:
                value += binary[count]
                count += 1
            else:
                value += ch
        ret.append(int(value, 2))

    return ret

"""
"""
def problem_part1(ret):
    current_mask = None
    memory = {}
    for mem, value in ret:
        if mem == MASK_KEY:
            current_mask = value
        else:
            memory[mem] = mask_it(current_mask, value)

    return sum(memory.values())

"""
"""
def problem_part2(ret):
    current_mask = None
    memory = {}
    for mem, value in ret:
        if mem == MASK_KEY:
            current_mask = value
        else:
            lst = mask_it2_electric_boogaloo(current_mask, mem)
            for location in lst:
                memory[location] = value
    return sum(memory.values())

def day14_main():
    print("2020 AOC Challenge Day 14: Docking Data")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    ret = []

    for line in raw_texts:
        if line == "":
            continue
        split_lines = line.split(" = ")
        if MASK_KEY in split_lines[0]:
            ret.append((split_lines[0], split_lines[1]))
        else:
            number = int(split_lines[1])
            string = ""
            for ch in split_lines[0]:
                if ch.isalpha() or ch == "[" or ch == "]":
                    continue
                string += ch
            ret.append((int(string), number))

    part1_answer = problem_part1(ret)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(ret)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day14_main()
import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input1.txt"

def inventory_management_system_part1(lines):
    two_counts, three_counts = 0, 0

    for line in lines:
        counts = {}
        for ch in line:
            counts[ch] = counts.get(ch, 0) + 1
        
        two, three = False, False
        for k, v in counts.items():
            if v == 2:
                two = True
            if v == 3:
                three = True
        two_counts += int(two)
        three_counts += int(three)
    
    return two_counts * three_counts

def inventory_management_system_part2(lines):
    pass

def day2_main():
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)

    part1_answer = inventory_management_system_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = inventory_management_system_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day2_main()
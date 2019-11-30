import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input1.txt"

def chronal_calibration_part1(lst, start=0):
    return sum(lst) + start

def chronal_calibration_part2(lst, start=0):
    index = 0 
    length = len(lst)
    current = 0
    seen = {}
    
    while True:
        current += lst[index % length]
        
        if current in seen:
            return current        

        seen[current] = 1        
        index += 1
        

def day1_main():
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    start = 0 

    calibrations = list(map(lambda x: int(x), lines))

    part1_answer = chronal_calibration_part1(calibrations, start)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = chronal_calibration_part2(calibrations, start)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day1_main()
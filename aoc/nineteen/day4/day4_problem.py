import os
import re

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def is_valid(number):
    has_duplicate = False
    is_increasing = True
    string = str(number)
    
    index = 1
    
    while index < len(string):
        if string[index-1] > string[index]:
            is_increasing = False
            return False
        
        if string[index] == string[index-1]:
            has_duplicate = True

        index += 1
    
    return is_increasing and has_duplicate

def is_valid_complicated(number):
    has_duplicate = False
    duplicate_count = 0
    duplicate_number = None
    duplicates = []
    is_increasing = True
    string = str(number)
    
    index = 1
    
    while index < len(string):
        if string[index-1] > string[index]:
            is_increasing = False
            return False
        
        if string[index] == string[index-1]:
            if duplicate_number != string[index]:
                if duplicate_number:
                    duplicates.append((duplicate_number, duplicate_count))
                duplicate_count = 1
                duplicate_number = string[index]
            has_duplicate = True
            duplicate_count += 1

        index += 1

    duplicates.append((duplicate_number, duplicate_count))
    
    return is_increasing and has_duplicate and len([n for n, c in duplicates if c == 2]) >= 1

def problem_part1(number_min, number_max):
    answer = []
    
    for number in range(number_min, number_max):
        if is_valid(number):
            answer.append(number)
    
    return answer

def problem_part2(number_min, number_max):
    answer = []
    
    for number in range(number_min, number_max+1):
        if is_valid_complicated(number):
            answer.append(number)
    
    return len(answer)

def day4_main():
    print("2019 AOC Challenge Day 4")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    number_range = lines[0].split('-')
    num_min, num_max = int(number_range[0]), int(number_range[1])

    print (lines)

    part1_answer = problem_part1(num_min, num_max)
    print("Part 1, Answer: {}".format(len(part1_answer)))

    part2_answer = problem_part2(num_min, num_max)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day_main()
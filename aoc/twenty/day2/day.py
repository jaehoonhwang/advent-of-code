import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

"""
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.
How many passwords are valid according to their policies?
"""
def problem_part1(lines):
    valid_count = 0

    for policy in lines:
        valid_range = policy[0]
        valid_min, valid_max = [int(x) for x in valid_range.split("-")]
        target_letter, password = policy[1], policy[2]
        count = 0
        for char in password:
            if char == target_letter:
                count += 1

        if valid_min <= count <= valid_max:
            valid_count += 1

    return valid_count

"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
"""
def problem_part2(lines):
    valid_count = 0

    for policy in lines:
        valid_range = policy[0]
        left, right = [int(x) - 1 for x in valid_range.split("-")]
        target_letter, password = policy[1], policy[2]
        count = 0

        if password[left] == target_letter:
            count += 1
        if password[right] == target_letter:
            count += 1

        if count == 1:
            valid_count += 1

    return valid_count

def day2_main():
    print("2020 AOC Challenge Day 2: Password Philosophy")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = []
    
    for line in raw_texts:
        split_line = line.split(" ")
        split_line[1] = split_line[1][:-1]
        lines.append(split_line)

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day2_main()
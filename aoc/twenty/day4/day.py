import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

valid_field = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

valid_value = {
    'byr': (1920, 2002),
    'iyr': (2010, 2020),
    'eyr': (2020, 2030),
    'hgt': (150, 193, 59, 76),
    'hcl': (6),
    'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': (9)
}

missing_field = 'cid'
valid_hcl_alpha = ['a', 'b', 'c', 'd', 'e', 'f']

"""
Note: Read questions more carefully, it's asking for VALID passports not invalid.
"""
def problem_part1(passports):
    count = 0
    for passport in passports:
        if passport == {}:
            continue
        lst = [field in passport for field in valid_field]
        if all(lst):
            count += 1

    return count

"""
"""
def problem_part2(passports):
    passports = [passport for passport in passports if all([field in passport for field in valid_field])]
    count = 0
    for passport in passports:
        if validate_fields(passport):
            count += 1
    return count

def validate_fields(passport):
    ret = []
    for key, value in passport.items():
        if key == 'byr':
            ret.append(valid_value[key][0] <= int(value) <= valid_value[key][1])
        elif key == 'iyr':
            ret.append(valid_value[key][0] <= int(value) <= valid_value[key][1])
        elif key == 'eyr':
            ret.append(valid_value[key][0] <= int(value) <= valid_value[key][1])
        elif key == 'hgt':
            height = value[:-2]
            unit = value[-2:]
            if unit == "cm":
                ret.append((valid_value[key][0] <= int(height) <= valid_value[key][1]))
            elif unit == "in":
                ret.append((valid_value[key][2] <= int(height) <= valid_value[key][3]))
            else:
                ret.append(False)
        elif key == 'hcl':
            hash_tag = value[0]
            if hash_tag != '#':
                ret.append(False)
                continue
            else:
                color_value = value[1:]
                if len(color_value) != 6:
                    ret.append(False)
                    continue
                else:
                    ret.append(all([ch.isnumeric() or ch in valid_hcl_alpha for ch in color_value]))
        elif key == 'ecl':
            ret.append(value in valid_value[key])
        elif key == 'pid':
            ret.append(value.isnumeric() and len(value) == 9)

    return all(ret)

def day4_main():
    print("2020 AOC Challenge Day 4: Passport Processing")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    pp = {}
    lines = []

    for i, line in enumerate(raw_texts):
        if not line:
            lines.append(pp)
            pp = {}
            continue
        split_line = line.split(" ")
        kv = list(map(lambda x: x.split(":"), split_line))
        for i in range(len(kv)):
            for j in range(1):
                key = kv[i][j]
                value = kv[i][j+1]
                pp[key] = value

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day4_main()
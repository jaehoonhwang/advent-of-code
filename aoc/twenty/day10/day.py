import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

"""
"""
def problem_part1(jolts):
    jolt_set = set(jolts)

    difference = [1, 2, 3]
    start = min([x for x in difference if x in jolt_set])
    difference_count = [0, 0, 0]
    difference_count[start-1] += 1

    while True:
        temp = start
        for i, number in enumerate(difference):
            if start + number in jolt_set:
                print(difference_count)
                print("{} / added by {} ".format(start, number))
                start += number
                difference_count[i] += 1
                break

        if temp == start:
            break

    print (start)
    return difference_count[0] * (difference_count[2]+1)

"""
"""
def problem_part2(jolts):
    jolt_set = set(jolts)
    jolt_set.add(0)
    ret = [0 for _ in range(max(jolts) + 5)]
    ret[0] = 1
    difference = [1, 2, 3]

    for i in range(max(jolts)+1):
        if i not in jolt_set:
            print ("{} is not being continujed".format(i))
            continue
        for number in difference:
            ret[i+number] += ret[i]

    return ret[max(jolts)]

def day10_main():
    print("2020 AOC Challenge Day 7: Handy Haversacks")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = [int(x) for x in raw_texts if x != '']

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day10_main()
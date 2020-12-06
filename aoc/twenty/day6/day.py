import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join
from string import ascii_lowercase

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

# There is a bug in a read file where it doesn't read last lines

"""
"""
def problem_part1(group):
    count = 0
    print(group)

    for people in group:
        seen = set()
        for questions in people:
            for question in questions:
                seen.add(question)

        count += len(seen)

    return count

"""
"""
def problem_part2(group):
    count = 0

    for people in group:
        seen = set([ch for ch in ascii_lowercase])
        for questions in people:
            seen.intersection_update(set(questions))

        count += len(seen)
    return count

def day6_main():
    print("2020 AOC Challenge Day 6: Custom Custom")
    input_path = path_join(directory_path, input_filename)
    answers = read_file_line(input_path)
    lines = []
    people = []

    for answer in answers:
        if answer == "":
            lines.append(people)
            people = []
        else:
            people.append(answer)

    lines.append(people)

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day6_main()
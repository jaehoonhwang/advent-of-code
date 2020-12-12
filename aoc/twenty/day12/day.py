import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

MAPPING = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
}

MAPPING_DEGREE = {
    "L": 1,
    "R": -1,
}

LIST_DEGREE = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

"""
"""
def problem_part1(directions):
    x, y = 0, 0
    degree = 0

    for direction, value in directions:
        if direction in MAPPING:
            x += MAPPING[direction][0] * value
            y += MAPPING[direction][1] * value
        elif direction in MAPPING_DEGREE:
            if direction == "R":
                degree += 360 - value
            else:
                degree += value
        else:
            degree = degree % 360
            index = degree // 90
            x += LIST_DEGREE[index][0] * value
            y += LIST_DEGREE[index][1] * value

    return abs(x) + abs(y)

"""
"""
def problem_part2(directions):
    x, y = 0, 0
    degree = 0
    wx, wy = 10, 1

    for direction, value in directions:
        if direction in MAPPING:
            wx += MAPPING[direction][0] * value
            wy += MAPPING[direction][1] * value
        elif direction in MAPPING_DEGREE:
            if direction == "R":
                degree += 360 - value
            else:
                degree += value
            degree = degree % 360
            index = degree // 90
            # Do it 90 degrees at a time.
            for _ in range(index):
                wx, wy = -1 * wy, wx
            degree = 0
        else:
            x += wx * value
            y += wy * value
        print ("direction: {} value: {} x: {} y: {} wx: {} wy: {}".format(
            direction, value, x, y, wx, wy))

    return abs(x) + abs(y)

def day12_main():
    print("2020 AOC Challenge Day 12: Boaty McBoatFace")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = [(x[0], int(x[1:])) for x in raw_texts if x != '']

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day12_main()
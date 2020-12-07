import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join
from string import ascii_lowercase

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

start = "shiny gold"
# "Solve it like BFS "
"""
"""
def problem_part1(bags):
    holding = {}
    color_seen = set()
    count = 0
    lst = [start]
    for source, destination_bags in bags:
        for count, color in destination_bags:
            holding[color] = holding.get(color, []) + [source]

    while lst:
        temp = []
        for color in lst:
            if color in color_seen:
                continue
            color_seen.add(color)
            count += 1
            if color in holding:
                temp.extend(holding[color])

        lst = temp

    return len(color_seen) - 1

"""
If you are having trouble doing this, follow thee example, it's summation of bags at each stage not
the product :(
"""
def problem_part2(bags):
    holding = {}
    color_seen = set()
    count = 0
    for source, destination_bags in bags:
        holding[source] = destination_bags

    lst = [(start, 1)]
    while lst:
        temp = []
        for (color, curr) in lst:
            if color not in holding or holding[color] == []:
                continue
            destination_bags = holding[color]
            for bag_count, colores in destination_bags:
                count += curr * bag_count
                temp.append((colores, curr * bag_count))

        lst = temp

    return count

def day7_main():
    print("2020 AOC Challenge Day 7: Handy Haversacks")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = []

    for line in raw_texts[1:]:
        split_line = line.split(" ")
        # Bag Source (Prefix color) and Destina
        source_bag = " ".join(split_line[:2])
        destination_bags = []
        if split_line[4] != "no":
            for i in range(4, len(split_line), 4):
                count = int(split_line[i])
                color = " ".join(split_line[i+1:i+3])
                destination_bags.append((count, color))
        lines.append([source_bag, destination_bags])

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day7_main()
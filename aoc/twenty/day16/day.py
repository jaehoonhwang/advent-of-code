import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

YOUR_TICKET = "your ticket"
NEARBY_TICKET = "nearby ticket"
TRIGGER = "departure"
DEPARTURE_RANGE = (0,5)

def check_valid(valid_ranges, ticket):
    def check_value(range, value):
        min, max = range
        return (min <= value) and (value <= max)
    ret = []
    for value in ticket:
        temp = [False] * len(valid_ranges)
        for i, ranges in enumerate(valid_ranges):
            lst = [check_value(r, value) for r in ranges]
            temp[i] = any(lst)
        if not any(temp):
            ret.append(value)

    return ret

def check_valid_part2(valid_ranges, ticket):
    def check_value(range, value):
        min, max = range
        return (min <= value) and (value <= max)
    ret = []
    for value in ticket:
        valid_indexes = set()
        for i, ranges in enumerate(valid_ranges):
            lst = [check_value(r, value) for r in ranges]
            if any(lst):
                valid_indexes.add(i)
        if len(valid_indexes) != 0:
            ret.append(valid_indexes)

    return ret

"""
"""
def problem_part1(valid_ranges, nearby_tickets):
    ret = []
    for ticket in nearby_tickets:
        invalid = check_valid(valid_ranges, ticket)
        ret.extend(invalid)
    return sum(ret)

def groom_indexes(indexes):
    def unpack_single_indexes(idxs, seen):
        ret = []
        for i, s in enumerate(idxs):
            t = tuple(s)
            if i in seen or len(t) != 1:
                continue
            ret.append((i, t))
        return ret

    seen = set()
    while True:
        single_indexes = unpack_single_indexes(indexes, seen)
        if not single_indexes:
            break
        for i, _ in single_indexes:
            seen.add(i)
        for i, index in enumerate(indexes):
            if i in seen:
                continue
            for _, single in single_indexes:
                indexes[i] = indexes[i].difference(single)
    print (indexes)
    return indexes

"""
"""
def problem_part2(valid_ranges, nearby_tickets, your_ticket):
    valid_tickets = []
    for ticket in nearby_tickets:
        invalid = check_valid(valid_ranges, ticket)
        if len(invalid) == 0:
            valid_tickets.append(ticket)

    valid_indexes = check_valid_part2(valid_ranges, valid_tickets[0])
    print(valid_indexes)

    for ticket in valid_tickets[1:]:
        potentials = check_valid_part2(valid_ranges, ticket)

        for i, indexes in enumerate(valid_indexes):
            potential_set = potentials[i]
            valid_indexes[i] = valid_indexes[i].intersection(potential_set)

    g_indexes= groom_indexes(valid_indexes)
    ret = 1
    for i, s in enumerate(g_indexes):
        number = list(s)[0]
        if DEPARTURE_RANGE[0] <= number <= DEPARTURE_RANGE[1]:
            ret *= your_ticket[i]

    return ret

def day16_main():
    print("2020 AOC Challenge Day 16: T i c k e t t r a n s l a t i o n")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    valid_ranges = []
    your_ticket = []
    nearby_tickets = []
    is_your_ticket = False
    is_near_ticket = False
    for line in raw_texts:
        if line == "":
            continue
        if not is_your_ticket and not is_near_ticket:
            if YOUR_TICKET in line:
                is_your_ticket = True
                continue
            split_line = line.split(":")
            split_range = split_line[1].split(" or ")
            split_number = [l.split("-") for l in split_range]
            temp = []
            for numbers in split_number:
                numbers = [int(x) for x in numbers]
                temp.append((numbers[0], numbers[1]))

            valid_ranges.append(temp)
        elif not is_near_ticket:
            your_ticket  = [int(x) for x in line.split(",")]
            is_near_ticket = True
        else:
            if NEARBY_TICKET in line:
                continue
            near = [int(x) for x in line.split(",")]
            nearby_tickets.append(near)

    part1_answer = problem_part1(valid_ranges, nearby_tickets)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(valid_ranges, nearby_tickets, your_ticket)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day16_main()
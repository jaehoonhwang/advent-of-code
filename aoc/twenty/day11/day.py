import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
ADJACENTS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]
OCCUPIED_LIMIT = 4
OCCUPIED_LIMIT_P2 = 5

def sanity_check(seats, i, j):
    return 0 <= i < len(seats) and  0 <= j < len(seats[0])

def simulate(seats):
    changes = []
    def empty_adjacent(i, j):
        if seats[i][j] != EMPTY_SEAT:
            return
        possible_routes = [(i+I, j+J) for I, J in ADJACENTS if sanity_check(seats, i+I, j+J)]
        seating_length = sum([1 for I, J in possible_routes if seats[I][J] == EMPTY_SEAT or seats[I][J] == FLOOR])
        return len(possible_routes) == seating_length

    def occupied_adjacent(i, j):
        if seats[i][j] != OCCUPIED_SEAT:
            return
        possible_routes = [(i+I, j+J) for I, J in ADJACENTS if sanity_check(seats, i+I, j+J)]
        seating_length = sum([1 for I, J in possible_routes if seats[I][J] == OCCUPIED_SEAT])
        return seating_length >= OCCUPIED_LIMIT

    index = 0
    while True:
        temp = []
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == FLOOR:
                    continue
                ea = empty_adjacent(i, j)
                oa = occupied_adjacent(i, j)
                if ea is not None and ea:
                    temp.append((i, j, OCCUPIED_SEAT))
                elif oa is not None and oa:
                    temp.append((i, j, EMPTY_SEAT))
        for i, j, mark in temp:
            seats[i][j] = mark

        if not temp:
            break
        index += 1

    return seats

def simulate_part2(seats):
    changes = []
    def empty_adjacent2(i, j):
        if seats[i][j] != EMPTY_SEAT:
            return
        evaluated = []
        for x_inc, y_inc in ADJACENTS:
            ii, jj = i+x_inc, j+y_inc
            is_sane = True

            if not sanity_check(seats, ii, jj):
                continue

            while seats[ii][jj] == FLOOR:
                ii, jj = ii + x_inc, jj + y_inc
                if not sanity_check(seats, ii, jj):
                    is_sane = False
                    break
            if is_sane:
                evaluated.append(seats[ii][jj])
            else:
                evaluated.append(FLOOR)

        seating_length = sum([1 for seat in evaluated if seat == OCCUPIED_SEAT])
        return seating_length == 0

    def occupied_adjacent2(i, j):
        if seats[i][j] != OCCUPIED_SEAT:
            return
        evaluated = []
        for x_inc, y_inc in ADJACENTS:
            ii, jj = i+x_inc, j+y_inc
            is_sane = True

            if not sanity_check(seats, ii, jj):
                continue

            while seats[ii][jj] == FLOOR:
                ii, jj = ii + x_inc, jj + y_inc
                if not sanity_check(seats, ii, jj):
                    is_sane = False
                    break
            if is_sane:
                evaluated.append(seats[ii][jj])
            else:
                evaluated.append(FLOOR)

        seating_length = sum([1 for seat in evaluated if seat == OCCUPIED_SEAT])
        return seating_length >= OCCUPIED_LIMIT_P2

    index = 0
    while True:
        temp = []
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == FLOOR:
                    continue
                ea = empty_adjacent2(i, j)
                oa = occupied_adjacent2(i, j)
                if ea is not None and ea:
                    temp.append((i, j, OCCUPIED_SEAT))
                elif oa is not None and oa:
                    temp.append((i, j, EMPTY_SEAT))
        for i, j, mark in temp:
            seats[i][j] = mark

        if not temp:
            break
        index += 1

    return seats
"""
"""
def problem_part1(seats):
    ret = simulate(seats)
    count = 0
    for seat in seats:
        for s in seat:
            if s == OCCUPIED_SEAT:
                count += 1

    return count

"""
"""
def problem_part2(seats):
    ret = simulate_part2(seats)
    count = 0
    for seat in ret:
        for s in seat:
            if s == OCCUPIED_SEAT:
                count += 1
    return count

def day11_main():
    print("2020 AOC Challenge Day 11: Seating System")
    input_path = path_join(directory_path, input_filename)
    raw_texts = read_file_line(input_path)
    lines = [list(x) for x in raw_texts if x != '']

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day11_main()
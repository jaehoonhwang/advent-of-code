import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

row_limit = 128
col_limit = 8
first = 7
last = 3

def binary_search(low, high, index, count, steps):
    mid = (low + high) // 2
    if count == 0:
        return mid

    if steps[index] == "F" or steps[index] == "L":
        return binary_search(low, mid-1, index + 1, count-1, steps)
    elif steps[index] == "B" or steps[index] == "R":
        return binary_search(mid+1, high, index + 1, count-1, steps)
    else:
        raise RuntimeError("UH OH")

def get_seat_number(row, column):
    return row * 8 + column

"""
"""
def problem_part1(seats):
    count = float('-inf')
    for seat in seats:
        rows = seat[:7]
        cols = seat[7:]
        r = binary_search(1, row_limit, 0, first, rows)
        c = binary_search(1, col_limit, 0, last, cols)
        count = max(count, get_seat_number(r, c))
    return count

"""
"""
def problem_part2(seats):
    assigned_seats = []
    for seat in seats:
        rows = seat[:7]
        cols = seat[7:]
        r = binary_search(1, row_limit, 0, first, rows)
        c = binary_search(1, col_limit, 0, last, cols)
        assigned_seats.append((r, c))

    lst = []
    seen_row = set()
    for i in range(row_limit):
        has_seen = 0
        for j in range(col_limit):
            if (i, j) not in assigned_seats:
                lst.append((i, j))
            else:
                has_seen += 1

        if has_seen >= col_limit - 1 or has_seen == 0:
            seen_row.add(i)

    for i, j in lst:
        if i in seen_row:
            continue
        print (i,j)
    return

def day5_main():
    print("2020 AOC Challenge Day 4: Passport Processing")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)

    part1_answer = problem_part1(lines)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(lines)
    print("Part 2, Answer: {}".format(part2_answer))

if __name__ == "__main__":
    day5_main()
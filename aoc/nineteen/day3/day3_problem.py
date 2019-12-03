import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join
from aoc.utils.mathemathics import manhattan_distance

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def mark_map(maps, wire, start):
    current = start

    for direction in wire:
        d, v = direction[0], int(direction[1:]) + 1
        current_start = current
        if d == "L":
            for i in range(1, v):
                x, y = current[0], current[1] - i
                maps[(x, y)] = maps.get((x, y), 0) + 1
            current = (current[0], current[1] - (v - 1))
        elif d == "R":
            for i in range(1, v):
                x, y = current[0], current[1] + i
                maps[(x, y)] = maps.get((x, y), 0) + 1
            current = (current[0], current[1] + (v - 1))
        elif d == "U":
            for i in range(1, v):
                x, y = current[0] - i, current[1]
                maps[(x, y)] = maps.get((x, y), 0) + 1
            current = (current[0] - (v - 1), current[1])
        elif d == "D":
            for i in range(1, v):
                x, y = current[0] + i, current[1]
                maps[(x, y)] = maps.get((x, y), 0) + 1
            current = (current[0] + (v - 1), current[1])
        else:
            raise Exception("THIS SHOULD NOT BE HIT")

def look_around(curr, seen):
    x, y = curr
    l, r = (x-1, y), (x+1, y)
    u, d = (x, y-1), (x, y+1)

    ret = [l, r, u , d]
            
    return [p for p in ret if p in maps and p not in seen]
    
def find_optimal_path(wire, maps, intersection):
    start = ((0, 0), 0, set((0, 0)))
    queue = [start]

    while queue:
        next_queue = []
        for candidate in queue:
            pos, tot, seen = candidate
            if pos == intersection:
                return tot

            potentials = look_around(pos, seen)
            seen.add(pos)

            for potential in potentials:
                next_queue.append((potential, tot + 1, set(seen)))

        queue = next_queue

def graphify(mapping):
    start = (0, 0)
    graphs = {start: []}
    seen = set()
    queue = [start]

    while queue:
        for candidate in queue:
            potentials = look_around(candidate, seen)
            count = 1

            if len(potentials) > 1:
                if candidate not in graph:
                    for potential in potentials:
                        graph[candidate].append((potential, count))
                        graph[potential].append((candidate, count))
                else:
                    

                for potential in potentials:




def problem_part1(wire1, wire2):
    start = (0, 0)
    maps = {}
    maps2 = {}

    mark_map(maps, wire1, start)
    mark_map(maps2, wire2, start)

    curr_min = float('inf')
    for k in maps.keys():
        if k in maps2:
            curr_min = min(manhattan_distance(start, k), curr_min)

    return curr_min

def problem_part2(wire1, wire2):
    start = (0, 0)
    maps = {}
    maps2 = {}

    mark_map(maps, wire1, start)
    mark_map(maps2, wire2, start)

    intersections = []
    for k in maps.keys():
        if k in maps2:
            intersections.append(k)

    ret = []
    for intersection in intersections:
        tots1, tots2 = find_optimal_path(wire1, maps, intersection), find_optimal_path(wire2, maps2, intersection)
        ret.append(tots1 + tots2)
        print(tots1 + tots2)

    return min(ret)

def day3_main():
    print("2019 AOC Challenge Day 3")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    wire1, wire2 = lines[0].split(","), lines[1].split(",")
    
    part1_answer = problem_part1(wire1, wire2)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(wire1, wire2)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day_main()
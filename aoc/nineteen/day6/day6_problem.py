import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"

def graphify(orbits):
    ret = {}

    for source, destination in orbits:
        ret[destination] = ret.get(destination, []) + [source]
        ret[source] = ret.get(source, [])
    
    return ret

def traverse(orbits, start):
    if not orbits[start]:
        return 0

    count = 1 
    current = orbits[start][0]
    
    while orbits[current]:
        current = orbits[current][0]
        count += 1
    
    return count

def traverse_on_steroid(orbits, start):
   if not orbits[start]:
        return 0

   current = orbits[start][0]
   paths = []
   count = 0 
    
   while orbits[current]:
       paths.append(current)
       current = orbits[current][0]
       count += 1
   
   return count, paths

def problem_part1(orbits):
    directed_orbits = graphify(orbits)
    answer = 0

    for planet in directed_orbits.keys():
        answer += traverse(directed_orbits, planet)
    
    return answer

def problem_part2(orbits):
    you_string, santa_string = "YOU", "SAN"
    directed_orbits = graphify(orbits)

    _, you_path = traverse_on_steroid(directed_orbits, you_string)
    _, santa_path = traverse_on_steroid(directed_orbits, santa_string)

    index = 0
    current = None

    while index < len(you_path):
        current = you_path[index]

        if current in santa_path:
            break 

        index += 1
        
    target = current
    you_index = you_path.index(target)
    santa_index = santa_path.index(target)
    
    return you_index + santa_index
    

def parse_line(line):
    source, destination = line.split(")")
    return source, destination

def day6_main():
    print("2019 AOC Challenge Day 6")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    orbits = [parse_line(line) for line in lines]

    part1_answer = problem_part1(orbits)
    print("Part 1, Answer: {}".format(part1_answer))

    part2_answer = problem_part2(orbits)
    print("Part 2, Answer: {}".format(part2_answer))


if __name__ == "__main__":
    day6_main()
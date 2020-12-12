import sys

from aoc.twenty.day1.day import day1_main
from aoc.twenty.day2.day import day2_main
from aoc.twenty.day3.day import day3_main
from aoc.twenty.day4.day import day4_main
from aoc.twenty.day5.day import day5_main
from aoc.twenty.day6.day import day6_main
from aoc.twenty.day7.day import day7_main
from aoc.twenty.day8.day import day8_main
from aoc.twenty.day9.day import day9_main
from aoc.twenty.day10.day import day10_main
from aoc.twenty.day11.day import day11_main
from aoc.twenty.day12.day import day12_main

def main():
    problem_number = sys.argv[1]
    print("2020: Problem number {}".format(problem_number))

    options = {
        "1": day1_main,
        "2": day2_main,
        "3": day3_main,
        "4": day4_main,
        "5": day5_main,
        "6": day6_main,
        "7": day7_main,
        "8": day8_main,
        "9": day9_main,
        "10": day10_main,
        "11": day11_main,
        "12": day12_main,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
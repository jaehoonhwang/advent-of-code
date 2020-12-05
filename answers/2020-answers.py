import sys

from aoc.twenty.day1.day import day1_main
from aoc.twenty.day2.day import day2_main
from aoc.twenty.day3.day import day3_main
from aoc.twenty.day4.day import day4_main
from aoc.twenty.day5.day import day5_main

def main():
    problem_number = sys.argv[1]
    print("2020: Problem number {}".format(problem_number))

    options = {
        "1": day1_main,
        "2": day2_main,
        "3": day3_main,
        "4": day4_main,
        "5": day5_main,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
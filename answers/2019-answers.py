import sys

from aoc.nineteen.day1.day1_problem import day1_main
from aoc.nineteen.day2.day2_problem import day2_main
from aoc.nineteen.day3.day3_problem import day3_main
from aoc.nineteen.day4.day4_problem import day4_main
from aoc.nineteen.day5.day5_problem import day5_main
from aoc.nineteen.day6.day6_problem import day6_main
from aoc.nineteen.day7.day7_problem import day7_main

def main():
    problem_number = sys.argv[1]
    print("2019: Problem nubmer {}".format(problem_number))

    options = {
        "1": day1_main,
        "2": day2_main,
        "3": day3_main,
        "4": day4_main,
        "5": day5_main,
        "6": day6_main,
        "7": day7_main,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
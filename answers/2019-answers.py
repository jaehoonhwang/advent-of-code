import sys

from aoc.nineteen.day1.day1_problem import day1_main
from aoc.nineteen.day2.day2_problem import day2_main
from aoc.nineteen.day3.day3_problem import day3_main

def day1():
    day1_main()

def day2():
    day2_main()

def day3():
    day3_main()

def main():
    problem_number = sys.argv[1]
    print("2019: Problem nubmer {}".format(problem_number))

    options = {
        "1": day1,
        "2": day2,
        "3": day3,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
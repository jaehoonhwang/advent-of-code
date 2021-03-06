import sys

from aoc.eighteen.day1.chronal_calibration import day1_main
from aoc.eighteen.day2.invetory_management_system import day2_main

def day1():
    day1_main()

def day2():
    day2_main()

def main():
    problem_number = sys.argv[1]
    print("2018: Problem nubmer {}".format(problem_number))

    options = {
        "1": day1,
        "2": day2,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
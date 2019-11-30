import sys

from aoc.eighteen.day1.chronal_calibration import day1_main

def day1():
    day1_main()

def main():
    problem_number = sys.argv[1]
    print("2018: Problem nubmer {}".format(problem_number))

    options = {
        "1": day1,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
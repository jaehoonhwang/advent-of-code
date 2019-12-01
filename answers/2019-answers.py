import sys

from aoc.nineteen.day1.day1_problem import day1_main

def day1():
    day1_main()

def main():
    problem_number = sys.argv[1]
    print("2019: Problem nubmer {}".format(problem_number))

    options = {
        "1": day1,
    }
    
    return options.get(problem_number)()

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception("Yeet the arguments; don't have enough.")

    main()
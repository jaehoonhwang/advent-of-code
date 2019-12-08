import os

from aoc.utils.file_reader import read_file_line
from aoc.utils.file_reader import path_join

directory_path = os.path.dirname(os.path.realpath(__file__))
input_filename = "input.txt"
input_value = 1

def handle_1(lst, input_a, input_b, output, is_a_position=True, is_b_position=True, is_ouptut_position=True):
    if input_a < 0 and is_a_position:
        raise Exception(" NOT EXPECTIN DIS: {} ".format(input_a))

    if input_b < 0 and is_b_position:
        raise Exception(" NOT EXPECTIN DIS: {} ".format(input_b))

    a = lst[input_a] if is_a_position else input_a
    b = lst[input_b] if is_b_position else input_b
    output = output

    lst[output] = a + b
    print ("Handle 1: {} {} location: {} output: {}".format(input_a, input_b, output, lst[output]))

def handle_2(lst, input_a, input_b, output, is_a_position=True, is_b_position=True, is_ouptut_position=True):
    if input_a < 0 and is_a_position:
        raise Exception(" NOT EXPECTIN DIS: {} ".format(input_a))

    if input_b < 0 and is_b_position:
        raise Exception(" NOT EXPECTIN DIS: {} ".format(input_b))

    a = lst[input_a] if is_a_position else input_a
    b = lst[input_b] if is_b_position else input_b
    output = output
    lst[output] = a * b
    print ("Handle 2: {} {} location: {} output: {}".format(input_a, input_b, output, lst[output]))

def handle_3(lst, input_a, output, is_a_position=True, is_output_position=True):
    print ("Handle 3: {} output: {}".format(input_a, output))
    lst[output] = input_a

def handle_4(lst, input_a, output):
    print ("Handle 4: output: {}".format(lst[output]))
    return lst[output]

def handle_5(lst, input_a, output, is_a_position=True, is_output_position=True):
    print ("Handle 5: {} output: {} pots: {}".format(input_a, output, output))
    a = lst[input_a] if is_a_position else input_a
    output = lst[output] if is_output_position else output
    return output if a != 0 else 0

def handle_6(lst, input_a, output, is_a_position=True, is_output_position=True):
    print ("Handle 6: {} output: {} pots: {}".format(input_a, output, output))
    a = lst[input_a] if is_a_position else input_a
    output = lst[output] if is_output_position else output
    return output if a == 0 else 0

def handle_7(lst, input_a, input_b, output, is_a_position=True, is_b_position=True,is_ouptut_position=True):
    print ("Handle 7: {} {} location: {} output: {}".format(input_a, input_b, output, lst[output]))
    a = lst[input_a] if is_a_position else input_a
    b = lst[input_b] if is_b_position else input_b
    output = output

    if a < b:
        lst[output] = 1
    else:
        lst[output] = 0

def handle_8(lst, input_a, input_b, output, is_a_position=True, is_b_position=True, is_ouptut_position=True):
    a = lst[input_a] if is_a_position else input_a
    b = lst[input_b] if is_b_position else input_b
    output = output
    print ("Handle 8: {} {} location: {} output: {}".format(a, b, output, lst[output]))

    if a == b:
        lst[output] = 1
    else:
        lst[output] = 0

def handle_99():
    return None

def parse_opcode(number):
    string = str(number)
    string = ("0" * (5 - len(string))) + string
    C, B, A = string[0], string[1], string[2]
    mode = string[-2:]
    
    return int(mode), int(A), int(B), int(C)

def handle_opcode(lst,input_list=[5]):
    current_index = 0
    current_input_index = 0
    input_value = input_list[0]
    ret = []
    print ("input_value: {}".format(input_value))

    op_code = {
        1: handle_1,
        2: handle_2,
        3: handle_3,
        4: handle_4, 
        5: handle_5, 
        6: handle_6, 
        7: handle_7, 
        8: handle_8, 
    }

    while current_index < len(lst):
        command = lst[current_index]
        print ("Current Index: {} and Val: {}".format(current_index, lst[current_index]))
        if command == 1 or command == 2 or command == 7 or command == 8:
            a, b, output = lst[current_index+1], lst[current_index+2], lst[current_index+3]
            op_code[command](lst, a, b, output)
            current_index += 4
        elif command == 3 or command == 4:
            position = lst[current_index+1]
            number = op_code[command](lst, input_value, position)
            current_index += 2
            if command == 4:
                ret.append(number)
        elif command == 5 or command == 6:
            value = lst[current_index+1]
            output = lst[current_index+2]
            number = op_code[command](lst, value, output)
            if number == 0:
                current_index += 3
            else:
                current_index = number
        elif command == 99:
            break
        else:
            mode, A, B, C = parse_opcode(command)
            if mode == 1 or mode == 2 or mode == 7 or mode == 8:
                a, b, output = lst[current_index+1], lst[current_index+2], lst[current_index+3]
                op_code[mode](lst, a, b, output, A == 0, B == 0, C==0)
                current_index += 4
            elif mode == 3 or mode == 4:
                position = lst[current_index+1]
                op_code[mode](lst, input_value, position)
                current_index += 2
                if mode == 4:
                    ret.append(number)
            elif mode == 5 or mode == 6:
                value = lst[current_index+1]
                output = lst[current_index+2]
                number = op_code[mode](lst, value, output, A==0, B==0)
                if number == 0:
                    current_index += 3
                else:
                    current_index = number
            elif mode == 99:
                break
            else:
                print (mode)
                raise NotImplementedError("YET")
    
    return ret[-1]
    
def problem_part1(numbers):
    answer = handle_opcode(numbers)
    return answer

def parse_input(lines):
    return list(map(lambda x: int(x), lines[0].split(",")))

def day5_main():
    print("2019 AOC Challenge Day 5")
    input_path = path_join(directory_path, input_filename)
    lines = read_file_line(input_path)
    numbers = list(map(lambda x: int(x), lines[0].split(",")))

    print (len(numbers))

    part1_answer = problem_part1(numbers)
    print("Part 1, Answer: {}".format(part1_answer))

if __name__ == "__main__":
    day_main()
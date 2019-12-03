#!/usr/bin/env python

def gravity_assist_program(intcode_arr, current_position=0):
    if intcode_arr[current_position] is 99:
        return intcode_arr
    pos_a = intcode_arr[current_position + 1]
    pos_b = intcode_arr[current_position + 2]
    target_position = intcode_arr[current_position + 3]
    if intcode_arr[current_position] is 1:
            intcode_arr[target_position] = intcode_arr[pos_a] + intcode_arr[pos_b]
    elif intcode_arr[current_position] is 2:
            intcode_arr[target_position] = intcode_arr[pos_a] * intcode_arr[pos_b]
    else:
        return[0]
    next_position = current_position + 4
    return gravity_assist_program(intcode_arr, next_position)

def brute_result(intcode_arr, max_val, target_val):
    max_range = range(0, max_val)
    for x in max_range:
        for y in max_range:
            replaced_arr = intcode_arr.copy()
            replaced_arr[1] = x
            replaced_arr[2] = y
            program_output = gravity_assist_program(replaced_arr)[0]
            if program_output == target_val:
                return [x, y]
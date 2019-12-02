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
        print("Unknown OpCode")
    next_position = current_position + 4
    return gravity_assist_program(intcode_arr, next_position)
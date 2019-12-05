#!/usr/bin/env python

def gravity_assist_program_v2(intcode_arr, ip=0):
    mode1 = 0
    mode2 = 0
    if intcode_arr[ip] is 99:
        return intcode_arr
    if intcode_arr[ip] > 99:
        mode1 = int(str(intcode_arr[ip])[-3])
        opcode = int(str(intcode_arr[ip])[-1])
    else:
        opcode = intcode_arr[ip]
    if intcode_arr[ip] > 999:
        mode2 = int(str(intcode_arr[ip])[-4])
    if intcode_arr[ip] > 9999:
        mode1 = int(str(intcode_arr[ip])[-5])
    if mode1:
        a = intcode_arr[ip + 1]
    else:
        a = intcode_arr[intcode_arr[ip + 1]]
    if mode2 and opcode in [1,2]:
        b = intcode_arr[ip + 2]
    elif opcode in [1,2]:
        b = intcode_arr[intcode_arr[ip + 2]]
    if opcode is 1:
            intcode_arr[intcode_arr[ip + 3]] = a + b
            next_ip = ip + 4
    elif opcode is 2:
            intcode_arr[intcode_arr[ip + 3]] = a * b
            next_ip = ip + 4
    elif opcode is 3:
        intcode_arr[intcode_arr[ip + 1]] = 1
        next_ip = ip + 2
    elif opcode is 4:
        print("Opcode 4 output: {}".format(intcode_arr[intcode_arr[ip + 1]]))
        next_ip = ip + 2
    else:
        return [0]
    return gravity_assist_program_v2(intcode_arr, next_ip)
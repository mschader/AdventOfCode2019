#!/usr/bin/env python

def gravity_assist_program_v2(intcode_arr, ip=0):
    opcode = int(f"{intcode_arr[ip] % 100}")
    if opcode is 99:
        return intcode_arr
    mode3, mode2, mode1 = f"{intcode_arr[ip] // 100:03d}"
    mode3 = int(mode3)
    mode2 = int(mode2)
    mode1 = int(mode1)
    if mode1:
        a = intcode_arr[ip + 1]
    else:
        a = intcode_arr[intcode_arr[ip + 1]]
    if mode2 and opcode in [1,2,5,6,7,8]:
        b = intcode_arr[ip + 2]
    elif opcode in [1,2,5,6,7,8]:
        b = intcode_arr[intcode_arr[ip + 2]]

    # Check opcodes from here and to the specific calculations
    if opcode is 1:
            intcode_arr[intcode_arr[ip + 3]] = a + b
            next_ip = ip + 4
    elif opcode is 2:
            intcode_arr[intcode_arr[ip + 3]] = a * b
            next_ip = ip + 4
    elif opcode is 3:
        intcode_arr[intcode_arr[ip + 1]] = int(input("Enter Opcode3 Input > "))
        next_ip = ip + 2
    elif opcode is 4:
        print("Opcode 4 output: {}".format(intcode_arr[intcode_arr[ip + 1]]))
        next_ip = ip + 2
    elif opcode is 5:
        if a:
            next_ip = b
        else:
            next_ip = ip + 3
    elif opcode is 6:
        if not a:
            next_ip = b
        else:
            next_ip = ip + 3
    elif opcode is 7:
        if a < b:
            intcode_arr[intcode_arr[ip + 3]] = 1
        else:
            intcode_arr[intcode_arr[ip + 3]] = 0
        next_ip = ip + 4
    elif opcode is 8:
        if a == b:
            intcode_arr[intcode_arr[ip + 3]] = 1
        else:
            intcode_arr[intcode_arr[ip + 3]] = 0
        next_ip = ip + 4
    else:
        return [0]
    return gravity_assist_program_v2(intcode_arr, next_ip)
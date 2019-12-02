#!/usr/bin/env python
from fuel_calc import get_required_fuel, get_required_fuel_rec

puzzle_input = "input1.txt"
puzzle_input_rec = "input2.txt"

def read_input_to_list(input_file):
    with open(input_file, "r") as f:
        input_list = [line.strip() for line in f]
    return [int(mass) for mass in input_list]

final_fuel = sum(get_required_fuel(num) for num in read_input_to_list(puzzle_input))
final_fuel_rec = sum(get_required_fuel_rec(num) for num in read_input_to_list(puzzle_input_rec))

print("Final Fuel Part One: {}".format(final_fuel))
print("Final Fuel Part Two: {}".format(final_fuel_rec))
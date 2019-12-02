#!/usr/bin/env python
from fuel_calc import get_required_fuel, get_required_fuel_rec

puzzle_input = "input1.txt"
puzzle_input_rec = "input2.txt"

with open(puzzle_input, "r") as f:
    input_list = [line.strip() for line in f]

fuel_list = [get_required_fuel(int(mass)) for mass in input_list]
final_fuel = sum(num for num in fuel_list)

print("Final Fuel Part One: {}".format(final_fuel))

with open(puzzle_input_rec, "r") as f:
    input_list = [line.strip() for line in f]

fuel_list_rec = [get_required_fuel_rec(int(mass)) for mass in input_list]
final_fuel_rec = sum(num for num in fuel_list_rec)

print("Final Fuel Part Two: {}".format(final_fuel_rec))
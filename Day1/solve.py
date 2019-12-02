#!/usr/bin/env python
from fuel_calc import get_required_fuel

puzzle_input = "input1.txt"

with open(puzzle_input, "r") as f:
    input_list = [line.strip() for line in f]

fuel_list = [get_required_fuel(int(mass)) for mass in input_list]
final_fuel = sum(num for num in fuel_list)
print("Final Fuel: {}".format(final_fuel))
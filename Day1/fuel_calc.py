#!/usr/bin/env python

divider = 3
subtractor = 2

def get_required_fuel(mass):
    return (mass // divider) - subtractor

def get_required_fuel_rec(mass):
    required_fuel = (mass // divider) - subtractor
    if required_fuel <= 0:
        return 0
    else:  
        return required_fuel + get_required_fuel_rec(required_fuel)
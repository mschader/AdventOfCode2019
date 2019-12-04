#!/usr/bin/env python

def closest_intersection(wire1, wire2):
    wire1_coordinates = get_wire_coordinates(wire1)
    wire2_coordinates = get_wire_coordinates(wire2)
    wire_intersections = get_wire_intersections(wire1_coordinates, wire2_coordinates)
    closest_result = calc_distance_2D(wire_intersections[0][0], wire_intersections[0][1])
    for i in range(1, len(wire_intersections)):
        current_distance = calc_distance_2D(wire_intersections[i][0], wire_intersections[i][1])
        if current_distance < closest_result:
            closest_result = current_distance
    return closest_result

def cheapest_intersection(wire1, wire2):
    wire1_coordinates = get_wire_coordinates(wire1)
    wire2_coordinates = get_wire_coordinates(wire2)
    wire_intersections = get_wire_intersections(wire1_coordinates, wire2_coordinates)
    current_cost = (get_wire_length(wire_intersections[0], wire1_coordinates) + get_wire_length(wire_intersections[0], wire2_coordinates))
    for i in range(1, len(wire_intersections)):
        new_cost = get_wire_length(wire_intersections[i], wire1_coordinates) + get_wire_length(wire_intersections[i], wire2_coordinates)
        if new_cost < current_cost:
            current_cost = new_cost
    return current_cost

def get_wire_length(coordinate, wire_coords):
    # Calculate +1 because [0,0] index is position 0 but counts as one
    return wire_coords.index(coordinate) + 1

def calc_distance_2D(x, y):
    return abs(x) + abs(y)

def WIRE_UP(current_pos, amount):
    new_coordinates = list()
    for i in range(amount):
        current_pos[1] += 1
        new_coordinates.append(tuple(current_pos.copy()))
    return new_coordinates

def WIRE_RIGHT(current_pos, amount):
    new_coordinates = list()
    for i in range(amount):
        current_pos[0] += 1
        new_coordinates.append(tuple(current_pos.copy()))
    return new_coordinates

def WIRE_DOWN(current_pos, amount):
    new_coordinates = list()
    for i in range(amount):
        current_pos[1] -= 1
        new_coordinates.append(tuple(current_pos.copy()))
    return new_coordinates

def WIRE_LEFT(current_pos, amount):
    new_coordinates = list()
    for i in range(amount):
        current_pos[0] -= 1
        new_coordinates.append(tuple(current_pos.copy()))
    return new_coordinates

def get_wire_coordinates(wire):
    current_pos = [0, 0]
    wire_coordinates = list()
    for entry in wire.split(','):
        direction = entry[0]
        direction_len = int(entry[1:])
        if direction is "U":
            wire_coordinates += WIRE_UP(current_pos, direction_len)
        elif direction is "R":
            wire_coordinates += WIRE_RIGHT(current_pos, direction_len)
        elif direction is "D":
            wire_coordinates += WIRE_DOWN(current_pos, direction_len)
        elif direction is "L":
            wire_coordinates += WIRE_LEFT(current_pos, direction_len)
    return wire_coordinates

def get_wire_intersections(wire1_coords, wire2_coords):
    return list(set(wire1_coords) & set(wire2_coords))
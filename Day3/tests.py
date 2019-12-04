#!/usr/bin/env python
import unittest

from wire_twist import closest_intersection, cheapest_intersection

class TestCountFuel(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(6, closest_intersection("R8,U5,L5,D3", "U7,R6,D4,L4"))
        self.assertEqual(159, closest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"))
        self.assertEqual(135, closest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))

    def test_examples_part_two(self):
        self.assertEqual(30, cheapest_intersection("R8,U5,L5,D3", "U7,R6,D4,L4"))
        self.assertEqual(610, cheapest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"))
        self.assertEqual(410, cheapest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"))

if __name__ == '__main__':
    unittest.main()
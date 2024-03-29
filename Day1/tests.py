#!/usr/bin/env python
import unittest

from fuel_calc import get_required_fuel, get_required_fuel_rec

class TestCountFuel(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(2, get_required_fuel(12))
        self.assertEqual(2, get_required_fuel(14))
        self.assertEqual(654, get_required_fuel(1969))
        self.assertEqual(33583, get_required_fuel(100756))

    def test_examples_par_two(self):
        self.assertEqual(2, get_required_fuel_rec(14))
        self.assertEqual(966, get_required_fuel_rec(1969))
        self.assertEqual(50346, get_required_fuel_rec(100756))

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python
import unittest

from fuel_calc import get_required_fuel

class TestCountFuel(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(2, get_required_fuel(12))
        self.assertEqual(2, get_required_fuel(14))
        self.assertEqual(654, get_required_fuel(1969))
        self.assertEqual(33583, get_required_fuel(100756))

if __name__ == '__main__':
    unittest.main()
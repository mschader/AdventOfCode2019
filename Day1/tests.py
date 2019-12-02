#!/usr/bin/env python
import unittest
import fuel_calc

class TestCountFuel(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(2, get_required_fuel(12))
        self.assertEqual(2, get_required_fuel(14))
        self.assertEqual(654, get_required_fuel(1969))
        self.assertEqual(100756, get_required_fuel(33583))
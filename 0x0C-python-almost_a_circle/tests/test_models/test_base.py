#!/usr/bin/python3
"""
Module test_base
Test the Base class with unittest
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):

    def test_correct_id_cases(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base((1, 2)).id, (1, 2))
        self.assertEqual(Base(True).id, True)

    def test_id_errors(self):
        self.assertRaises(TypeError, Base, name=0)
        self.assertRaises(TypeError, Base, 0, 1)
        self.assertRaises(TypeError, Base, None, None)
        self.assertRaises(TypeError, Base, (1, 2), (2, 3))
        self.assertRaises(TypeError, Base, True, False)

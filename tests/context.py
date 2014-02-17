# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Brian Speir. All rights reserved.
#
# Licensed under The BSD 3-Clause License (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of
# the License at http://opensource.org/licenses/BSD-3-Clause.
#
#

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

import module


class TestCase(unittest.TestCase):
    """Baseclass for all the tests. Use these Pythonic methods for
    testing instead of the camelCase ones in include in unittest.
    """

    def assert_equal(self, first, second, msg=None):
        """Test that first and second are equal. If the values do not
        compare equal, the test will fail."""
        return self.assertEqual(first, second, msg)

    def assert_not_equal(self, first, second, msg=None):
        """Test that first and second are not equal. If the values do
        compare equal, the test will fail."""
        return self.assertNotEqual(first, second, msg=None)

    def assert_true(self, expr, msg=None):
        """Test that an expression is true."""
        self.assertTrue(expr, msg)

    def assert_false(self, expr, msg=None):
        """Test that an expression is true."""
        self.assertFalse(expr, msg)

    def assert_is(self, first, second):
        """Test that first and second evaluate to the same object."""
        self.assertIs(first, second)

    def assert_is_not(self, first, second):
        """Test that first and second don’t evaluate to the same object."""
        self.assertIsNot(first, second)

    def assert_is_none(self, expr):
        """Test that expression is None."""
        self.assertIsNone(expr)

    def assert_is_not_none(self, expr):
        """Test that expression is not None."""
        self.assertIsNotNone(expr)

    def assert_in(self, first, second):
        """Test that first is in second."""
        self.assertIn(first, second)

    def assert_not_in(self, first, second):
        """Test that first is not in second."""
        self.assertNotIn(first, second)

    def assert_is_instance(self, obj, cls):
        """Test that object is an instance of class (which can be a
        class or a tuple of classes, as supported by isinstance()).

        """
        self.assertIsInstance(obj, cls)

    def assert_not_instance(self, obj, cls):
        """Test that object is not an instance of class (which can be a
        class or a tuple of classes, as supported by isinstance()).

        """
        self.assertIsInstance(obj, cls)

    def assert_raises(self, *args, **kwargs):
        """Test that an exception is raised when callable is called with
        any positional or keyword arguments that are also passed to
        assertRaises().

        """
        return self.assertRaises(*args, **kwargs)

    def assert_raises_regexp(self, *args, **kwargs):
        """Like assertRaises() but also tests that regexp matches on the
        string representation of the raised exception.

        """
        return self.assertRaisesRegexp(*args, **kwargs)

    def assert_almost_equal(self, first, second,
                            places=7, msg=None, delta=None):
        """Test that first and second are approximately equal"""
        return self.assertAlmostEqual(first, second, places, msg, delta)

    def assert_not_almost_equal(self, first, second,
                                places=7, msg=None, delta=None):
        """Test that first and second are not approximately equal"""
        return self.assertNotAlmostEqual(first, second, places, msg, delta)

    def assert_greater(self, first, second, msg=None):
        """Test that first is respectively > than second."""
        return self.assertGreater(first, second, msg)

    def assert_greater_equal(self, first, second, msg=None):
        """Test that first is respectively >= than second."""
        return self.assertGreaterEqual(first, second, msg)

    def assert_less(self, first, second, msg=None):
        """Test that first is respectively < than second."""
        return self.assertLess(first, second, msg)

    def assert_less_equal(self, first, second, msg=None):
        """Test that first is respectively <= than second."""
        return self.assertLessEqual(first, second, msg)

    def assert_regexp_matches(self, text, regexp, msg=None):
        """Test that a regexp search matches text."""
        return self.assertRegexpMatches(self, text, regexp, msg)

    def assert_not_regexp_matches(self, text, regexp, msg=None):
        """Test that a regexp search does not match text."""
        return self.assertNotRegexpMatches(self, text, regexp, msg)

    def assert_items_equal(self, actual, expected, msg=None):
        """Test that sequence expected contains the same elements as
        actual, regardless of their order.

        """
        return self.assertItemsEqual(actual, expected, msg)

    def assertDictContainsSubset(self, expected, actual, msg=None):
        """Tests whether the key/value pairs in dictionary actual are a
        superset of those in expected.

        """
        return self.assertDictContainsSubset(expected, actual, msg)

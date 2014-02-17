# -*- coding: utf-8 -*-

#
# Copyright (C) 2014 Brian Speir. All rights reserved.
#
# Licensed under The BSD 3-Clause License (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of
# the License at http://opensource.org/licenses/BSD-3-Clause.
#
#

import unittest

from .context import TestCase, module


class BasicTestSuite(TestCase):
    """Basic test cases."""

    def test_gravity(self):
        assert True


if __name__ == '__main__':
    unittest.main()

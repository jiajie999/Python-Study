#!/usr/bin/env python

file_name = 'Maximal_Rectangle'
func_name = 'maximalRectangle'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)(["1"])

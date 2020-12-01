#! /usr/bin/env python
# -*-coding: utf-8 -*-

"""
function: calculate run time with function
"""

import time


def cal_time(func):
    def run_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s exec: %.3fs" %(func.__name__, end-start))
        return result
    return run_time

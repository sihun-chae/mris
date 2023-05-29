import sys
import os

path_parent = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
path_grandparent = os.path.dirname(path_parent)

sys.path.append(path_grandparent)
from test_suite import test

def set_tests():
    test.append_i_type("slti", 12, 25, 0x0, -0x81, -0x800)
    test.append_i_type("slti", 5, 5, 0x1, -0x1001, 0x0)
    test.append_i_type("slti", 28, 4, 0x1, -0x40000000, 0x7ff)
    test.append_i_type("slti", 15, 31, 0x1, -0x11, 0x1)
    test.append_i_type("slti", 13, 1, 0x1, -0x80000000, 0x3)
    test.append_i_type("slti", 1, 15, 0x1, 0x0, 0x2)
    test.append_i_type("slti", 9, 16, 0x0, 0x7fffffff, -0x8)
    test.append_i_type("slti", 31, 11, 0x0, 0x1, -0x400)
    test.append_i_type("slti", 27, 14, 0x0, 0x10, 0x10)
    test.append_i_type("slti", 26, 12, 0x0, 0x33333334, 0x4)
    test.append_i_type("slti", 4, 17, 0x0, 0x3fffffff, 0x8)
    test.append_i_type("slti", 10, 18, 0x1, -0x2001, 0x20)
    test.append_i_type("slti", 21, 27, 0x1, 0x3, 0x40)
    test.append_i_type("slti", 8, 3, 0x0, 0x55555554, 0x80)
    test.append_i_type("slti", 0, 7, 0, 0x55555554, 0x100)
    test.append_i_type("slti", 24, 22, 0x1, -0x55555556, 0x200)
    test.append_i_type("slti", 18, 24, 0x0, 0x4000, 0x400)
    test.append_i_type("slti", 25, 6, 0x1, -0x401, -0x2)
    test.append_i_type("slti", 23, 21, 0x0, 0x66666667, -0x3)
    test.append_i_type("slti", 7, 0, 0x0, 0x0, -0x5)
    test.append_i_type("slti", 20, 10, 0x1, -0xb504, -0x9)
    test.append_i_type("slti", 16, 26, 0x0, 0x3fffffff, -0x11)
    test.append_i_type("slti", 29, 20, 0x1, -0x80001, -0x21)
    test.append_i_type("slti", 3, 13, 0x1, -0x10000001, -0x41)
    test.append_i_type("slti", 14, 29, 0x0, 0x800000, -0x81)
    test.append_i_type("slti", 2, 23, 0x1, -0x10000001, -0x101)
    test.append_i_type("slti", 22, 2, 0x0, 0x0, -0x201)
    test.append_i_type("slti", 19, 30, 0x1, -0x40001, -0x401)
    test.append_i_type("slti", 11, 19, 0x1, 0x4, 0x555)
    test.append_i_type("slti", 30, 8, 0x1, -0x40000000, -0x556)
    test.append_i_type("slti", 17, 9, 0x1, 0x2, 0x7ff)
    test.append_i_type("slti", 6, 28, 0x0, 0x8, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x20, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x40, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x80, 0x200)
    test.append_i_type("slti", 11, 10, 0x0, 0x100, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x200, -0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x400, -0x101)
    test.append_i_type("slti", 11, 10, 0x0, 0x800, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x1000, -0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x2000, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x8000, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x10000, -0x1)
    test.append_i_type("slti", 11, 10, 0x0, 0x20000, -0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x40000, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x80000, -0x41)
    test.append_i_type("slti", 11, 10, 0x0, 0x100000, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x200000, -0x11)
    test.append_i_type("slti", 11, 10, 0x0, 0x400000, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x1000000, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x2000000, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x4000000, -0x41)
    test.append_i_type("slti", 11, 10, 0x0, 0x8000000, 0x7ff)
    test.append_i_type("slti", 11, 10, 0x0, 0x10000000, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x20000000, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x40000000, -0x11)
    test.append_i_type("slti", 11, 10, 0x1, -0x2, 0x1)
    test.append_i_type("slti", 11, 10, 0x0, -0x3, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0x5, 0x100)
    test.append_i_type("slti", 11, 10, 0x1, -0x9, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, -0x21, 0x1)
    test.append_i_type("slti", 11, 10, 0x1, -0x41, -0x4)
    test.append_i_type("slti", 11, 10, 0x0, -0x101, -0x800)
    test.append_i_type("slti", 11, 10, 0x1, -0x201, 0x9)
    test.append_i_type("slti", 11, 10, 0x1, -0x801, -0x8)
    test.append_i_type("slti", 11, 10, 0x1, -0x4001, 0x400)
    test.append_i_type("slti", 11, 10, 0x1, -0x8001, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, -0x10001, -0x101)
    test.append_i_type("slti", 11, 10, 0x1, -0x20001, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, -0x200001, -0x6)
    test.append_i_type("slti", 11, 10, 0x1, -0x400001, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0x800001, 0x7)
    test.append_i_type("slti", 11, 10, 0x1, -0x1000001, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0x2000001, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, -0x4000001, -0x4)
    test.append_i_type("slti", 11, 10, 0x1, -0x8000001, 0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0x20000001, 0x10)
    test.append_i_type("slti", 11, 10, 0x1, -0x40000001, -0x101)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x3, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x3, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555555, 0x2e)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x666)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x554)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x667)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555556, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x5, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x5, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333333, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666666, 0x2e)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x666)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x554)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x667)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0xb504, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0xb504, 0x2e)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x2, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x2, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x2, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x2, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x2, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x2, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x2, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555554, 0x2e)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x0, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666667, 0x2e)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x666)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x554)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x667)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0xb503, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0xb505, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x0, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x0, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x0, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x0, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x0, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x4, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x4, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333332, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x66666665, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0xb503, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x4)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x332)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x665)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x6)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x334)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, -0x2c)
    test.append_i_type("slti", 11, 10, 0x0, 0x55555556, 0x2e)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, -0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x666)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x2d)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x554)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x556)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, -0x555)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x667)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, -0x55555555, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, 0x3)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, 0x5)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x333)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, -0x2d)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, 0x2)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, 0x0)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, 0x4)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x332)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x665)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, -0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, 0x6)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x334)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x667)
    test.append_i_type("slti", 11, 10, 0x0, 0x6, -0x2c)
    test.append_i_type("slti", 11, 10, 0x1, 0x6, 0x2e)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x3)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x555)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, -0x556)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x5)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x333)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x666)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, -0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x2d)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x2)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x554)
    test.append_i_type("slti", 11, 10, 0x0, 0x33333334, 0x0)
    test.append_i_type("slti", 11, 10, 0x1, -0x100001, -0x5)
    test.append_ecall()
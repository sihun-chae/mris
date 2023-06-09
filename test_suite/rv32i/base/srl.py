import sys
import os

path_parent = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
path_grandparent = os.path.dirname(path_parent)

sys.path.append(path_grandparent)
from test_suite import test

def set_tests():
    test.append_r_type("srl", 11, 26, 11, 0x1ff7f, -0x400001, 0xf)
    test.append_r_type("srl", 12, 31, 31, 0x155, 0x55555556, 0x55555556)
    test.append_r_type("srl", 7, 7, 7, 0x1, -0x1, -0x1)
    test.append_r_type("srl", 18, 18, 12, 0x100, 0x100, 0x0)
    test.append_r_type("srl", 8, 14, 3, 0x0, 0x9, 0x9)
    test.append_r_type("srl", 20, 21, 22, 0x80000, -0x80000000, 0xc)
    test.append_r_type("srl", 30, 4, 17, 0x0, 0x0, 0xf)
    test.append_r_type("srl", 6, 1, 4, 0x1, 0x7fffffff, 0x1e)
    test.append_r_type("srl", 15, 0, 21, 0x0, 0x0, 0x1d)
    test.append_r_type("srl", 5, 28, 23, 0x0, 0x2, 0x6)
    test.append_r_type("srl", 4, 9, 30, 0x0, 0x4, 0xa)
    test.append_r_type("srl", 10, 13, 29, 0x2, 0x8, 0x2)
    test.append_r_type("srl", 25, 2, 16, 0x0, 0x10, 0x7)
    test.append_r_type("srl", 19, 11, 28, 0x0, 0x20, 0x8)
    test.append_r_type("srl", 23, 10, 6, 0x0, 0x40, 0xb)
    test.append_r_type("srl", 0, 3, 1, 0, 0x80, 0x6)
    test.append_r_type("srl", 14, 6, 8, 0x0, 0x200, 0xe)
    test.append_r_type("srl", 9, 20, 27, 0x0, 0x400, 0x1d)
    test.append_r_type("srl", 16, 30, 18, 0x0, 0x800, 0xd)
    test.append_r_type("srl", 24, 22, 10, 0x10, 0x1000, 0x8)
    test.append_r_type("srl", 2, 15, 24, 0x2, 0x2000, 0xc)
    test.append_r_type("srl", 21, 17, 9, 0x80, 0x4000, 0x7)
    test.append_r_type("srl", 27, 12, 20, 0x0, 0x8000, 0x1f)
    test.append_r_type("srl", 26, 27, 5, 0x2000, 0x10000, 0x3)
    test.append_r_type("srl", 17, 16, 13, 0x200, 0x20000, 0x8)
    test.append_r_type("srl", 28, 23, 15, 0x4, 0x40000, 0x10)
    test.append_r_type("srl", 1, 8, 26, 0x4000, 0x80000, 0x5)
    test.append_r_type("srl", 29, 24, 2, 0x0, 0x100000, 0x17)
    test.append_r_type("srl", 31, 29, 14, 0x20, 0x200000, 0x10)
    test.append_r_type("srl", 22, 5, 19, 0x10000, 0x400000, 0x6)
    test.append_r_type("srl", 3, 19, 0, 0x800000, 0x800000, 0x0)
    test.append_r_type("srl", 8, 25, 4, 0x0, 0x1000000, 0x1e)
    test.append_r_type("srl", 30, 6, 25, 0x0, 0x2000000, 0x1d)
    test.append_r_type("srl", 13, 12, 9, 0x0, 0x4000000, 0x1e)
    test.append_r_type("srl", 12, 10, 11, 0x80000, 0x8000000, 0x8)
    test.append_r_type("srl", 12, 10, 11, 0x10000, 0x10000000, 0xc)
    test.append_r_type("srl", 12, 10, 11, 0x4, 0x20000000, 0x1b)
    test.append_r_type("srl", 12, 10, 11, 0x1000000, 0x40000000, 0x6)
    test.append_r_type("srl", 12, 10, 11, 0x1fffff, -0x2, 0xb)
    test.append_r_type("srl", 12, 10, 11, 0x1fff, -0x3, 0x13)
    test.append_r_type("srl", 12, 10, 11, 0x3ffffffe, -0x5, 0x2)
    test.append_r_type("srl", 12, 10, 11, 0x1fff, -0x9, 0x13)
    test.append_r_type("srl", 12, 10, 11, 0x1ff, -0x11, 0x17)
    test.append_r_type("srl", 12, 10, 11, 0x1ffff, -0x21, 0xf)
    test.append_r_type("srl", 12, 10, 11, 0x3ffff, -0x41, 0xe)
    test.append_r_type("srl", 12, 10, 11, 0x3fffffd, -0x81, 0x6)
    test.append_r_type("srl", 12, 10, 11, 0x3ffff, -0x101, 0xe)
    test.append_r_type("srl", 12, 10, 11, 0x7ffff, -0x201, 0xd)
    test.append_r_type("srl", 12, 10, 11, 0x1f, -0x401, 0x1b)
    test.append_r_type("srl", 12, 10, 11, 0x1f, -0x801, 0x1b)
    test.append_r_type("srl", 12, 10, 11, 0x7ffff, -0x1001, 0xd)
    test.append_r_type("srl", 12, 10, 11, 0xffffd, -0x2001, 0xc)
    test.append_r_type("srl", 12, 10, 11, 0xffff, -0x4001, 0x10)
    test.append_r_type("srl", 12, 10, 11, 0x3, -0x8001, 0x1e)
    test.append_r_type("srl", 12, 10, 11, 0x3fff, -0x10001, 0x12)
    test.append_r_type("srl", 12, 10, 11, 0x1, -0x20001, 0x1f)
    test.append_r_type("srl", 12, 10, 11, 0x1fff7, -0x40001, 0xf)
    test.append_r_type("srl", 12, 10, 11, 0x1f, -0x80001, 0x1b)
    test.append_r_type("srl", 12, 10, 11, 0x3ffbfff, -0x100001, 0x6)
    test.append_r_type("srl", 12, 10, 11, 0x3fdf, -0x800001, 0x12)
    test.append_r_type("srl", 12, 10, 11, 0x7f7f, -0x1000001, 0x11)
    test.append_r_type("srl", 12, 10, 11, 0xfdfff, -0x2000001, 0xc)
    test.append_r_type("srl", 12, 10, 11, 0x1f7, -0x4000001, 0x17)
    test.append_r_type("srl", 12, 10, 11, 0x7bffffff, -0x8000001, 0x1)
    test.append_r_type("srl", 12, 10, 11, 0x77ffff, -0x10000001, 0x9)
    test.append_r_type("srl", 12, 10, 11, 0x6ffff, -0x20000001, 0xd)
    test.append_r_type("srl", 12, 10, 11, 0xbfffff, -0x40000001, 0x8)
    test.append_r_type("srl", 12, 10, 11, 0xaaaaa, 0x55555555, 0xb)
    test.append_r_type("srl", 12, 10, 11, 0x5, -0x55555556, 0x1d)
    test.append_r_type("srl", 12, 10, 11, 0x0, 0x3, 0x3)
    test.append_r_type("srl", 12, 10, 11, 0x0, 0x5, 0xf)
    test.append_r_type("srl", 12, 10, 11, 0xccccc, 0x33333333, 0xa)
    test.append_r_type("srl", 12, 10, 11, 0xccc, 0x66666666, 0x13)
    test.append_r_type("srl", 12, 10, 11, 0x0, 0xb505, 0x1f)
    test.append_r_type("srl", 12, 10, 11, 0x0, 0x6, 0x4)
    test.append_r_type("srl", 12, 10, 11, 0x7ef, -0x2000001, 0x15)
    test.append_r_type("srl", 12, 10, 11, 0xffff4, -0xb504, 0xc)
    test.append_r_type("srl", 12, 10, 11, 0x0, 0xb504, 0x1d)
    test.append_r_type("srl", 12, 10, 11, 0x2aa, 0x55555554, 0x15)
    test.append_r_type("srl", 12, 10, 11, 0x3ff7f, -0x200001, 0xe)
    test.append_r_type("srl", 12, 10, 11, 0x33333332, 0x33333332, 0x0)
    test.append_r_type("srl", 12, 10, 11, 0xccccccc, 0x66666665, 0x3)
    test.append_r_type("srl", 12, 10, 11, 0x5a81, 0xb503, 0x1)
    test.append_r_type("srl", 12, 10, 11, 0x155555, -0x55555555, 0xb)
    test.append_r_type("srl", 12, 10, 11, 0x6, 0x33333334, 0x1b)
    test.append_r_type("srl", 12, 10, 11, 0x1999999, 0x66666667, 0x6)
    test.append_r_type("srl", 12, 10, 11, 0x3fffd2b, -0xb503, 0x6)
    test.append_r_type("srl", 12, 10, 11, 0x555555, 0x55555556, 0x8)
    test.append_r_type("srl", 12, 10, 11, 0xffffffff, -0x1, 0x0)
    test.append_r_type("srl", 12, 10, 11, 0x0, 0x1, 0x1d)
    test.append_r_type("srl", 12, 10, 11, 0x2, 0x80, 0x6)
    test.append_r_type("srl", 12, 10, 11, 0x400000, 0x800000, 0x1)
    test.append_ecall()
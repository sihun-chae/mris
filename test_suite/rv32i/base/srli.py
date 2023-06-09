import sys
import os

path_parent = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
path_grandparent = os.path.dirname(path_parent)

sys.path.append(path_grandparent)
from test_suite import test

def set_tests():
    test.append_i_type("srli", 8, 30, 0x3fffd2bf, -0xb504, 0x2)
    test.append_i_type("srli", 17, 17, 0x0, 0x7, 0x13)
    test.append_i_type("srli", 19, 27, 0xffff4afc, -0xb504, 0x0)
    test.append_i_type("srli", 9, 29, 0x3fffffff, 0x3fffffff, 0x0)
    test.append_i_type("srli", 22, 25, 0x1, -0xa, 0x1f)
    test.append_i_type("srli", 13, 1, 0x0, 0x200, 0x1f)
    test.append_i_type("srli", 0, 21, 0, 0x3, 0x3)
    test.append_i_type("srli", 29, 0, 0x0, 0x0, 0x9)
    test.append_i_type("srli", 18, 16, 0x0, 0x0, 0x1)
    test.append_i_type("srli", 27, 20, 0x3fff, 0x7fffffff, 0x11)
    test.append_i_type("srli", 2, 31, 0x0, 0x1, 0x12)
    test.append_i_type("srli", 31, 7, 0x0, 0x2, 0x1d)
    test.append_i_type("srli", 16, 14, 0x0, 0x4, 0xf)
    test.append_i_type("srli", 25, 12, 0x0, 0x8, 0x1b)
    test.append_i_type("srli", 11, 4, 0x0, 0x10, 0xf)
    test.append_i_type("srli", 23, 24, 0x0, 0x20, 0x17)
    test.append_i_type("srli", 28, 8, 0x0, 0x40, 0xd)
    test.append_i_type("srli", 30, 15, 0x0, 0x80, 0x1e)
    test.append_i_type("srli", 20, 18, 0x0, 0x100, 0x1f)
    test.append_i_type("srli", 14, 13, 0x0, 0x400, 0x12)
    test.append_i_type("srli", 3, 11, 0x0, 0x800, 0xf)
    test.append_i_type("srli", 26, 23, 0x0, 0x1000, 0xf)
    test.append_i_type("srli", 10, 19, 0x800, 0x2000, 0x2)
    test.append_i_type("srli", 21, 10, 0x1, 0x4000, 0xe)
    test.append_i_type("srli", 7, 5, 0x1000, 0x8000, 0x3)
    test.append_i_type("srli", 5, 2, 0x0, 0x10000, 0x17)
    test.append_i_type("srli", 6, 28, 0x1, 0x20000, 0x11)
    test.append_i_type("srli", 12, 3, 0x800, 0x40000, 0x7)
    test.append_i_type("srli", 4, 26, 0x0, 0x80000, 0x1d)
    test.append_i_type("srli", 24, 9, 0x40000, 0x100000, 0x2)
    test.append_i_type("srli", 15, 6, 0x10000, 0x200000, 0x5)
    test.append_i_type("srli", 1, 22, 0x400, 0x400000, 0xc)
    test.append_i_type("srli", 11, 10, 0x4000, 0x800000, 0x9)
    test.append_i_type("srli", 11, 10, 0x400, 0x1000000, 0xe)
    test.append_i_type("srli", 11, 10, 0x400000, 0x2000000, 0x3)
    test.append_i_type("srli", 11, 10, 0x400000, 0x4000000, 0x4)
    test.append_i_type("srli", 11, 10, 0x100000, 0x8000000, 0x7)
    test.append_i_type("srli", 11, 10, 0x200000, 0x10000000, 0x7)
    test.append_i_type("srli", 11, 10, 0x20000000, 0x20000000, 0x0)
    test.append_i_type("srli", 11, 10, 0x1, 0x40000000, 0x1e)
    test.append_i_type("srli", 11, 10, 0x7, -0x2, 0x1d)
    test.append_i_type("srli", 11, 10, 0x1fffff, -0x3, 0xb)
    test.append_i_type("srli", 11, 10, 0x7ffffff, -0x5, 0x5)
    test.append_i_type("srli", 11, 10, 0x7ffffffb, -0x9, 0x1)
    test.append_i_type("srli", 11, 10, 0x7, -0x11, 0x1d)
    test.append_i_type("srli", 11, 10, 0xffff, -0x21, 0x10)
    test.append_i_type("srli", 11, 10, 0xffffff, -0x41, 0x8)
    test.append_i_type("srli", 11, 10, 0x3fff, -0x81, 0x12)
    test.append_i_type("srli", 11, 10, 0x1fffffdf, -0x101, 0x3)
    test.append_i_type("srli", 11, 10, 0x1fff, -0x201, 0x13)
    test.append_i_type("srli", 11, 10, 0x7ffffd, -0x401, 0x9)
    test.append_i_type("srli", 11, 10, 0x1ffffef, -0x801, 0x7)
    test.append_i_type("srli", 11, 10, 0xffffefff, -0x1001, 0x0)
    test.append_i_type("srli", 11, 10, 0x3ffff, -0x2001, 0xe)
    test.append_i_type("srli", 11, 10, 0x7fffdfff, -0x4001, 0x1)
    test.append_i_type("srli", 11, 10, 0x7, -0x8001, 0x1d)
    test.append_i_type("srli", 11, 10, 0x7fff7f, -0x10001, 0x9)
    test.append_i_type("srli", 11, 10, 0x1fffbff, -0x20001, 0x7)
    test.append_i_type("srli", 11, 10, 0x1fff, -0x40001, 0x13)
    test.append_i_type("srli", 11, 10, 0x1ffef, -0x80001, 0xf)
    test.append_i_type("srli", 11, 10, 0xffef, -0x100001, 0x10)
    test.append_i_type("srli", 11, 10, 0x3ff7fff, -0x200001, 0x6)
    test.append_i_type("srli", 11, 10, 0xffbfff, -0x400001, 0x8)
    test.append_i_type("srli", 11, 10, 0x3fdfff, -0x800001, 0xa)
    test.append_i_type("srli", 11, 10, 0x1fdfff, -0x1000001, 0xb)
    test.append_i_type("srli", 11, 10, 0x7effffff, -0x2000001, 0x1)
    test.append_i_type("srli", 11, 10, 0x7df, -0x4000001, 0x15)
    test.append_i_type("srli", 11, 10, 0x7bf, -0x8000001, 0x15)
    test.append_i_type("srli", 11, 10, 0x3bfff, -0x10000001, 0xe)
    test.append_i_type("srli", 11, 10, 0x37ffffff, -0x20000001, 0x2)
    test.append_i_type("srli", 11, 10, 0x2fff, -0x40000001, 0x12)
    test.append_i_type("srli", 11, 10, 0xaaa, 0x55555555, 0x13)
    test.append_i_type("srli", 11, 10, 0xaaaaa, -0x55555556, 0xc)
    test.append_i_type("srli", 11, 10, 0x0, 0x5, 0x3)
    test.append_i_type("srli", 11, 10, 0xcc, 0x66666667, 0x17)
    test.append_i_type("srli", 11, 10, 0x3fffd2, -0xb503, 0xa)
    test.append_i_type("srli", 11, 10, 0x5, 0xb505, 0xd)
    test.append_i_type("srli", 11, 10, 0x33333, 0x33333333, 0xc)
    test.append_i_type("srli", 11, 10, 0x333, 0x66666666, 0x15)
    test.append_i_type("srli", 11, 10, 0x1, 0xb504, 0xf)
    test.append_i_type("srli", 11, 10, 0x2, 0x55555554, 0x1d)
    test.append_i_type("srli", 11, 10, 0x6, 0x33333332, 0x1b)
    test.append_i_type("srli", 11, 10, 0x333333, 0x66666665, 0x9)
    test.append_i_type("srli", 11, 10, 0x0, 0xb503, 0x12)
    test.append_i_type("srli", 11, 10, 0xaaaa, 0x55555556, 0xf)
    test.append_i_type("srli", 11, 10, 0x5, -0x55555555, 0x1d)
    test.append_i_type("srli", 11, 10, 0x0, 0x6, 0x1f)
    test.append_i_type("srli", 11, 10, 0xcccccc, 0x33333334, 0x6)
    test.append_i_type("srli", 11, 10, 0x0, 0x3, 0x3)
    test.append_i_type("srli", 11, 10, 0x400000, -0x80000000, 0x9)
    test.append_ecall()
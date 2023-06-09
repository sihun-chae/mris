import sys
import os

path_parent = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
path_grandparent = os.path.dirname(path_parent)

sys.path.append(path_grandparent)
from test_suite import test

def set_tests():
    test.append_i_type("slli", 27, 17, 0xe0000000, -0x40000001, 0x1d)
    test.append_i_type("slli", 26, 26, 0x33330000, 0x66666666, 0xf)
    test.append_i_type("slli", 11, 22, 0xfffeffff, -0x10001, 0x0)
    test.append_i_type("slli", 6, 15, 0x4, 0x4, 0x0)
    test.append_i_type("slli", 16, 9, 0x80000000, -0x400001, 0x1f)
    test.append_i_type("slli", 20, 11, 0x0, 0x4, 0x1f)
    test.append_i_type("slli", 19, 1, 0x800, 0x8, 0x8)
    test.append_i_type("slli", 25, 19, 0x0, -0x80000000, 0x10)
    test.append_i_type("slli", 12, 8, 0x0, 0x0, 0xc)
    test.append_i_type("slli", 30, 27, 0xffffff00, 0x7fffffff, 0x8)
    test.append_i_type("slli", 4, 2, 0x2, 0x1, 0x1)
    test.append_i_type("slli", 14, 31, 0x80, 0x2, 0x6)
    test.append_i_type("slli", 17, 24, 0x40000, 0x10, 0xe)
    test.append_i_type("slli", 10, 4, 0x100, 0x20, 0x3)
    test.append_i_type("slli", 2, 18, 0x8000000, 0x40, 0x15)
    test.append_i_type("slli", 23, 5, 0x10000000, 0x80, 0x15)
    test.append_i_type("slli", 8, 13, 0x200, 0x100, 0x1)
    test.append_i_type("slli", 0, 20, 0, 0x200, 0x0)
    test.append_i_type("slli", 9, 16, 0x1000, 0x400, 0x2)
    test.append_i_type("slli", 5, 21, 0x40000000, 0x800, 0x13)
    test.append_i_type("slli", 1, 23, 0x80000, 0x1000, 0x7)
    test.append_i_type("slli", 18, 12, 0x20000000, 0x2000, 0x10)
    test.append_i_type("slli", 15, 29, 0x2000000, 0x4000, 0xb)
    test.append_i_type("slli", 21, 3, 0x0, 0x8000, 0x17)
    test.append_i_type("slli", 31, 0, 0x0, 0x0, 0x1)
    test.append_i_type("slli", 3, 14, 0x0, 0x20000, 0x1b)
    test.append_i_type("slli", 24, 25, 0x0, 0x40000, 0x1f)
    test.append_i_type("slli", 29, 30, 0x0, 0x80000, 0xf)
    test.append_i_type("slli", 13, 28, 0x0, 0x100000, 0x17)
    test.append_i_type("slli", 7, 10, 0x10000000, 0x200000, 0x7)
    test.append_i_type("slli", 22, 7, 0x0, 0x400000, 0x1d)
    test.append_i_type("slli", 28, 6, 0x2000000, 0x800000, 0x2)
    test.append_i_type("slli", 11, 10, 0x40000000, 0x1000000, 0x6)
    test.append_i_type("slli", 11, 10, 0x40000000, 0x2000000, 0x5)
    test.append_i_type("slli", 11, 10, 0x0, 0x4000000, 0x11)
    test.append_i_type("slli", 11, 10, 0x8000000, 0x8000000, 0x0)
    test.append_i_type("slli", 11, 10, 0x80000000, 0x10000000, 0x3)
    test.append_i_type("slli", 11, 10, 0x0, 0x20000000, 0xc)
    test.append_i_type("slli", 11, 10, 0x0, 0x40000000, 0xb)
    test.append_i_type("slli", 11, 10, 0xffff8000, -0x2, 0xe)
    test.append_i_type("slli", 11, 10, 0xfffffffa, -0x3, 0x1)
    test.append_i_type("slli", 11, 10, 0xfffffd80, -0x5, 0x7)
    test.append_i_type("slli", 11, 10, 0xffffdc00, -0x9, 0xa)
    test.append_i_type("slli", 11, 10, 0xffde0000, -0x11, 0x11)
    test.append_i_type("slli", 11, 10, 0xfff7c000, -0x21, 0xe)
    test.append_i_type("slli", 11, 10, 0xfdf80000, -0x41, 0x13)
    test.append_i_type("slli", 11, 10, 0xff7f0000, -0x81, 0x10)
    test.append_i_type("slli", 11, 10, 0xfff7f800, -0x101, 0xb)
    test.append_i_type("slli", 11, 10, 0xfbfe0000, -0x201, 0x11)
    test.append_i_type("slli", 11, 10, 0xfffdff80, -0x401, 0x7)
    test.append_i_type("slli", 11, 10, 0xfbff8000, -0x801, 0xf)
    test.append_i_type("slli", 11, 10, 0xffbffc00, -0x1001, 0xa)
    test.append_i_type("slli", 11, 10, 0xfff7ffc0, -0x2001, 0x6)
    test.append_i_type("slli", 11, 10, 0xfffefffc, -0x4001, 0x2)
    test.append_i_type("slli", 11, 10, 0xfffbfff8, -0x8001, 0x3)
    test.append_i_type("slli", 11, 10, 0xe0000000, -0x20001, 0x1d)
    test.append_i_type("slli", 11, 10, 0xe0000000, -0x40001, 0x1d)
    test.append_i_type("slli", 11, 10, 0x7ffff000, -0x80001, 0xc)
    test.append_i_type("slli", 11, 10, 0xf7ffffc0, -0x200001, 0x6)
    test.append_i_type("slli", 11, 10, 0xfff80000, -0x800001, 0x13)
    test.append_i_type("slli", 11, 10, 0xfffe0000, -0x1000001, 0x11)
    test.append_i_type("slli", 11, 10, 0xffff8000, -0x2000001, 0xf)
    test.append_i_type("slli", 11, 10, 0xffffe000, -0x4000001, 0xd)
    test.append_i_type("slli", 11, 10, 0xffffc000, -0x8000001, 0xe)
    test.append_i_type("slli", 11, 10, 0xffffff80, -0x10000001, 0x7)
    test.append_i_type("slli", 11, 10, 0xfffff800, -0x20000001, 0xb)
    test.append_i_type("slli", 11, 10, 0xaaaa0000, 0x55555555, 0x11)
    test.append_i_type("slli", 11, 10, 0x55000000, -0x55555556, 0x17)
    test.append_i_type("slli", 11, 10, 0x180000, 0x3, 0x13)
    test.append_i_type("slli", 11, 10, 0xa, 0x5, 0x1)
    test.append_i_type("slli", 11, 10, 0x99999998, 0x33333333, 0x3)
    test.append_i_type("slli", 11, 10, 0xffd2bf00, -0xb504, 0x6)
    test.append_i_type("slli", 11, 10, 0x33800000, 0x66666667, 0x17)
    test.append_i_type("slli", 11, 10, 0xffd2bf40, -0xb503, 0x6)
    test.append_i_type("slli", 11, 10, 0x80000000, 0xb505, 0x1f)
    test.append_i_type("slli", 11, 10, 0x33333320, 0x33333332, 0x4)
    test.append_i_type("slli", 11, 10, 0x80000000, -0x6, 0x1e)
    test.append_i_type("slli", 11, 10, 0x5a8200, 0xb504, 0x7)
    test.append_i_type("slli", 11, 10, 0xefffff00, -0x100001, 0x8)
    test.append_i_type("slli", 11, 10, 0xaaaaaaa0, 0x55555554, 0x3)
    test.append_i_type("slli", 11, 10, 0x66650000, 0x66666665, 0x10)
    test.append_i_type("slli", 11, 10, 0xb5030000, 0xb503, 0x10)
    test.append_i_type("slli", 11, 10, 0xab000000, 0x55555556, 0x17)
    test.append_i_type("slli", 11, 10, 0xaaaac000, -0x55555555, 0xe)
    test.append_i_type("slli", 11, 10, 0x80000000, 0x6, 0x1e)
    test.append_i_type("slli", 11, 10, 0x80000000, 0x33333334, 0x1d)
    test.append_i_type("slli", 11, 10, 0x200, 0x200, 0x0)
    test.append_i_type("slli", 11, 10, 0x20000, 0x10000, 0x1)
    test.append_ecall()
import sys
import os

path_parent = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
path_grandparent = os.path.dirname(path_parent)

sys.path.append(path_grandparent)
from test_suite import test

def set_tests():
    test.append_i_type("ori", 22, 5, 0xfffffdff, -0x201, -0x800)
    test.append_i_type("ori", 27, 27, 0x0, 0x0, 0x0)
    test.append_i_type("ori", 8, 17, 0x333337ff, 0x33333334, 0x7ff)
    test.append_i_type("ori", 1, 20, 0xffff4afd, -0xb504, 0x1)
    test.append_i_type("ori", 19, 12, 0x8000002d, -0x80000000, 0x2d)
    test.append_i_type("ori", 3, 8, 0x7fffffff, 0x7fffffff, 0x555)
    test.append_i_type("ori", 26, 28, 0x667, 0x1, 0x667)
    test.append_i_type("ori", 23, 16, 0xffffffff, 0x7, -0x7)
    test.append_i_type("ori", 31, 25, 0x40002, 0x40000, 0x2)
    test.append_i_type("ori", 11, 23, 0x20000004, 0x20000000, 0x4)
    test.append_i_type("ori", 17, 14, 0xfffffdff, -0x201, 0x8)
    test.append_i_type("ori", 7, 31, 0x12, 0x2, 0x10)
    test.append_i_type("ori", 4, 21, 0x8020, 0x8000, 0x20)
    test.append_i_type("ori", 5, 15, 0x840, 0x800, 0x40)
    test.append_i_type("ori", 25, 30, 0xfffbffff, -0x40001, 0x80)
    test.append_i_type("ori", 30, 11, 0xfffffffb, -0x5, 0x100)
    test.append_i_type("ori", 10, 4, 0xfff7ffff, -0x80001, 0x200)
    test.append_i_type("ori", 0, 13, 0, -0x40000001, 0x400)
    test.append_i_type("ori", 6, 26, 0xffffffff, -0x21, -0x2)
    test.append_i_type("ori", 18, 19, 0xffffffff, 0xb503, -0x3)
    test.append_i_type("ori", 21, 7, 0xfffffffb, 0x10000000, -0x5)
    test.append_i_type("ori", 16, 24, 0xffffffff, -0x80001, -0x9)
    test.append_i_type("ori", 9, 0, 0xffffffef, 0x0, -0x11)
    test.append_i_type("ori", 28, 3, 0xffffffdf, 0x2000, -0x21)
    test.append_i_type("ori", 15, 1, 0xffffffff, 0x55555556, -0x41)
    test.append_i_type("ori", 2, 18, 0xffffffff, -0xb504, -0x81)
    test.append_i_type("ori", 20, 22, 0xfffffeff, -0x55555556, -0x101)
    test.append_i_type("ori", 13, 6, 0xfffffdff, 0x1000000, -0x201)
    test.append_i_type("ori", 14, 29, 0xfffffbff, 0x20000000, -0x401)
    test.append_i_type("ori", 12, 2, 0xfffffafe, -0xb504, -0x556)
    test.append_i_type("ori", 24, 9, 0x5, 0x4, 0x5)
    test.append_i_type("ori", 29, 10, 0xe, 0x8, 0x6)
    test.append_i_type("ori", 11, 10, 0x210, 0x10, 0x200)
    test.append_i_type("ori", 11, 10, 0x2c, 0x20, 0x2c)
    test.append_i_type("ori", 11, 10, 0x43, 0x40, 0x3)
    test.append_i_type("ori", 11, 10, 0xa0, 0x80, 0x20)
    test.append_i_type("ori", 11, 10, 0xffffffbf, 0x100, -0x41)
    test.append_i_type("ori", 11, 10, 0xfffffffa, 0x200, -0x6)
    test.append_i_type("ori", 11, 10, 0xffffffd3, 0x400, -0x2d)
    test.append_i_type("ori", 11, 10, 0x1005, 0x1000, 0x5)
    test.append_i_type("ori", 11, 10, 0x4665, 0x4000, 0x665)
    test.append_i_type("ori", 11, 10, 0x10009, 0x10000, 0x9)
    test.append_i_type("ori", 11, 10, 0x20200, 0x20000, 0x200)
    test.append_i_type("ori", 11, 10, 0x80000, 0x80000, 0x0)
    test.append_i_type("ori", 11, 10, 0x100200, 0x100000, 0x200)
    test.append_i_type("ori", 11, 10, 0xffffffd4, 0x200000, -0x2c)
    test.append_i_type("ori", 11, 10, 0xfffffdff, 0x400000, -0x201)
    test.append_i_type("ori", 11, 10, 0x800080, 0x800000, 0x80)
    test.append_i_type("ori", 11, 10, 0xffffffdf, 0x2000000, -0x21)
    test.append_i_type("ori", 11, 10, 0x4000010, 0x4000000, 0x10)
    test.append_i_type("ori", 11, 10, 0x8000554, 0x8000000, 0x554)
    test.append_i_type("ori", 11, 10, 0xfffffffa, 0x40000000, -0x6)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x2, -0x41)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x3, -0x9)
    test.append_i_type("ori", 11, 10, 0xfffffff7, -0x9, -0x800)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x11, -0x2d)
    test.append_i_type("ori", 11, 10, 0xffffffbf, -0x41, -0x556)
    test.append_i_type("ori", 11, 10, 0xffffff7f, -0x81, 0x665)
    test.append_i_type("ori", 11, 10, 0xfffffeff, -0x101, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x401, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffff7ff, -0x801, 0x7ff)
    test.append_i_type("ori", 11, 10, 0xffffefff, -0x1001, 0x7)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x2001, -0x21)
    test.append_i_type("ori", 11, 10, 0xffff7fff, -0x8001, 0x2d)
    test.append_i_type("ori", 11, 10, 0xfffeffff, -0x10001, 0x332)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x20001, -0xa)
    test.append_i_type("ori", 11, 10, 0xffefffff, -0x100001, 0x6)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x200001, -0x400)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x400001, -0x2c)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x800001, -0xa)
    test.append_i_type("ori", 11, 10, 0xfeffffff, -0x1000001, 0x3ff)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x2000001, -0x8)
    test.append_i_type("ori", 11, 10, 0xfbffffff, -0x4000001, 0x4)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x8000001, -0x6)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x10000001, -0x7)
    test.append_i_type("ori", 11, 10, 0xdfffffff, -0x20000001, 0x554)
    test.append_i_type("ori", 11, 10, 0xffffffff, 0x55555555, -0x101)
    test.append_i_type("ori", 11, 10, 0x3, 0x3, 0x3)
    test.append_i_type("ori", 11, 10, 0x557, 0x3, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaab, 0x3, -0x556)
    test.append_i_type("ori", 11, 10, 0x7, 0x3, 0x5)
    test.append_i_type("ori", 11, 10, 0x333, 0x3, 0x333)
    test.append_i_type("ori", 11, 10, 0x667, 0x3, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd3, 0x3, -0x2d)
    test.append_i_type("ori", 11, 10, 0x2f, 0x3, 0x2d)
    test.append_i_type("ori", 11, 10, 0x3, 0x3, 0x2)
    test.append_i_type("ori", 11, 10, 0x557, 0x3, 0x554)
    test.append_i_type("ori", 11, 10, 0x3, 0x3, 0x0)
    test.append_i_type("ori", 11, 10, 0x7, 0x3, 0x4)
    test.append_i_type("ori", 11, 10, 0x333, 0x3, 0x332)
    test.append_i_type("ori", 11, 10, 0x667, 0x3, 0x665)
    test.append_i_type("ori", 11, 10, 0x2f, 0x3, 0x2c)
    test.append_i_type("ori", 11, 10, 0x557, 0x3, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaab, 0x3, -0x555)
    test.append_i_type("ori", 11, 10, 0x7, 0x3, 0x6)
    test.append_i_type("ori", 11, 10, 0x337, 0x3, 0x334)
    test.append_i_type("ori", 11, 10, 0x667, 0x3, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x3, -0x2c)
    test.append_i_type("ori", 11, 10, 0x2f, 0x3, 0x2e)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555555, 0x3)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555555, 0x555)
    test.append_i_type("ori", 11, 10, 0xffffffff, 0x55555555, -0x556)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555555, 0x5)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555555, 0x333)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555555, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x55555555, -0x2d)
    test.append_i_type("ori", 11, 10, 0x5555557d, 0x55555555, 0x2d)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555555, 0x2)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555555, 0x554)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555555, 0x0)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555555, 0x4)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555555, 0x332)
    test.append_i_type("ori", 11, 10, 0x55555775, 0x55555555, 0x665)
    test.append_i_type("ori", 11, 10, 0x5555557d, 0x55555555, 0x2c)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555555, 0x556)
    test.append_i_type("ori", 11, 10, 0xffffffff, 0x55555555, -0x555)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555555, 0x6)
    test.append_i_type("ori", 11, 10, 0x55555775, 0x55555555, 0x334)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555555, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd5, 0x55555555, -0x2c)
    test.append_i_type("ori", 11, 10, 0x5555557f, 0x55555555, 0x2e)
    test.append_i_type("ori", 11, 10, 0xaaaaaaab, -0x55555556, 0x3)
    test.append_i_type("ori", 11, 10, 0xaaaaafff, -0x55555556, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaaa, -0x55555556, -0x556)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555556, 0x5)
    test.append_i_type("ori", 11, 10, 0xaaaaabbb, -0x55555556, 0x333)
    test.append_i_type("ori", 11, 10, 0xaaaaaeee, -0x55555556, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffffb, -0x55555556, -0x2d)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555556, 0x2d)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaa, -0x55555556, 0x2)
    test.append_i_type("ori", 11, 10, 0xaaaaaffe, -0x55555556, 0x554)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaa, -0x55555556, 0x0)
    test.append_i_type("ori", 11, 10, 0xaaaaaaae, -0x55555556, 0x4)
    test.append_i_type("ori", 11, 10, 0xaaaaabba, -0x55555556, 0x332)
    test.append_i_type("ori", 11, 10, 0xaaaaaeef, -0x55555556, 0x665)
    test.append_i_type("ori", 11, 10, 0xaaaaaaae, -0x55555556, 0x2c)
    test.append_i_type("ori", 11, 10, 0xaaaaaffe, -0x55555556, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaab, -0x55555556, -0x555)
    test.append_i_type("ori", 11, 10, 0xaaaaaaae, -0x55555556, 0x6)
    test.append_i_type("ori", 11, 10, 0xaaaaabbe, -0x55555556, 0x334)
    test.append_i_type("ori", 11, 10, 0xaaaaaeef, -0x55555556, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffffe, -0x55555556, -0x2c)
    test.append_i_type("ori", 11, 10, 0xaaaaaaae, -0x55555556, 0x2e)
    test.append_i_type("ori", 11, 10, 0x7, 0x5, 0x3)
    test.append_i_type("ori", 11, 10, 0x555, 0x5, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaaf, 0x5, -0x556)
    test.append_i_type("ori", 11, 10, 0x5, 0x5, 0x5)
    test.append_i_type("ori", 11, 10, 0x337, 0x5, 0x333)
    test.append_i_type("ori", 11, 10, 0x667, 0x5, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x5, -0x2d)
    test.append_i_type("ori", 11, 10, 0x2d, 0x5, 0x2d)
    test.append_i_type("ori", 11, 10, 0x7, 0x5, 0x2)
    test.append_i_type("ori", 11, 10, 0x555, 0x5, 0x554)
    test.append_i_type("ori", 11, 10, 0x5, 0x5, 0x0)
    test.append_i_type("ori", 11, 10, 0x5, 0x5, 0x4)
    test.append_i_type("ori", 11, 10, 0x337, 0x5, 0x332)
    test.append_i_type("ori", 11, 10, 0x665, 0x5, 0x665)
    test.append_i_type("ori", 11, 10, 0x2d, 0x5, 0x2c)
    test.append_i_type("ori", 11, 10, 0x557, 0x5, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaaf, 0x5, -0x555)
    test.append_i_type("ori", 11, 10, 0x7, 0x5, 0x6)
    test.append_i_type("ori", 11, 10, 0x335, 0x5, 0x334)
    test.append_i_type("ori", 11, 10, 0x667, 0x5, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd5, 0x5, -0x2c)
    test.append_i_type("ori", 11, 10, 0x2f, 0x5, 0x2e)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333333, 0x3)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333333, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffbbb, 0x33333333, -0x556)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333333, 0x5)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333333, 0x333)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333333, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffff3, 0x33333333, -0x2d)
    test.append_i_type("ori", 11, 10, 0x3333333f, 0x33333333, 0x2d)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333333, 0x2)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333333, 0x554)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333333, 0x0)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333333, 0x4)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333333, 0x332)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333333, 0x665)
    test.append_i_type("ori", 11, 10, 0x3333333f, 0x33333333, 0x2c)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333333, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffbbb, 0x33333333, -0x555)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333333, 0x6)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333333, 0x334)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333333, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffff7, 0x33333333, -0x2c)
    test.append_i_type("ori", 11, 10, 0x3333333f, 0x33333333, 0x2e)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666666, 0x3)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666666, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffeee, 0x66666666, -0x556)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666666, 0x5)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666666, 0x333)
    test.append_i_type("ori", 11, 10, 0x66666666, 0x66666666, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffff7, 0x66666666, -0x2d)
    test.append_i_type("ori", 11, 10, 0x6666666f, 0x66666666, 0x2d)
    test.append_i_type("ori", 11, 10, 0x66666666, 0x66666666, 0x2)
    test.append_i_type("ori", 11, 10, 0x66666776, 0x66666666, 0x554)
    test.append_i_type("ori", 11, 10, 0x66666666, 0x66666666, 0x0)
    test.append_i_type("ori", 11, 10, 0x66666666, 0x66666666, 0x4)
    test.append_i_type("ori", 11, 10, 0x66666776, 0x66666666, 0x332)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666666, 0x665)
    test.append_i_type("ori", 11, 10, 0x6666666e, 0x66666666, 0x2c)
    test.append_i_type("ori", 11, 10, 0x66666776, 0x66666666, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffeef, 0x66666666, -0x555)
    test.append_i_type("ori", 11, 10, 0x66666666, 0x66666666, 0x6)
    test.append_i_type("ori", 11, 10, 0x66666776, 0x66666666, 0x334)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666666, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffff6, 0x66666666, -0x2c)
    test.append_i_type("ori", 11, 10, 0x6666666e, 0x66666666, 0x2e)
    test.append_i_type("ori", 11, 10, 0xffff4aff, -0xb504, 0x3)
    test.append_i_type("ori", 11, 10, 0xffff4ffd, -0xb504, 0x555)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb504, 0x5)
    test.append_i_type("ori", 11, 10, 0xffff4bff, -0xb504, 0x333)
    test.append_i_type("ori", 11, 10, 0xffff4efe, -0xb504, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0xb504, -0x2d)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb504, 0x2d)
    test.append_i_type("ori", 11, 10, 0xffff4afe, -0xb504, 0x2)
    test.append_i_type("ori", 11, 10, 0xffff4ffc, -0xb504, 0x554)
    test.append_i_type("ori", 11, 10, 0xffff4afc, -0xb504, 0x0)
    test.append_i_type("ori", 11, 10, 0xffff4afc, -0xb504, 0x4)
    test.append_i_type("ori", 11, 10, 0xffff4bfe, -0xb504, 0x332)
    test.append_i_type("ori", 11, 10, 0xffff4efd, -0xb504, 0x665)
    test.append_i_type("ori", 11, 10, 0xffff4afc, -0xb504, 0x2c)
    test.append_i_type("ori", 11, 10, 0xffff4ffe, -0xb504, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaff, -0xb504, -0x555)
    test.append_i_type("ori", 11, 10, 0xffff4afe, -0xb504, 0x6)
    test.append_i_type("ori", 11, 10, 0xffff4bfc, -0xb504, 0x334)
    test.append_i_type("ori", 11, 10, 0xffff4eff, -0xb504, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffffc, -0xb504, -0x2c)
    test.append_i_type("ori", 11, 10, 0xffff4afe, -0xb504, 0x2e)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb504, 0x3)
    test.append_i_type("ori", 11, 10, 0xb555, 0xb504, 0x555)
    test.append_i_type("ori", 11, 10, 0xffffffae, 0xb504, -0x556)
    test.append_i_type("ori", 11, 10, 0xb505, 0xb504, 0x5)
    test.append_i_type("ori", 11, 10, 0xb737, 0xb504, 0x333)
    test.append_i_type("ori", 11, 10, 0xb766, 0xb504, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0xb504, -0x2d)
    test.append_i_type("ori", 11, 10, 0xb52d, 0xb504, 0x2d)
    test.append_i_type("ori", 11, 10, 0xb506, 0xb504, 0x2)
    test.append_i_type("ori", 11, 10, 0xb554, 0xb504, 0x554)
    test.append_i_type("ori", 11, 10, 0xb504, 0xb504, 0x0)
    test.append_i_type("ori", 11, 10, 0xb504, 0xb504, 0x4)
    test.append_i_type("ori", 11, 10, 0xb736, 0xb504, 0x332)
    test.append_i_type("ori", 11, 10, 0xb765, 0xb504, 0x665)
    test.append_i_type("ori", 11, 10, 0xb52c, 0xb504, 0x2c)
    test.append_i_type("ori", 11, 10, 0xb556, 0xb504, 0x556)
    test.append_i_type("ori", 11, 10, 0xffffffaf, 0xb504, -0x555)
    test.append_i_type("ori", 11, 10, 0xb506, 0xb504, 0x6)
    test.append_i_type("ori", 11, 10, 0xb734, 0xb504, 0x334)
    test.append_i_type("ori", 11, 10, 0xb767, 0xb504, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd4, 0xb504, -0x2c)
    test.append_i_type("ori", 11, 10, 0xb52e, 0xb504, 0x2e)
    test.append_i_type("ori", 11, 10, 0x3, 0x2, 0x3)
    test.append_i_type("ori", 11, 10, 0x557, 0x2, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaaa, 0x2, -0x556)
    test.append_i_type("ori", 11, 10, 0x7, 0x2, 0x5)
    test.append_i_type("ori", 11, 10, 0x333, 0x2, 0x333)
    test.append_i_type("ori", 11, 10, 0x666, 0x2, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd3, 0x2, -0x2d)
    test.append_i_type("ori", 11, 10, 0x2f, 0x2, 0x2d)
    test.append_i_type("ori", 11, 10, 0x2, 0x2, 0x2)
    test.append_i_type("ori", 11, 10, 0x556, 0x2, 0x554)
    test.append_i_type("ori", 11, 10, 0x2, 0x2, 0x0)
    test.append_i_type("ori", 11, 10, 0x6, 0x2, 0x4)
    test.append_i_type("ori", 11, 10, 0x332, 0x2, 0x332)
    test.append_i_type("ori", 11, 10, 0x667, 0x2, 0x665)
    test.append_i_type("ori", 11, 10, 0x2e, 0x2, 0x2c)
    test.append_i_type("ori", 11, 10, 0x556, 0x2, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaab, 0x2, -0x555)
    test.append_i_type("ori", 11, 10, 0x6, 0x2, 0x6)
    test.append_i_type("ori", 11, 10, 0x336, 0x2, 0x334)
    test.append_i_type("ori", 11, 10, 0x667, 0x2, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd6, 0x2, -0x2c)
    test.append_i_type("ori", 11, 10, 0x2e, 0x2, 0x2e)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555554, 0x3)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555554, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffffe, 0x55555554, -0x556)
    test.append_i_type("ori", 11, 10, 0x55555555, 0x55555554, 0x5)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555554, 0x333)
    test.append_i_type("ori", 11, 10, 0x55555776, 0x55555554, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x55555554, -0x2d)
    test.append_i_type("ori", 11, 10, 0x5555557d, 0x55555554, 0x2d)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555554, 0x2)
    test.append_i_type("ori", 11, 10, 0x55555554, 0x55555554, 0x554)
    test.append_i_type("ori", 11, 10, 0x55555554, 0x55555554, 0x0)
    test.append_i_type("ori", 11, 10, 0x55555554, 0x55555554, 0x4)
    test.append_i_type("ori", 11, 10, 0x55555776, 0x55555554, 0x332)
    test.append_i_type("ori", 11, 10, 0x55555775, 0x55555554, 0x665)
    test.append_i_type("ori", 11, 10, 0x5555557c, 0x55555554, 0x2c)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555554, 0x556)
    test.append_i_type("ori", 11, 10, 0xffffffff, 0x55555554, -0x555)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555554, 0x6)
    test.append_i_type("ori", 11, 10, 0x55555774, 0x55555554, 0x334)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555554, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd4, 0x55555554, -0x2c)
    test.append_i_type("ori", 11, 10, 0x5555557e, 0x55555554, 0x2e)
    test.append_i_type("ori", 11, 10, 0x3, 0x0, 0x3)
    test.append_i_type("ori", 11, 10, 0x555, 0x0, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaaa, 0x0, -0x556)
    test.append_i_type("ori", 11, 10, 0x5, 0x0, 0x5)
    test.append_i_type("ori", 11, 10, 0x333, 0x0, 0x333)
    test.append_i_type("ori", 11, 10, 0x666, 0x0, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd3, 0x0, -0x2d)
    test.append_i_type("ori", 11, 10, 0x33333336, 0x33333334, 0x332)
    test.append_i_type("ori", 11, 10, 0x33333775, 0x33333334, 0x665)
    test.append_i_type("ori", 11, 10, 0x3333333c, 0x33333334, 0x2c)
    test.append_i_type("ori", 11, 10, 0x33333776, 0x33333334, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffbbf, 0x33333334, -0x555)
    test.append_i_type("ori", 11, 10, 0x33333336, 0x33333334, 0x6)
    test.append_i_type("ori", 11, 10, 0x33333334, 0x33333334, 0x334)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333334, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffff4, 0x33333334, -0x2c)
    test.append_i_type("ori", 11, 10, 0x3333333e, 0x33333334, 0x2e)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x3)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666667, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffeef, 0x66666667, -0x556)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x5)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666667, 0x333)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffff7, 0x66666667, -0x2d)
    test.append_i_type("ori", 11, 10, 0x6666666f, 0x66666667, 0x2d)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x2)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666667, 0x554)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x0)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x4)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666667, 0x332)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x665)
    test.append_i_type("ori", 11, 10, 0x6666666f, 0x66666667, 0x2c)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666667, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffeef, 0x66666667, -0x555)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x6)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666667, 0x334)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666667, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffff7, 0x66666667, -0x2c)
    test.append_i_type("ori", 11, 10, 0x6666666f, 0x66666667, 0x2e)
    test.append_i_type("ori", 11, 10, 0xffff4aff, -0xb503, 0x3)
    test.append_i_type("ori", 11, 10, 0xffff4ffd, -0xb503, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaff, -0xb503, -0x556)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb503, 0x5)
    test.append_i_type("ori", 11, 10, 0xffff4bff, -0xb503, 0x333)
    test.append_i_type("ori", 11, 10, 0xffff4eff, -0xb503, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0xb503, -0x2d)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb503, 0x2d)
    test.append_i_type("ori", 11, 10, 0xffff4aff, -0xb503, 0x2)
    test.append_i_type("ori", 11, 10, 0xffff4ffd, -0xb503, 0x554)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb503, 0x0)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb503, 0x4)
    test.append_i_type("ori", 11, 10, 0xffff4bff, -0xb503, 0x332)
    test.append_i_type("ori", 11, 10, 0xffff4efd, -0xb503, 0x665)
    test.append_i_type("ori", 11, 10, 0xffff4afd, -0xb503, 0x2c)
    test.append_i_type("ori", 11, 10, 0xffff4fff, -0xb503, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaff, -0xb503, -0x555)
    test.append_i_type("ori", 11, 10, 0xffff4aff, -0xb503, 0x6)
    test.append_i_type("ori", 11, 10, 0xffff4bfd, -0xb503, 0x334)
    test.append_i_type("ori", 11, 10, 0xffff4eff, -0xb503, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffffd, -0xb503, -0x2c)
    test.append_i_type("ori", 11, 10, 0xffff4aff, -0xb503, 0x2e)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb505, 0x3)
    test.append_i_type("ori", 11, 10, 0xb555, 0xb505, 0x555)
    test.append_i_type("ori", 11, 10, 0xffffffaf, 0xb505, -0x556)
    test.append_i_type("ori", 11, 10, 0xb505, 0xb505, 0x5)
    test.append_i_type("ori", 11, 10, 0xb737, 0xb505, 0x333)
    test.append_i_type("ori", 11, 10, 0xb767, 0xb505, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0xb505, -0x2d)
    test.append_i_type("ori", 11, 10, 0xb52d, 0xb505, 0x2d)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb505, 0x2)
    test.append_i_type("ori", 11, 10, 0xb555, 0xb505, 0x554)
    test.append_i_type("ori", 11, 10, 0xb505, 0xb505, 0x0)
    test.append_i_type("ori", 11, 10, 0xb505, 0xb505, 0x4)
    test.append_i_type("ori", 11, 10, 0xb737, 0xb505, 0x332)
    test.append_i_type("ori", 11, 10, 0xb765, 0xb505, 0x665)
    test.append_i_type("ori", 11, 10, 0xb52d, 0xb505, 0x2c)
    test.append_i_type("ori", 11, 10, 0xb557, 0xb505, 0x556)
    test.append_i_type("ori", 11, 10, 0xffffffaf, 0xb505, -0x555)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb505, 0x6)
    test.append_i_type("ori", 11, 10, 0xb735, 0xb505, 0x334)
    test.append_i_type("ori", 11, 10, 0xb767, 0xb505, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd5, 0xb505, -0x2c)
    test.append_i_type("ori", 11, 10, 0xb52f, 0xb505, 0x2e)
    test.append_i_type("ori", 11, 10, 0x2d, 0x0, 0x2d)
    test.append_i_type("ori", 11, 10, 0x2, 0x0, 0x2)
    test.append_i_type("ori", 11, 10, 0x554, 0x0, 0x554)
    test.append_i_type("ori", 11, 10, 0x4, 0x0, 0x4)
    test.append_i_type("ori", 11, 10, 0x332, 0x0, 0x332)
    test.append_i_type("ori", 11, 10, 0x665, 0x0, 0x665)
    test.append_i_type("ori", 11, 10, 0x2c, 0x0, 0x2c)
    test.append_i_type("ori", 11, 10, 0x556, 0x0, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaab, 0x0, -0x555)
    test.append_i_type("ori", 11, 10, 0x6, 0x0, 0x6)
    test.append_i_type("ori", 11, 10, 0x334, 0x0, 0x334)
    test.append_i_type("ori", 11, 10, 0x667, 0x0, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd4, 0x0, -0x2c)
    test.append_i_type("ori", 11, 10, 0x2e, 0x0, 0x2e)
    test.append_i_type("ori", 11, 10, 0x7, 0x4, 0x3)
    test.append_i_type("ori", 11, 10, 0x555, 0x4, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaae, 0x4, -0x556)
    test.append_i_type("ori", 11, 10, 0x337, 0x4, 0x333)
    test.append_i_type("ori", 11, 10, 0x666, 0x4, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x4, -0x2d)
    test.append_i_type("ori", 11, 10, 0x2d, 0x4, 0x2d)
    test.append_i_type("ori", 11, 10, 0x6, 0x4, 0x2)
    test.append_i_type("ori", 11, 10, 0x554, 0x4, 0x554)
    test.append_i_type("ori", 11, 10, 0x4, 0x4, 0x0)
    test.append_i_type("ori", 11, 10, 0x4, 0x4, 0x4)
    test.append_i_type("ori", 11, 10, 0x336, 0x4, 0x332)
    test.append_i_type("ori", 11, 10, 0x665, 0x4, 0x665)
    test.append_i_type("ori", 11, 10, 0x2c, 0x4, 0x2c)
    test.append_i_type("ori", 11, 10, 0x556, 0x4, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaaf, 0x4, -0x555)
    test.append_i_type("ori", 11, 10, 0x6, 0x4, 0x6)
    test.append_i_type("ori", 11, 10, 0x334, 0x4, 0x334)
    test.append_i_type("ori", 11, 10, 0x667, 0x4, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd4, 0x4, -0x2c)
    test.append_i_type("ori", 11, 10, 0x2e, 0x4, 0x2e)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333332, 0x3)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333332, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffbba, 0x33333332, -0x556)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333332, 0x5)
    test.append_i_type("ori", 11, 10, 0x33333333, 0x33333332, 0x333)
    test.append_i_type("ori", 11, 10, 0x33333776, 0x33333332, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffff3, 0x33333332, -0x2d)
    test.append_i_type("ori", 11, 10, 0x3333333f, 0x33333332, 0x2d)
    test.append_i_type("ori", 11, 10, 0x33333332, 0x33333332, 0x2)
    test.append_i_type("ori", 11, 10, 0x33333776, 0x33333332, 0x554)
    test.append_i_type("ori", 11, 10, 0x33333332, 0x33333332, 0x0)
    test.append_i_type("ori", 11, 10, 0x33333336, 0x33333332, 0x4)
    test.append_i_type("ori", 11, 10, 0x33333332, 0x33333332, 0x332)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333332, 0x665)
    test.append_i_type("ori", 11, 10, 0x3333333e, 0x33333332, 0x2c)
    test.append_i_type("ori", 11, 10, 0x33333776, 0x33333332, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffbbb, 0x33333332, -0x555)
    test.append_i_type("ori", 11, 10, 0x33333336, 0x33333332, 0x6)
    test.append_i_type("ori", 11, 10, 0x33333336, 0x33333332, 0x334)
    test.append_i_type("ori", 11, 10, 0x33333777, 0x33333332, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffff6, 0x33333332, -0x2c)
    test.append_i_type("ori", 11, 10, 0x3333333e, 0x33333332, 0x2e)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666665, 0x3)
    test.append_i_type("ori", 11, 10, 0x66666775, 0x66666665, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffeef, 0x66666665, -0x556)
    test.append_i_type("ori", 11, 10, 0x66666665, 0x66666665, 0x5)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666665, 0x333)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666665, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffff7, 0x66666665, -0x2d)
    test.append_i_type("ori", 11, 10, 0x6666666d, 0x66666665, 0x2d)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666665, 0x2)
    test.append_i_type("ori", 11, 10, 0x66666775, 0x66666665, 0x554)
    test.append_i_type("ori", 11, 10, 0x66666665, 0x66666665, 0x0)
    test.append_i_type("ori", 11, 10, 0x66666665, 0x66666665, 0x4)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666665, 0x332)
    test.append_i_type("ori", 11, 10, 0x66666665, 0x66666665, 0x665)
    test.append_i_type("ori", 11, 10, 0x6666666d, 0x66666665, 0x2c)
    test.append_i_type("ori", 11, 10, 0x66666777, 0x66666665, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffeef, 0x66666665, -0x555)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666665, 0x6)
    test.append_i_type("ori", 11, 10, 0x66666775, 0x66666665, 0x334)
    test.append_i_type("ori", 11, 10, 0x66666667, 0x66666665, 0x667)
    test.append_i_type("ori", 11, 10, 0xfffffff5, 0x66666665, -0x2c)
    test.append_i_type("ori", 11, 10, 0x6666666f, 0x66666665, 0x2e)
    test.append_i_type("ori", 11, 10, 0xb503, 0xb503, 0x3)
    test.append_i_type("ori", 11, 10, 0xb557, 0xb503, 0x555)
    test.append_i_type("ori", 11, 10, 0xffffffab, 0xb503, -0x556)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb503, 0x5)
    test.append_i_type("ori", 11, 10, 0xb733, 0xb503, 0x333)
    test.append_i_type("ori", 11, 10, 0xb767, 0xb503, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd3, 0xb503, -0x2d)
    test.append_i_type("ori", 11, 10, 0xb52f, 0xb503, 0x2d)
    test.append_i_type("ori", 11, 10, 0xb503, 0xb503, 0x2)
    test.append_i_type("ori", 11, 10, 0xb557, 0xb503, 0x554)
    test.append_i_type("ori", 11, 10, 0xb503, 0xb503, 0x0)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb503, 0x4)
    test.append_i_type("ori", 11, 10, 0xb733, 0xb503, 0x332)
    test.append_i_type("ori", 11, 10, 0xb767, 0xb503, 0x665)
    test.append_i_type("ori", 11, 10, 0xb52f, 0xb503, 0x2c)
    test.append_i_type("ori", 11, 10, 0xb557, 0xb503, 0x556)
    test.append_i_type("ori", 11, 10, 0xffffffab, 0xb503, -0x555)
    test.append_i_type("ori", 11, 10, 0xb507, 0xb503, 0x6)
    test.append_i_type("ori", 11, 10, 0xb737, 0xb503, 0x334)
    test.append_i_type("ori", 11, 10, 0xb767, 0xb503, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0xb503, -0x2c)
    test.append_i_type("ori", 11, 10, 0xb52f, 0xb503, 0x2e)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555556, 0x3)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555556, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffffe, 0x55555556, -0x556)
    test.append_i_type("ori", 11, 10, 0x55555557, 0x55555556, 0x5)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555556, 0x333)
    test.append_i_type("ori", 11, 10, 0x55555776, 0x55555556, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x55555556, -0x2d)
    test.append_i_type("ori", 11, 10, 0x5555557f, 0x55555556, 0x2d)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555556, 0x2)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555556, 0x554)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555556, 0x0)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555556, 0x4)
    test.append_i_type("ori", 11, 10, 0x55555776, 0x55555556, 0x332)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555556, 0x665)
    test.append_i_type("ori", 11, 10, 0x5555557e, 0x55555556, 0x2c)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555556, 0x556)
    test.append_i_type("ori", 11, 10, 0xffffffff, 0x55555556, -0x555)
    test.append_i_type("ori", 11, 10, 0x55555556, 0x55555556, 0x6)
    test.append_i_type("ori", 11, 10, 0x55555776, 0x55555556, 0x334)
    test.append_i_type("ori", 11, 10, 0x55555777, 0x55555556, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd6, 0x55555556, -0x2c)
    test.append_i_type("ori", 11, 10, 0x5555557e, 0x55555556, 0x2e)
    test.append_i_type("ori", 11, 10, 0xaaaaaaab, -0x55555555, 0x3)
    test.append_i_type("ori", 11, 10, 0xaaaaafff, -0x55555555, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaab, -0x55555555, -0x556)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555555, 0x5)
    test.append_i_type("ori", 11, 10, 0xaaaaabbb, -0x55555555, 0x333)
    test.append_i_type("ori", 11, 10, 0xaaaaaeef, -0x55555555, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffffb, -0x55555555, -0x2d)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555555, 0x2d)
    test.append_i_type("ori", 11, 10, 0xaaaaaaab, -0x55555555, 0x2)
    test.append_i_type("ori", 11, 10, 0xaaaaafff, -0x55555555, 0x554)
    test.append_i_type("ori", 11, 10, 0xaaaaaaab, -0x55555555, 0x0)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555555, 0x4)
    test.append_i_type("ori", 11, 10, 0xaaaaabbb, -0x55555555, 0x332)
    test.append_i_type("ori", 11, 10, 0xaaaaaeef, -0x55555555, 0x665)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555555, 0x2c)
    test.append_i_type("ori", 11, 10, 0xaaaaafff, -0x55555555, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaab, -0x55555555, -0x555)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555555, 0x6)
    test.append_i_type("ori", 11, 10, 0xaaaaabbf, -0x55555555, 0x334)
    test.append_i_type("ori", 11, 10, 0xaaaaaeef, -0x55555555, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x55555555, -0x2c)
    test.append_i_type("ori", 11, 10, 0xaaaaaaaf, -0x55555555, 0x2e)
    test.append_i_type("ori", 11, 10, 0x7, 0x6, 0x3)
    test.append_i_type("ori", 11, 10, 0x557, 0x6, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffaae, 0x6, -0x556)
    test.append_i_type("ori", 11, 10, 0x7, 0x6, 0x5)
    test.append_i_type("ori", 11, 10, 0x337, 0x6, 0x333)
    test.append_i_type("ori", 11, 10, 0x666, 0x6, 0x666)
    test.append_i_type("ori", 11, 10, 0xffffffd7, 0x6, -0x2d)
    test.append_i_type("ori", 11, 10, 0x2f, 0x6, 0x2d)
    test.append_i_type("ori", 11, 10, 0x6, 0x6, 0x2)
    test.append_i_type("ori", 11, 10, 0x556, 0x6, 0x554)
    test.append_i_type("ori", 11, 10, 0x6, 0x6, 0x0)
    test.append_i_type("ori", 11, 10, 0x6, 0x6, 0x4)
    test.append_i_type("ori", 11, 10, 0x336, 0x6, 0x332)
    test.append_i_type("ori", 11, 10, 0x667, 0x6, 0x665)
    test.append_i_type("ori", 11, 10, 0x2e, 0x6, 0x2c)
    test.append_i_type("ori", 11, 10, 0x556, 0x6, 0x556)
    test.append_i_type("ori", 11, 10, 0xfffffaaf, 0x6, -0x555)
    test.append_i_type("ori", 11, 10, 0x6, 0x6, 0x6)
    test.append_i_type("ori", 11, 10, 0x336, 0x6, 0x334)
    test.append_i_type("ori", 11, 10, 0x667, 0x6, 0x667)
    test.append_i_type("ori", 11, 10, 0xffffffd6, 0x6, -0x2c)
    test.append_i_type("ori", 11, 10, 0x2e, 0x6, 0x2e)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333334, 0x3)
    test.append_i_type("ori", 11, 10, 0x33333775, 0x33333334, 0x555)
    test.append_i_type("ori", 11, 10, 0xfffffbbe, 0x33333334, -0x556)
    test.append_i_type("ori", 11, 10, 0x33333335, 0x33333334, 0x5)
    test.append_i_type("ori", 11, 10, 0x33333337, 0x33333334, 0x333)
    test.append_i_type("ori", 11, 10, 0x33333776, 0x33333334, 0x666)
    test.append_i_type("ori", 11, 10, 0xfffffff7, 0x33333334, -0x2d)
    test.append_i_type("ori", 11, 10, 0x3333333d, 0x33333334, 0x2d)
    test.append_i_type("ori", 11, 10, 0x33333336, 0x33333334, 0x2)
    test.append_i_type("ori", 11, 10, 0x33333774, 0x33333334, 0x554)
    test.append_i_type("ori", 11, 10, 0x33333334, 0x33333334, 0x0)
    test.append_i_type("ori", 11, 10, 0x33333334, 0x33333334, 0x4)
    test.append_i_type("ori", 11, 10, 0xbfffffff, -0x40000001, 0x400)
    test.append_i_type("ori", 11, 10, 0xffffffff, -0x4001, -0x11)
    test.append_ecall()
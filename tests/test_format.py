import unittest

import copy

from tablo import joinrow, Format, Align


class TestFormat(unittest.TestCase):

    def test_joinrow(self):
        expected = '| 4   | Нет | 112.003    |'
        row = [
            ('4',       Format(Align.Left, margin=3)),
            ('Нет',     Format(Align.Left, margin=3)),
            ('112.003', Format(Align.Left, margin=10)),
        ]

        actual = joinrow(row)

        self.assertEqual(expected, actual)

    def test_eq(self):
        a = Format(Align.Left, margin=3)
        b = Format(Align.Left, margin=3)

        self.assertEqual(a, b)

    def test_format_copy(self):
        a = Format(Align.Left, margin=3)

        b = a.copy()
        c = copy.copy(a)

        self.assertNotEqual(id(a), id(b))
        self.assertNotEqual(id(a), id(c))
        self.assertEqual(a, b)
        self.assertEqual(a, c)

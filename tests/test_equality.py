import unittest

from tablo import Tablo


class TestEquality(unittest.TestCase):

    def test__eq_raises_error__with_not_Tablo_instance(self):
        actual = Tablo('X Y'.split())
        actual.append_row([1, 2])
        with self.assertRaises(TypeError):
            actual == 'STRING'

    def test__eq_True__with_eq_headers_and_eq_rows(self):
        expected = Tablo('X Y'.split())
        expected.append_row([1, 2])

        actual = Tablo('X Y'.split())
        actual.append_row([1, 2])

        self.assertEqual(expected, actual)

    def test__eq_True__with_neq_headers_and_eq_rows(self):
        expected = Tablo('A B'.split())
        expected.append_row([1, 2])

        actual = Tablo('X Y'.split())
        actual.append_row([1, 2])

        self.assertNotEqual(expected, actual)

    def test__eq_True__with_eq_headers_and_neq_rows(self):
        expected = Tablo('A B'.split())
        expected.append_row([1, 2])

        actual = Tablo('X Y'.split())
        actual.append_row([5, 5])

        self.assertNotEqual(expected, actual)

    def test_parse_with_whitespaces(self):
        """ Парсим несколько строк с разделителями в виде новой строки """

        s = (
            '\n\n\n\n  \t\t\t'
            '| X | Y   | Z                                 |\n\t\t\t'
            '| 1 | 2.5 | две пустые строки                 |\n\n'
            '| 2 | 0.9 | две пустые строки окруж пробелами |    \n\n   '
            '| 3 | 4.3 | две пустые строки пробел между    |  \n   \n '
            '| 4 | 1.2 | вообще без пробелов               || 5 | 4.1 | эту строку надо перенести |'
            '\n\n\n\n'
        )
        t2 = Tablo.from_str(s)
        t2.print()

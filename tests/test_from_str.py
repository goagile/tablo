import unittest

from tablo import Tablo


class TestFromStr(unittest.TestCase):

    def test_parse_with_whitespaces(self):
        """ Парсим несколько строк с разделителями в виде новой строки """

        expected = Tablo('X Y Z'.split())
        expected.append_row('1|2.5|две пустые строки'.split('|'))
        expected.append_row('2|0.9|две пустые строки окруж пробелами'.split('|'))
        expected.append_row('3|4.3|две пустые строки пробел между'.split('|'))
        expected.append_row('4|1.2|вообще без пробелов'.split('|'))
        expected.append_row('5|4.1|эту строку надо перенести'.split('|'))
        # expected.print()

        s = (
            '\n\n\n\n  \t\t\t'
            '| X | Y   | Z                                 |\n\t\t\t'
            '| 1 | 2.5 | две пустые строки                 |\n\n'
            '| 2 | 0.9 | две пустые строки окруж пробелами |    \n\n   '
            '| 3 | 4.3 | две пустые строки пробел между    |  \n   \n '
            '| 4 | 1.2 | вообще без пробелов               || 5 | 4.1 | эту строку надо перенести |'
            '\n\n\n\n'
        )
        actual = Tablo.from_str(s)
        # actual.print()

        self.assertEqual(expected, actual)

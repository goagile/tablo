import unittest

from tablo import BaseTablo


class TestBaseFunctions(unittest.TestCase):

    def test_raise_exception_with_non_promitive_data(self):
        tablo = BaseTablo('X Y Z A B'.split())
        row = ('@', 4, 2.1, False, ['invalid', 'data'])

        with self.assertRaises(ValueError) as x:
            tablo.append_row(row)

    def test_loose_data_in_rows(self):
        expected = ('45', 18.2, None, None, None)
        tablo = BaseTablo('X Y Z A B'.split())
        tablo.append_row(['45', 18.2])
        row = tablo[0]

        actual = row.X, row.Y, row.Z, row.A, row.B

        self.assertEqual(expected, actual)

    def test__get_row_value_by_column_name(self):
        tablo = BaseTablo('X Y Z A B'.split())
        expected = '@', 4, 2.1, False, 'Нет'
        tablo.append_row(expected)
        row = tablo[0]

        actual = (row.X, row.Y, row.Z, row.A, row.B)

        self.assertEqual(expected, actual)

    def test_raise_error_with_invalid_column_name(self):
        tablo = BaseTablo('X Y Z A B'.split())
        expected = '@', 4, 2.1, False, 'Нет'
        tablo.append_row(expected)
        row = tablo[0]

        with self.assertRaises(AttributeError):
            row.G

    def test__get_row_value_by_column_index(self):
        tablo = BaseTablo('X Y Z A B'.split())
        expected = '@', 4, 2.1, False, 'Нет'
        tablo.append_row(expected)
        row = tablo[0]

        actual = row[0], row[1], row[2], row[3], row[4]

        self.assertEqual(expected, actual)

    def test__get_column_value_by_row_index(self):
        expected = ('@', '&')
        tablo = BaseTablo('X Y Z A B'.split())
        tablo.append_row(['@', 4, 2.1, False, 'Нет'])
        tablo.append_row(['&', 22, 5.03, True, 'Да'])
        column_X = tablo.X

        actual = column_X[0], column_X[1]

        self.assertEqual(expected, actual)

    def test__raise_with_index_out_of_range(self):
        tablo = BaseTablo('X Y Z A B'.split())
        tablo.append_row(['@', 4, 2.1, False, 'Нет'])
        tablo.append_row(['&', 22, 5.03, True, 'Да'])
        column_X = tablo.X

        with self.assertRaises(IndexError):
            actual = column_X[10]

    def test__iter_rows_and_get_row_data(self):
        expected = [
            ['@', 4, 2.1, False, 'Нет'],
            ['&', 22, 5.03, True, 'Да']
        ]
        tablo = BaseTablo('X Y Z A B'.split())
        tablo.append_row(expected[0])
        tablo.append_row(expected[1])

        actual = [row.data for row in tablo]

        self.assertEqual(expected, actual)

    def test__iter_rows_and_columns(self):
        expected = [
            ['@', 4, 2.1, False, 'Нет'],
            ['&', 22, 5.03, True, 'Да']
        ]
        tablo = BaseTablo('X Y Z A B'.split())
        tablo.append_row(expected[0])
        tablo.append_row(expected[1])

        actual = []
        for row in tablo:
            actual.append([col for col in row])

        self.assertEqual(expected, actual)

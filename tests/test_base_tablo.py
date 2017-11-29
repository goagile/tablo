import unittest

from tablo import BaseTablo


class TestEquality(unittest.TestCase):

    def test__get_column_value_by_name(self):
        tablo = BaseTablo('X Y Z A B'.split())
        expected = '@', 4, 2.1, False, 'Нет'
        tablo.append_row(expected)
        row = tablo[0]

        actual = (row.X, row.Y, row.Z, row.A, row.B)

        self.assertEqual(expected, actual)

    def test__get_column_value_by_index(self):
        tablo = BaseTablo('X Y Z A B'.split())
        expected = '@', 4, 2.1, False, 'Нет'
        tablo.append_row(expected)
        row = tablo[0]

        actual = row[0], row[1], row[2], row[3], row[4]

        self.assertEqual(expected, actual)

        """

        Добавление строки в таблицу

            >>> row = '&', 22, 5.03, True, 'Да'
            >>> tablo.append_row(row)

        Доступ к столбцу по индексу строки

            >>> column_X = tablo.X
            >>> column_X[0], column_X[1]
            ('@', '&')

        Перебор строк и доступ к данным строки

            >>> for row in tablo:
            ...     row.data
            ['@', 4, 2.1, False, 'Нет']
            ['&', 22, 5.03, True, 'Да']

        Перебор строк и столбцов

            >>> for row in tablo:
            ...     [col for col in row]
            ['@', 4, 2.1, False, 'Нет']
            ['&', 22, 5.03, True, 'Да']


        Ошибки
        ======

        Добавление сложного типа в ячейку

            >>> row = ('@', 4, 2.1, False, ['invalid', 'data'])
            >>> tablo.append_row(row)
            Traceback (most recent call last):
                ...
            ValueError: '['invalid', 'data']' Invalid Primitive type

        Неполная строка

            >>> row = ('45', 18.2)
            >>> tablo.append_row(row)
            >>> row = tablo[2]
            >>> row.X, row.Y, row.Z, row.A, row.B
            ('45', 18.2, None, None, None)

        Доступ к несуществующей строке

            >>> column_X[10]
            Traceback (most recent call last):
              ...
            IndexError: list index out of range

        Доступ к несуществующему атрибуту по имени столбца

            >>> row = tablo[0]
            >>> row.G
            Traceback (most recent call last):
              ...
            AttributeError: 'G' Invalid column name

        """

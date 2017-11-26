"""

Подключаем таблицу

    >>> from tablo import SplitTablo

Фикс: Ошибка выравнивания
-------------------------
Возникает, когда длина header > длина cell:

    | Name | Value   |
    | x | 1.87887 |
    | y | 20.0    |

    >>> tablo = SplitTablo(headers='Name Value'.split())
    >>> tablo.append_row(['x', 1.87887])
    >>> tablo.append_row(['y', 20.0])
    >>> tablo.print()
    | Name | Value   |
    | x    | 1.87887 |
    | y    | 20.0    |

"""

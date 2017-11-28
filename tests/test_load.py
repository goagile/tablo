"""

    >>> from tablo import Tablo

    >>> t = Tablo('X Y Z'.split())
    >>> t.append_row([1, 2.5, 'нет'])
    >>> t.append_row([2, 4.3, 'да'])
    >>> t.print()
    | X | Y   | Z   |
    | 1 | 2.5 | нет |
    | 2 | 4.3 | да  |
    >>> print(t)
    | X | Y   | Z   |
    | 1 | 2.5 | нет |
    | 2 | 4.3 | да  |
    <BLANKLINE>

    # >>> s = (
    # ... '| X | Y   | Z   |'
    # ... '| 1 | 2.5 | нет |'
    # ... '| 2 | 4.3 | да  |'
    # ... )
    # >>> s
    #
    # >>> t2 = Tablo.from_str(s)
    # >>> t2.print()
    # | X | Y   | Z   |
    # | 1 | 2.5 | нет |
    # | 2 | 4.3 | да  |

    # TODO: print(t2)

Парсим заголовок

    >>> s = (
    ... '| X | Y   | Z   |'
    ... )
    >>> t2 = Tablo.from_str(s)
    >>> t2.headers
    ['X', 'Y', 'Z']

Парсим одну строку

    >>> s = (
    ... '| X | Y   | Z   |\\n'
    ... '| 1 | 2.5 | нет |\\n'
    ... )
    >>> t2 = Tablo.from_str(s)
    >>> [v for v in t2[0]]
    ['1', '2.5', 'нет']

"""

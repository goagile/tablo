"""

    >>> from tablo.split_tablo_format import joinrow, Align, Format

Печать отформатированной последовательности

    >>> sequence = ['X', 'Y', 'Z', 'A', 'B']
    >>> row = [
    ...     ('4',   Format(Align.Left, margin=3)),
    ...     ('Нет', Format(Align.Left, margin=3)),
    ...     ('112.003', Format(Align.Left, margin=10)),
    ... ]

    >>> joinrow(row)
    '| 4   | Нет | 112.003    |'

Копирование формата

    >>> a = Format(Align.Left, margin=3)
    >>> b = a.copy()
    >>> id(a) != id(b)
    True
    >>> b
    Format(align=Left, margin=3, spacer=' ')

"""

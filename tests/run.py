from tablo import SplitTablo


I = 562.2
R = 67.232
U = 'INVALID DATA'

tablo = SplitTablo(headers='I R U'.split())
tablo.append_row([I, R])
tablo.print()

print()

tablo = SplitTablo(headers='Ifsdfsdf R U'.split())
tablo.append_row([I, R])
tablo.print()
# print(tablo.R[0])

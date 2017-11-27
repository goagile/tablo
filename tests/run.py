from tablo import Tablo


I = 562.2
R = 67.232
U = 'INVALID DATA'

tablo = Tablo(headers='I R U'.split())
tablo.append_row([I, R])
tablo.print()

print()

tablo = Tablo(headers='Ifsdfsdf R U'.split())
tablo.append_row([I, R])
tablo.print()
# print(tablo.R[0])

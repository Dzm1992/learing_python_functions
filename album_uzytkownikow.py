#8.8

def make_album(nazwa_zespolu, tytul_albumu, liczba_utworow=''):
	"""Tworzy słownik reprezentujący album muzyczny."""
	slownik = {'Zespół': nazwa_zespolu, 'Album': tytul_albumu}
	if liczba_utworow:
		slownik['Utwory'] = liczba_utworow
	return slownik
	
while True:
	print("Aby przerwać wpisz q w dowolnym momencie.")
	n_zespolu = input("Podaj artystę/zespół: ")
	if n_zespolu == 'q':
		break
	t_albumu = input("Podaj tytul albumu: ")
	if t_albumu == 'q':
		break
	album = make_album(n_zespolu, t_albumu)
	print(album)

	

	

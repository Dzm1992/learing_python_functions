#8.7
def make_album(nazwa_zespolu, tytul_albumu, liczba_utworow=''):
	"""Tworzy słownik reprezentujący album muzyczny."""
	if liczba_utworow:
		slownik = {'Zespół': nazwa_zespolu, 'Album': tytul_albumu, 'Utwory': liczba_utworow}
	else:
		slownik = {'Zespół': nazwa_zespolu, 'Album': tytul_albumu}
	return slownik
	
	

print(make_album('Mes', 'Zamach na Przeciętność', '2'))
print(make_album('Eldo', 'Eternia'))
print(make_album('Pezet', 'Muzyka Rozrywkowa'))

	

	

def make_album(nazwa_zespolu, tytul_albumu, liczba_utworow=''):
	"""Tworzy słownik reprezentujący album muzyczny."""
	slownik = {'Zespół': nazwa_zespolu, 'Album': tytul_albumu}
	if liczba_utworow:
		slownik['Utwory'] = liczba_utworow
	return slownik
	
	

print(make_album('Mes', 'Zamach na Przeciętność', '2'))
print(make_album('Eldo', 'Eternia'))
print(make_album('Pezet', 'Muzyka Rozrywkowa'))
print(make_album('Pezet', 'Muzyka Rozrywkowa', '2'))

	

	

	

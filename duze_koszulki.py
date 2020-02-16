#8.4

def make_shirt(size='XXL', text='Kocham Pythona'):
	"""Zwraca wielkosc i nadruk na koszulce."""
	print("Koszulka ma rozmiar: " + size + ", nadrukowany tekst to: " + text + ".")

make_shirt()
make_shirt('XL')
make_shirt(size='L')
make_shirt('M', 'Kocham Jave')

#8.11

magicy = ['Hudini', 'Magik', 'Ryze']
wielcy_magicy = []


def make_great(magicy, wielcy_magicy):
	"""Dodaje 'doskonały' na poczatku imienia w nowej liscie."""
	while magicy:
		wizards = magicy.pop()
		wielcy_magicy.append("Wielki " + wizards)
				
def show_magicians(wielcy_magicy):
	"""Wyświetla każdego magika z listy."""
	for wielki_magik in wielcy_magicy:
		print(wielki_magik)
	

make_great(magicy[:], wielcy_magicy)
show_magicians(magicy)
show_magicians(wielcy_magicy)

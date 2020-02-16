#8.5

def describe_city(miasto, kraj='Polska'):
	"""Wyświetla miasto i kraj."""
	print(miasto.title() + " leży w " + kraj.title() + ".")
	
describe_city('warszawa', 'polska')
describe_city('kraków')
describe_city('bydgoszcz')
describe_city('paryż', 'francja')
describe_city(kraj='Niemcy', miasto='Berlin')

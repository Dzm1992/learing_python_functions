#8.12

def lista_skladnikow(*skladniki):
	"""Pokazuje liste skladnikow kanapki."""
	print("Kanapka sklada sie z następujacych skladnikow: ")
	for skladnik in skladniki:
		print("- " + skladnik)
		

lista_skladnikow('Szynka', 'Ser', 'Pomidor', 'Cebula')

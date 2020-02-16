#8.14

def game_info(tytuł, gatunek, **cechy):
	"""Pokazuje informacje o grze."""
	gra = {}
	gra['Tytuł'] = tytuł
	gra['Gatunek'] = gatunek
	
	for k, v in cechy.items():
		gra[k] = v
	
	return gra
	
gra = game_info('LoL', 'MOBA', Wydawca='Riot Games')
print(gra)

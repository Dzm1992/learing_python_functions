#8.6

def city_country(country, city):
	"""Wyswietla kraj i miasto."""
	a = country
	b = city
	c = a + ", " + b
	return c.title()
	
	
d = city_country('polska', 'warszawa')
print(d)	


from US import US
from UK import UK
from AU import AU
from CA import CA
def info():

	print("Account Generator Ready")
	location = raw_input('Enter Location US UK CA AU \t')
	if location == 'US':
		x = raw_input('My guy how many accounts are we making?')
		x = int(x)
		domain = raw_input('My guy which domain do you need?')
		US(x, domain)
	if location == 'UK':
		x = raw_input('My guy how many accounts are we making?')
		x = int(x)
		domain = raw_input('My guy which domain do you need?')
		UK(x, domain)
	if location == 'AU':
		x = raw_input('My guy how many accounts are we making?')
		x = int(x)
		domain = raw_input('My guy which domain do you need?')
		AU(x, domain)
	if location == 'CA':
		x = raw_input('My guy how many accounts are we making?')
		x = int(x)
		domain = raw_input('My guy which domain do you need?')
		CA(x, domain)
	

from US import USGEN 
from UK import UK
from AU import AU
from CA import CA

USGEN = USGEN()




class Info:
	def start(self):
		print("Account Generator Ready")
		location = raw_input('Enter Location US UK CA AU \t')
		if location == 'US':
			x = int(raw_input('Number of accounts to be made:\t'))
			domain = raw_input('Enter in your domain:')
			USGEN.US(x, domain)
		if location == 'UK':
			x = int(raw_input('Number of accounts to be made:\t'))
			domain = raw_input('Enter in your domain:\t')
			UK(x, domain)
		if location == 'AU':
			x = int(raw_input('Number of accounts to be made:\t'))
			domain = raw_input('Enter in your domain:\t')
			AU(x, domain)
		if location == 'CA':
			x = int(raw_input('Number of accounts to be made:\t'))
			domain = raw_input('Enter in your domain:\t')
			CA(x, domain)
			

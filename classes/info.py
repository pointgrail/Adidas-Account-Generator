from US import US
from UK import UK
from AU import AU
from CA import CA

class INFO:
	def info(self):
		print("Account Generator Ready")
		location = raw_input('Enter Location US UK CA AU \t')
		if location == 'US':
			x = raw_input('Number of accounts to be made:')
			x = int(x)
			domain = raw_input('Enter in your domain:')
			US(x, domain)
		if location == 'UK':
			x = raw_input('Number of accounts to be made:')
			x = int(x)
			domain = raw_input('Enter in your domain:')
			UK(x, domain)
		if location == 'AU':
			x = raw_input('Number of accounts to be made:')
			x = int(x)
			domain = raw_input('Enter in your domain:')
			AU(x, domain)
		if location == 'CA':
			x = raw_input('Number of accounts to be made:')
			x = int(x)
			domain = raw_input('Enter in your domain:')
			CA(x, domain)
			

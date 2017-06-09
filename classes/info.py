from US import USGEN 
from UK import UKGEN
from AU import AUGEN 
from CA import CA

USGEN = USGEN()
UKGEN = UKGEN()
AUGEN = AUGEN()


class Info:
	def start(self):
		#washed code 
		print("Account Generator Ready")
		
		location = raw_input('Enter Location US UK CA AU \t')
		x = int(raw_input('Number of accounts to be made:\t'))
		domain = raw_input('Enter in your domain:')
		
		if location == 'US':	
			USGEN.US(x, domain)
		
		if location == 'UK':
			UKGEN.UK(x, domain)
		
		if location == 'AU':
			AU(x, domain)
		
		if location == 'CA':
			CA(x, domain)
			

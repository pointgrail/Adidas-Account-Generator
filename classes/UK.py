import requests, time, random, string, os
from faker import Faker
from bs4 import BeautifulSoup
fake = Faker()

#Import Custom Account Check
from accountCheck import acctCheck
acctCheck = acctCheck()


class UKGEN:
	
  def UK(self, x, domain):
      for i in range(x):
      	fake 	 = Faker()
		first 	 = fake.first_name() 
		last 	 = fake.last_name()
		number 	 = random.randint(0, 999)
		Day 	 = '%d'   % (random.randint(1, 28))
		Month 	 = '%d'   % (random.randint(1, 12))
		Year 	 = '19%d' % (random.randint(80, 95))
		email 	 = '%s%s%s@%s' % (first, number, last, domain)
		password = '%s%s%s'    % (first, number, last)

		headers  = {

		    'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
		    'Accept-Encoding'		: 'gzip, deflate, sdch, br',
		    'Accept-Language'		: 'en-GB,en;q=0.8',
		    'Upgrade-Insecure-Requests' : '1'
		}

		s = requests.Session()
		s.headers.update(headers)

		r 	  = s.get('https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount')
		csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

		s.headers.update({
		    'Origin': 'https://cp.adidas.co.uk',
		    'Referer': 'https://cp.adidas.co.uk/web/eCom/en_GB/loadcreateaccount',
		})

		payload = {
			
		       'firstName'			: first, 
		       'lastName'			: last,
		       'minAgeCheck'			: 'true',
		       'day'				: Day,
		       'month'				: Month,
		       'year'				: Year,
		       '_minAgeCheck'			: 'on',
		       'email'				: email,
		       'password'			: password,
		       'confirmPassword'		: password,
		       '_amf'				: 'on',
		       'terms'				: 'true',
		       '_terms'				: 'on',
		       'metaAttrs[pageLoadedEarlier]'	: 'true',
		       'app'				: 'eCom',
		       'locale'				: 'en_GB',
		       'domain'				: '',
		       'consentData1'			: 'Sign me up for adidas emails, featuring exclGBive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.co.uk/GB/help-topics-privacy_policy.html">Policy Policy</a> for details.',
		       'consentData2'			: '',
		       'consentData3'			: '',
		       'CSRFToken'			: csrftoken

			       }

		r = s.post('https://cp.adidas.co.uk/web/eCom/en_GB/accountcreate', data=payload)

		if not acctCheck.AccountCheck(r):
		    print "Account Exists : Username = {0}, Password = {1}".format(email, password)

		if acctCheck.AccountCheck(r):
		    print 'Created Account : Username = {0}, Password = {1}'.format(email, password)
		    with open('accountsUK' + '.txt', 'a') as f:
			f.write(email + ':' + password + '\n')
			f.close()

		time.sleep(2)
import requests, time, random, string, os
from faker import Faker
from bs4 import BeautifulSoup
fake = Faker()

def account_successfully_createdUS(response):
    try:
        return False if BeautifulSoup(response.text, "html.parser").find('input',
                                                                        {'id': 'resumeURL'}).get('value') == \
                        'https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/MyAccount-CreateOrLogin' \
            else True
    except:
        return True
def US(x, domain):

	
    for i in range(x):
        first = fake.first_name()
        last = fake.last_name()
        number = random.randint(0, 999)
        email = '{}{}{}@{}'.format(first, number, last, domain)
        password = '{}{}{}'.format(first, number, last)

        headers = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'en-US,en;q=0.8',
           'Upgrade-Insecure-Requests': '1'
        }


        s = requests.Session()
        s.headers.update(headers)

        r = s.get('https://cp.adidas.com/web/eCom/en_US/loadcreateaccount')
        csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'CSRFToken'}).get('value')

        s.headers.update({
                'Origin': 'https://cp.adidas.com',
                'Referer': 'https://cp.adidas.com/web/eCom/en_US/loadcreateaccount',
        })
        r = s.post('https://cp.adidas.com/web/eCom/en_US/accountcreate',
                       data={
                           'firstName': first,
                           'lastName': last,
                           'minAgeCheck': 'true',
                           '_minAgeCheck': 'on',
                           'email': email,
                           'password': password,
                           'confirmPassword': password,
                           '_amf': 'on',
                           'terms': 'true',
                           '_terms': 'on',
                           'metaAttrs[pageLoadedEarlier]': 'true',
                           'app': 'eCom',
                           'locale': 'en_US',
                           'domain': '',
                           'consentData1': 'Sign me up for adidas emails, featuring exclusive offers, featuring latest product info, news about upcoming events, and more. See our <a target="_blank" href="https://www.adidas.com/us/help-topics-privacy_policy.html">Policy Policy</a> for details.',
                           'consentData2': '',
                           'consentData3': '',
                           'CSRFToken': csrftoken
                       })
        if account_successfully_createdUS(r) == False:
            print "Account EXISTS : Username = {0}, Password = {1}".format(email, password)

        if account_successfully_createdUS(r) == True:

            print "Created Account : Username = {0}, Password = {1}".format(email, password)
            with open('accountsUS' + '.txt', 'a') as f:
                f.write(email + ':' + password + '\n')
                f.close()

        time.sleep(2)
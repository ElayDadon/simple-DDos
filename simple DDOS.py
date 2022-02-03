import requests 
import os 
import random
import string
import json 
chars = string.ascii_letters+string.digits+'!@#$%^&*()'
random.seed = (os.urandom(1024))
#site url
url = ''
name_list = json.loads(open('#filenamesname').read())
for name in name_list: 
	name_foremail = ''.join(random.choice(string.digits))
	#changable end of email
	username = name.lower()+name_email+'@gmail.com'
	password = ''.loin(random.choice(chars) for i in range(8))
	#inside data write the format of the site submit
	requests.post(url,allow_redirects=False,data={})
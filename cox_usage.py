import mechanize  
import re
from bs4 import BeautifulSoup
import json

#URL that we authenticate against
login_url = "https://www.cox.com/resaccount/sign-in.cox"
#URL that we grab all the data from
stats_url = "https://www.cox.com/internet/mydatausage.cox"
#Your cox user account (e.g. username@cox.net) and password
cox_user = "username"
cox_pass = "password"
 
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
#Open the login URL
sign_in = br.open(login_url)
#Find the form named sign-in
br.select_form(name = "sign-in")
#Set the username 
br["username"] = cox_user
#Set the password 
br["password"] = cox_pass
#Submit the form
logged_in = br.submit()    
#Read the stats URL
url_read = br.open(stats_url).read()
soup = BeautifulSoup(url_read,"lxml") 
#Grab the second script from the page with all the stats in it
js = soup.findAll("script")[1].string
#Split and RSplit on the first { and on the last } which is where the data object is located
jsonValue = '{%s}' % (js.split('{', 1)[1].rsplit('}', 1)[0],)
#Load into json
value = json.loads(jsonValue)
#Print pretty json
print json.dumps(value, indent=4, sort_keys=True)

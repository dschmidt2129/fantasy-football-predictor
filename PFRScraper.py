import requests
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import datetime

# TODO: REFACTOR TO A MORE OOO STRUCTURE

# TODO: ADD A MORE REFINED WAY TO GET YEARLY STATISTICS
# https://www.delftstack.com/howto/python/python-current-year/
# currentDateTime = datetime.datetime.now()

# date = currentDateTime.date()

# current_year = date.strftime('%Y')

year = input('What year statistics do you want to see: ')

# PRO FOOTBALL REFERENCE URL FOR PASSING, RUSHING, RECEIVING, KICKING
passing_url = 'https://www.pro-football-reference.com/years/' + year + '/passing.htm'
rushing_url = 'https://www.pro-football-reference.com/years/' + year + '/rushing.htm'
receiving_url = 'https://www.pro-football-reference.com/years/' + year + '/receiving.htm'
kicking_url = 'https://www.pro-football-reference.com/years/' + year + '/kicking.htm'

request = requests.get(passing_url)

if(request.status_code == 200):
    soup = bs(request.content, 'html.parser')

# TODO: ADD SWITCH STATEMENT TO SWITCH BETWEEN THE DIFFERENT TABLE DIVS
# HTML ELEMENT is id=div_kicking/passing/rushing/receiving
    stat_table = soup.find('div',{'id' : 'div_passing'})
    print(stat_table)
else:
    raise URLError('Could not find Pro Football Reference Stats for this year')    
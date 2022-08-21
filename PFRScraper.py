import requests
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
class PFRScraper:  
    # no arg constructor
    def __init__(self):
        pass

    def scrape(self, year, url_type):
        url = ''
        # PRO FOOTBALL REFERENCE URL FOR PASSING, RUSHING, RECEIVING, KICKING
        pfr_url = 'https://www.pro-football-reference.com/years/'
        passing_url =  pfr_url + year + '/passing.htm'
        rushing_url = pfr_url + year + '/rushing.htm'
        receiving_url = pfr_url + year + '/receiving.htm'
        kicking_url = pfr_url + year + '/kicking.htm'

# switch statement to get the correct url based on the user input
        match url_type:
            case 'passing':
                url = passing_url
            case 'rushing':
                url = rushing_url    
            case 'receiving':
                url = receiving_url
            case 'kicking':
                url = kicking_url
            case _: #defauld case
                url = passing_url

        request = requests.get(url)

        if(request.status_code == 200):
            soup = bs(request.content, 'html.parser')
            # HTML ELEMENT is id=div_kicking/passing/rushing/receiving
            div_type = 'div_'
            match url_type:
                case 'passing':
                    div_type += 'passing'
                case 'rushing':
                    div_type += 'rushing'    
                case 'receiving':
                    div_type += 'receiving'
                case 'kicking':
                    div_type += 'kicking'
                case _: #default case
                    div_type += 'passing'
            stat_table = soup.find('div',{'id' : div_type})
            print(stat_table)
        else:
            raise URLError('Could not find Pro Football Reference Stats for this year')    
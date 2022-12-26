from turtle import position
import requests
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import pandas as pd
import numpy as np

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

            pos = ''
            match url_type:
                case 'passing':
                    pos = 'QB'
                case 'rushing':   
                    pos = 'RB'
                case 'receiving':
                    pos = 'WR'
                case 'kicking':
                    pos = 'K'
                case _: #default case
                    pos = 'QB'
            print(self.format_pos_data(soup, pos))
        else:
            raise URLError('Could not find Pro Football Reference Stats for this year')

    # formats and filters the scraped data into a readable format 
    def format_pos_data(self, soup, pos):
        # collect table headers
        field_headers = []
        column_headers = []
        if pos == 'K':
            # TODO: FIGURE OUT HOW TO ADD THE FIELD GOAL YARDAGE COLUMNS
            field_goal_headers = soup.find_all('tr')[0]
            field_headers = [j.get_text() for j in field_goal_headers.find_all('th')]
            column_headers = soup.find_all('tr')[1]
            column_headers = [i.get_text() for i in column_headers.find_all('th')]
        else:
            column_headers = soup.find_all('tr')[0]
            column_headers = [i.get_text() for i in column_headers.find_all('th')]
        
        # collect table rows
        rows = soup.find_all('tr')[2:] # actual statistics rows after the headers, first row is empty in this scraping method (at least for kickers it was)

        # get stats from each row
        stats = []
        for i in range(len(rows)):
            stats.append([col.get_text() for col in rows[i].find_all('td')])

        # Create DataFrame from the scraped data
        data = pd.DataFrame(stats) # columns = column titles for the data frames, omitting rk
        # clean data to be specific to position
        if pos != 'K':
            data.columns =column_headers[1:]
            return data[data.Pos == pos]
        else:
            
            y =[("", column_headers[1]),("", column_headers[2]), 
                ("", column_headers[3]),("", column_headers[4]), 
                ("", column_headers[5]),("", column_headers[6]), 
                (field_headers[2], column_headers[7]), (field_headers[2], column_headers[8]),
                (field_headers[3], column_headers[9]), (field_headers[3], column_headers[10]),
                (field_headers[4], column_headers[11]),(field_headers[4], column_headers[12]),
                (field_headers[5], column_headers[13]), (field_headers[5], column_headers[14])]
                # TODO NEED TO ADD 50+ FIELD GOAL HEADER AND EXTRA POINT HEADER TO THE TABLE MULTI INDEX HEADERS

            #TODO NEED TO FIGURE OUT WHY COLUMN HEADERS AND FIELD HEADERS DO NOT MATCH UP 
            for i in range(len(column_headers) - len(field_headers)-5): # SUPER KLUGEY SOLUTION
                y.append('')

            col_list = pd.MultiIndex.from_tuples(y)
            data.columns = col_list
            data.to_csv('kickers_2020.csv')
            # todo write data to db using SQLite?
            return data
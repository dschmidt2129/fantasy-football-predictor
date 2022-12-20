# fantasy-football-predictor
python application that when finished will utilize web scraping and machine learning to predict and suggest players to add to a given roster based on a player's performance and a roster's needs

Official ESPN fantasy football api:
    http://espn-fantasy-football-api.s3-website.us-east-2.amazonaws.com/

Useful documentation and urls:
    https://phoenixnap.com/kb/mysql-docker-container
    https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c#v2sportsfootballleaguesnflathletesathlete_idstatistics0
    https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
    https://stmorse.github.io/journal/pfr-scrape-python.html
    https://towardsdatascience.com/scraping-nfl-stats-to-compare-quarterback-efficiencies-4989642e02fe
    

Steps to run:
    1. Install python 3.10 from https://www.python.org/
        a. make sure to add the python directory to the user variables path
        b. add the scripts directory to the system variables path
    2. Install the python extension on vscode
    3. In the terminal, run:
        a. pip install requests
        b. pip install bs4
        c. pip install pandas
        d. pip install numpy

steps to run the frontend:
    download the lts version of nodejs
    run npm install react
        npm intall react-bootstrap
        npm install react-dom
    npm start
    
To run the application:
    run main.py in order to start the application or type 'python main.py' in the terminal

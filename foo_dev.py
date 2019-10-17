import os
import requests
from bs4 import BeautifulSoup

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def top_scorers(opt):
    width=20
    if int(opt)==1:
        page = requests.get("https://www.premierleague.com/stats")
        soup = BeautifulSoup(page.content, 'html.parser')
        
        statsHero = soup.find(class_="statsHero")
        name = statsHero.find(class_="statName").get_text()
        goals = statsHero.find(class_="stat").get_text()
        goal = get_num(goals)
        print("Top 3 Scorers of EPL\n")
        print(f'{name: <{width}}',goal)
    
        second = soup.find_all('li', attrs = {"class": "statsRow"})
        second_info = soup.find_all(class_="teamInfo")
        
        for i in range(2):
            second_name = second_info[i].find('a' , attrs = {"class" : "statName"}).get_text()
            second_goal = get_num(second[i].find(class_="stat").get_text())
            print(f'{second_name: <{width}}',second_goal)
        news=soup.find_all(class_="wrapper")[1].find(class_="mainWidget")
        
        print(news)
    else:
        page = requests.get("https://www.statbunker.com/competitions/TopGoalScorers?comp_id=600")
        soup = BeautifulSoup(page.content, 'html.parser')
        odd = soup.find(class_='table').find('tbody').find_all('tr')
        print("Top 10 Scorers of LaLiga\n")
        
        for i in range(5):
            odd_name = odd[i].find('p').get_text()
            odd_mobs = odd[i].find_all(class_="mob")
            odd_goals = odd_mobs[2].get_text()
            
            print(f'{odd_name: <{width}}',odd_goals)

def points_table(opt):
    width=20
    if(int(opt)==1):
        page = requests.get("http://www.espn.in/football/table/_/league/eng.1")
    else:
        page = requests.get("http://www.espn.in/football/table/_/league/esp.1")
    soup = BeautifulSoup(page.content, 'html.parser')
    rows = soup.find_all("tr",{"class":"standings-row"})
    h1 = "   Team - Name"
    h2 = "Points"
    print(f'{h1:<{width}}','  ', h2)
    for i in range(10):
        team_names = rows[i].find('span',{'class':'team-names'}).get_text()
        points = rows[i].find_all('td')[8].get_text()
        print(f'{team_names:<{width}}','    ',points)

        
# Start of the program

print("Enter mode, foo or dev ?")
mode = input()

if(mode=="dev"):
    os.system('python cc_rating.py')
    exit()
    
inp = 0
while(int(inp)!=3):
    print("Enter League option:")
    print("1. EPL")
    print("2. LaLiga")
    print("3. Exit")
    inp = input()
    if(int(inp)==3):
        print("             Thanks ! Bye")
        exit()
    else:
        print("Enter choice:\n1. Top Scorers\n2. Points Table\n")
        ch = input()
        top_scorers(inp) if int(ch) == 1 else points_table(inp)
    print()        
#Author: Joey
#Description: Python web scraper/fortnite stats
#10/10/18
import time
import requests
import threading
from requests import get
from bs4 import BeautifulSoup

user = str(input("Username: "))
url = requests.get("https://www.stormshield.one/pvp/stats/"+user)
soup = BeautifulSoup(url.content,'html.parser')

[type(item) for item in list(soup.children)]

html = list(soup.children)[1]
text = soup.find(class_="row overview__body").get_text()
data = text.split("\n")

wins = data[5]
solo = data[10]
duos = data[22]
squad = data[34]

kills = data[50]
solok = data[55]
duosk = data[64]
squadk = data[73]

matches = data[122]
solom = data[127]
duosm = data[136]
squadm = data[145]


print("-"*42)
print("Matches: {}\nSolo Matches: {}\nDuos Matchea: {}\nSquad Matchea: {}".format(matches,solom,
    duosm,squadm))

print("------------------------------------------")
print("Wins       Solo       Duos        Squad")
print("------------------------------------------")
print("{}   |   {}   |   {}   |   {}   ".format(wins,solo,duos,squad))
print("------------------------------------------")
print("Kills      Solo       Duos        Squad")
print("------------------------------------------")
print("{}  |   {}   |   {}   |   {}    ".format(kills,solok,duosk,squadk))
print("------------------------------------------")

#Will be updated soon...

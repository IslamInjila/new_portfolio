import urllib.request
from bs4 import BeautifulSoup
soup = BeautifulSoup(urllib.request.urlopen("https://graphics.reuters.com/world-coronavirus-tracker-and-maps/vaccination-rollout-and-access/")
.read(),'lxml')

C:\Users\injil\OneDrive\Documents\new_portfolio\images\datascarpe.py


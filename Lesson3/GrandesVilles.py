# coding: utf-8

import json
import pandas as pd
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json


# Parameters
url_ville = "https://www.insee.fr/fr/statistiques/1906659?sommaire=1906743"
api = "https://fr.distance24.org/route.json?stops="

def build_soup(url):
    res = requests.get(url)
    if res.status_code == 200:
        html_doc = res.content
        soup = BeautifulSoup(html_doc, "html.parser")
        return soup


def get_top_ville(soup):
    soup = build_soup(url_ville)
    table = soup.find("table", id="produit-tableau-T16F014T4").find('tbody')
    rows = table.find_all('tr')
    rows = rows[0:50]
    list_ville = []
    for row in rows:
        ville = row.find_next('th').find_next('th').text
        list_ville.append(ville)
    return list_ville

soup = build_soup(url_ville)
towns = get_top_ville(soup)
df = pd.DataFrame(index= [towns], columns= [towns])
# print(df)

 

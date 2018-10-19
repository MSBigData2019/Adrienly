# coding: utf-8

import json
import pandas as pd
from bs4 import BeautifulSoup
import requests

# Parameters
acces_token = ""
url_page = "https://gist.github.com/paulmillr/2657075"
head = {'Authorization': 'token {}'.format('')}
url_get = "https://api.github.com/users/{}/repos?access_token={}&page={}"
df = pd.DataFrame(columns = ['contributors', 'average_stargazers'])


def build_soup(url):
    res = requests.get(url)
    if res.status_code == 200:
        html_doc = res.content
        soup = BeautifulSoup(html_doc, "html.parser")
        return soup

def _get_top_contributors(soup):
    table = soup.find("table").find('tbody')
    rows = table.find_all('tr')
    list_cont = []
    for row in rows:
        cont = row.find_next("td").text
        cont = cont.split(" ")
        list_cont.append(cont[0])
    return list_cont

def get_mean_stars_users(listcontrib):
    #Initialisation des variables
    dico_mean_stars = {}
    list_stars_mean = []

    dico_mean_stars["login"] = listcontrib 
    for i in range(len(listcontrib)):
        sum_stars = 0
        mean_stars = 0
        get_repo = requests.get(url_get.format(listcontrib[i], acces_token, 1))
        if get_repo.status_code == 200:
            get_json = json.loads(get_repo.content)
            for j in range(len(get_json)):
                sum_stars += get_json[j].get("stargazers_count")
            mean_stars = sum_stars/len(get_json)
            list_stars_mean.append(mean_stars)
            dico_mean_stars["mean"] = list_stars_mean
#    df_users_stars_mean = pd.DataFrame.from_dict(dico_mean_stars)
    # print(df_users_stars_mean)
    return dico_mean_stars

def main():
    soup = build_soup(url_page)
    df['contributors'] = _get_top_contributors(soup)
    df['average_stargazers'] = get_mean_stars_users(df['contributors'])
    print(df.sort_values('average_stargazers', ascending=False).to_string())
    
 



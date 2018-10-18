# coding: utf-8

# import re
# import unittest
import json
import argparse
from bs4 import BeautifulSoup
import requests
from jq import jq
import pprint

url_page = "https://gist.github.com/paulmillr/2657075"
res = requests.get(url_page)
if res.status_code == 200:
    html_doc = res.text
    soup = BeautifulSoup(html_doc, "html.parser")

table = soup.find("table").find('tbody')
rows = table.find_all('tr')
list_cont = []
for row in rows:
    cont = row.find_next("td").text
    cont = cont.split(" ")
    list_cont.append(cont[0])
print(list_cont)

token = "dbf09a3d5e0b47b313e454c5a33069c7870ef712"
head = {'Authorization': 'adrienly' + token}
url_api = f"https://api.github.com/search/users/fabpot/repo"
r = requests.get(url_api, headers = head, verify = False)
data = r.json()
pprint.pprint(r)


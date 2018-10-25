# coding: utf-8

import json
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


# parameters

url_api = "https://open-medicaments.fr/api/v1/medicaments?query=paracetamol&limit=100"




def get_json(url):
    res = requests.get(url)
    get_jason = json.loads(res.content)
    return get_jason

json_para = get_json(url_api)
df_para = pd.DataFrame(json_para)

string = "PARACETAMOL ZYDUS 500 mg, gélule"

# definition du regex
reg = r'([\D]*)(\d+)(.*),(.*)'
print(re.findall(reg,string))
serie = df_para["denomination"]

#transformation de la DF en Serie et modification des colonnes 
ds = serie.str.extract(reg)
ds["mul"]=1000
ds["mul"]= ds["mul"].where(ds[2].str.strip()=="g",1)
ds['dosage'] = ds[1].fillna(0).astype(int)*ds['mul']
print(ds.head(20))
print(df_para)

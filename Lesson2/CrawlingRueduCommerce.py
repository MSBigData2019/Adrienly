
import requests
import unittest
from bs4 import BeautifulSoup
import re


url_prefix = "https://www.fnac.com/PC-portable-Acer/Par-marque/nsh50321/w-4?ItemPerPage=20&SDM=list&sl"


url = url_prefix + "acer"


#def _search_in_grid(grid, selector, dist_from_selector):
#    for element in grid:
#        all_price = 



res= requests.get(url)
if res.status_code == 200:
    html_doc = resh.text
    soup_search = BeautifulSoup(html_doc,"html.parser")


    discount = soup.find("section", class_ = "grid").find("div", class_ = "price").text
    print("discount")

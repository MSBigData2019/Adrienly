# coding: utf-8
import requests
import unittest
from bs4 import BeautifulSoup
import re

# mmentaire


print("Veuillez appeler la fonction main() avec pour attribut le nom du groupe que vous souhaitez. Exemple : main(\"danone\")")
def main(group):

    search_url_prefix = "https://www.reuters.com/finance/stocks/lookup?searchType=any&comSortBy=marketcap&sortBy=&dateRange=&search="

    url_page_search = search_url_prefix + group
    res_search = requests.get(url_page_search)
    if res_search.status_code == 200:
        html_doc = res_search.text
        soup_search = BeautifulSoup(html_doc,"html.parser")
 #       print(soup_search.text)
    sygle = soup_search.find("table", class_ = "search-table-data").find_next("td").find_next("td").text

    print("sygle = " + sygle)
    website_prefix = "http://www.reuters.com/finance/stocks/financial-highlights/"


    # if group == "airbus":
    #     web_suffix = "AIR.PA"
    # if group == "lvmh":
    #     group = "LVMH"
    #     web_suffix = "LVMH.PA"
    # if group == "danone":
    #     web_suffix = "DANO.PA"
    # else:
    #     print("Le groupe demande n'est pas dans la base de donnee connu ici...")

    url_page = website_prefix + sygle

    res = requests.get(url_page)


    if res.status_code == 200:
        html_doc = res.text
        soup = BeautifulSoup(html_doc,"html.parser")
        specific_class = "sectionQuote nasdaqChange"
        specific_class2 = "font-size: 23px;"
        specific_class3 = "sectionQuoteDetail"
        specific_class4 = "pos"

        valueStock = (soup.find("div", class_= specific_class).find("span", attrs={"style": "font-size: 23px;"}).text)
        valuePercent = (soup.find("div", class_= "sectionQuote priceChange").find("span", class_ = "valueContentPercent").text)
   
        def _search_in_tables(tables, selecter, dist_from_selecter):
            for table in tables:
                all_td = table.find_all("td")
                for i, td in enumerate(all_td):
                    if selecter in td.text:
                        return all_td[i+dist_from_selecter].text

        all_small_tables = soup.find("div", class_= "column2 gridPanel grid4").find_all("tbody", class_= "dataSmall")

        share_Owned = _search_in_tables(all_small_tables, "Shares Owned:", 1).strip()


        all_big_tables = soup.find("div", class_= "column1 gridPanel grid8").find_all("table", class_= "dataTable")
        quarter_dec = _search_in_tables(all_big_tables, "Quarter Ending Dec-18", 2).strip()
        cie_dividend_yield = _search_in_tables(all_big_tables, "Dividend Yield", 1).strip()
        ind_dividend_yield = _search_in_tables(all_big_tables, "Dividend Yield", 2).strip()
        sect_dividend_yield = _search_in_tables(all_big_tables, "Dividend Yield", 3).strip()
   
        print("groupe :" + group)
        print("Shares Owned :" + share_Owned)
        print("Mean quarter Ending Dec 2018 = " + quarter_dec.replace(",", " "))
        print("Stock Value = " + valueStock.strip())
        print("% change = " + valuePercent.strip().strip('(%)'))
        print("Dividend Yield for :")
        print("  Company = " + cie_dividend_yield)
        print("  Industry= " + ind_dividend_yield)
        print("  Sector= " + sect_dividend_yield)
    




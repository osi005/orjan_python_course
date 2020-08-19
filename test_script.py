# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:11:01 2020

@author: 104460KM079
"""
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import os
import requests
from bs4 import BeautifulSoup


USERN = os.getenv("USER")
PASSWORD = os.getenv("PASSW")
url = "http://mycbmreports.karstenmoholt.com/modal/kamo_webreport/kamo_status_history_items/history/128"
url2 = "http://mycbmreports.karstenmoholt.com/kamo_webreport/kamo_machine_trains/index/location:33"
pdfurl = "http://mycbmreports.karstenmoholt.com/kamo_webreport/kamo_status_history_items/generatePdf/96196/My_CBM_report.pdf"
test_url = "http://mycbmreports.karstenmoholt.com/kamo_webreport/kamo_locations/location_overview/33"


response = requests.get(url, auth=(USERN, PASSWORD))

soup = BeautifulSoup(response.content, 'html.parser') #html.parser
table = soup.find_all('table')
df = pd.read_html(str(table))[0] # converts from soup bt4 to pandas dataframe


print(df)
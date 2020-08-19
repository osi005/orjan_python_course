# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 08:26:58 2020

@author: 104460KM079
"""
from dotenv import load_dotenv
load_dotenv()
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


def get_first_data_struct(url):
    '''
    Function that returns json data object from url...
    '''
    try:
        r = requests.get(url, auth=(USERN, PASSWORD))
        report_object = r.json() #printing the json object
        report = report_object['data']
        return report
    except Exception as E:
        print(E)


def filter_first_data_struct():
    '''
    Function that call get_data function.
    The data get filtered according to useful_keys,
    and returned as filtered_data
    '''
    url = "http://mycbmreports.karstenmoholt.com/api/kamo_webreport/kamo_machine_trains.json?api_key=dcb87dd4436bf24ed82dee0d0ee2435a"
    pay_load = get_first_data_struct(url)
    
    useful_keys = ['id', 'location_id', 'area_id', 'name', 'sfi_tag']
    filtered_data = [] #initializing empty list 
    #filtered_dict_firstlevel = {} # not currently in use
    
    for item_dict in pay_load: 
        '''Loops over all items (dictionaries) in pay_load (list)
        ''' 
        filtered_dict_secondlevel = {} # (re)initializing empty dict 
        keys = list(item_dict.keys())[0] # extracting list of keys  
        data_dict = item_dict[keys]          #henter 
        
        for key, value in data_dict.items():
            if key in useful_keys:
                filtered_dict_secondlevel[key] = value
        filtered_data.append(filtered_dict_secondlevel)
    #print(filtered_data)
    return filtered_data


def get_location_name_from_id(input_data):
    # Iterate over specific column from the dataframe
    #location_name_dict = {33: 'Båt1', 34: 'Båt2', 35: 'Båt3', 313: 'Båt66' }
    #input_data['vessel_name'] = location_name_dict
    
    #map data with dict
    #df['Capital'] = df['Country'].map(country_capital)
    
    base_url = "http://mycbmreports.karstenmoholt.com/kamo_webreport/kamo_machine_trains/index/location:"
    # Creating dict with location_id as key, which also removes dublicate keys
    get_vessel_name_dict = dict.fromkeys(input_data['location_id'])
    
    for key in get_vessel_name_dict:
        print('Finding vessel_name for vessel_id: ', key)
        url = base_url + key
        print('Request url content')
        print(url)
        response = requests.get(url, auth=(USERN, PASSWORD))
        soup = BeautifulSoup(response.content, 'html.parser') #html.parser
        table = soup.find_all('table')
        df = pd.read_html(str(table))[0]
        print(df)
        time.sleep(1)
        
    
    
    
    '''
    for column in input_data[['location_id']]:
        columnSeriesObj = input_data[column]
        print('Column Contents : ', columnSeriesObj.values)
        print(input_data[column])
    '''  
    input_data.to_csv('mycbm_data.csv')
    return "Tjommi"


if __name__ == "__main__":
    # Main code
    # extracting password and user
    
    USERN = os.getenv("USER")
    PASSWORD = os.getenv("PASSW")
    
       
    mydata = pd.DataFrame(filter_first_data_struct())
    get_location_name_from_id(mydata)
    
    #mydata.to_csv('mycbm_data.csv') #, index=False

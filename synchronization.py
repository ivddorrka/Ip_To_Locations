import requests
import pandas as pd
import shutil
import re
import sys


def get_location(ip_address, api_key):
    url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    location = {
        "city": data["city"],
        "region_name": data["region_name"],
        "country": data["country_name"],
        "continent_name": data["continent_name"]
    }

    print(f"IP = {ip_address}, specifics: {location}")
    return location


def diff_between_api(file_a, file_b):
    return 2

def input_out_file(input_file_path, last_remembered_file_path):

    try:
        df1 = pd.read_excel(input_file_path)
    except:
        print("Input file doesn't exist by the given path")
        sys.exit(1)

    column_data_1 = ''
    try:
        column_data_1 = df1['IP']
    except KeyError:
        print("ip column has a wrong name, should be 'IP' using latin symbols")
        sys.exit(1)

    column_data_2 = []
    try:
        df2 = pd.read_excel(last_remembered_file_path)
        column_data_2 = df2['IP']
    except:
        pass

    
    i_to_start_with = 0
    for i in range(max(len(column_data_1), len(column_data_2))):
        try:
            print(column_data_1[i], column_data_2[i])
            if column_data_1[i]!=column_data_2[i]:
                i_to_start_with = i
                break
        except :
            i_to_start_with = i
            break
        i_to_start_with = i

    if i_to_start_with != max(len(column_data_1), len(column_data_2))-1:
        ip_regex = r'^(\d{1,3}\.){3}\d{1,3}$'


        cities =  []
        region_names = []
        countries = []
        continent_names = []

        for i in range(i_to_start_with, max(len(column_data_1), len(column_data_2))):
            
            
            ip_address = column_data_1[i]
            
            if re.match(ip_regex, ip_address):
                js_responce = get_location(ip_address, api_key)
                cities.append(js_responce['city'])
                region_names.append(js_responce['region_name'])
                countries.append(js_responce['country'])
                continent_names.append(js_responce['continent_name'])
            else:
                cities.append('')
                region_names.append('')
                countries.append('')
                continent_names.append('')

        try:
            cities_1 = df2['city']
            region_names1 = df2['region']
            countries_1 = df2['country']
            continent_names_1 = df2['continent']
        except:
            cities_1 = []
            region_names1 = []
            countries_1 = []
            continent_names_1 = []

        df1['city'] = list(cities_1)[:i_to_start_with] + list(cities)
        df1['region'] = list(region_names1)[:i_to_start_with]  + list(region_names)
        df1['country'] = list(countries_1)[:i_to_start_with] +list(countries)
        df1['continent'] = list(continent_names_1)[:i_to_start_with] +list(continent_names)

        
        df1.to_excel(input_file_path, index=False)
    return 0

api_key = ''
with open('my_key_file.txt', 'r') as file:
    api_key = file.readline()
    if not api_key:
        print("API not specified, visit https://ipstack.com/plan to get one. \nAPI should be added to my_key_file.txt as first line")


input_file = sys.argv[1]
last_remembered_file_path = "locations_fromIP_generated.xlsx"


input_out_file(input_file, last_remembered_file_path)
print(f"Results have been saved in {input_file} and {last_remembered_file_path}")
shutil.copy2(input_file, last_remembered_file_path)
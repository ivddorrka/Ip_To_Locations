import requests
import pandas as pd
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

    return location


def read_file(file_path, ip_column_name, api_key):
    df = pd.read_excel(file_path)
    column_data = df[ip_column_name]
    ip_regex = r'^(\d{1,3}\.){3}\d{1,3}$'
    cities =  []
    region_names = []
    countries = []
    continent_names = []

    for ip_address in column_data:
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
    
    df['city'] = cities
    df['region'] = region_names
    df['country'] = countries
    df['continent'] = continent_names

    df.to_excel(file_path, index=False)

        
file_path = sys.argv[1]  # read the first argument
ip_column_name = sys.argv[2]  # read the second argument
api_key = sys.argv[3]  # read the third argument


if __name__=="__main__":
    read_file(file_path, ip_column_name, api_key)



"""
EVE Market Search!
"""
import csv
import requests
import sys
import os

def resource_path(relative_path):
    """
    This function is needed for PyInstaller to correctly use
    the absolute paths to referenced files. See the following
    link for details: https://stackoverflow.com/a/49802075
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def lookup_item_id(given_name):
    """Takes given item name and returns the item type_id"""
    csv_file = resource_path('invTypes.csv')
    with open(csv_file, encoding="utf8") as r_file:
        reader = csv.reader(r_file)
        for row in reader:
            if str(given_name).upper() == row[2].upper():
                return row[0]
        # If item is not found, return None
        return None

def add_commas(number):
    """Add commas to large numbers for legibility"""
    return "{:,}".format(float(number))

def determine_system(arg):
    """Decides hub to search based on given argument"""
    system_dict = {
        'AMARR': 60008494,
        'DODIXIE': 60011866,
        'HEK': 60005686,
        'JITA': 60003760,
        'RENS': 60004588
    }
    if arg in system_dict.keys():
        return system_dict[arg]

def search_market(item_id, hub):
    """Takes type_id and makes request to Fuzzwork market API"""
    # Request JSON data
    url = f'https://market.fuzzwork.co.uk/aggregates/?station={hub}&types={item_id}'
    req = requests.get(url)
    result = req.json()

    # Assign values and add commas to number
    market_info = {}
    market_info['max_buy'] = add_commas(result[f'{item_id}']['buy']['max'])
    market_info['min_sell'] = add_commas(result[f'{item_id}']['sell']['min'])
    market_info['buy_orders'] = add_commas(result[f'{item_id}']['buy']['orderCount'])
    market_info['buy_volume'] = add_commas(result[f'{item_id}']['buy']['volume'])
    market_info['sell_orders'] = add_commas(result[f'{item_id}']['sell']['orderCount'])
    market_info['sell_volume'] = add_commas(result[f'{item_id}']['sell']['volume'])

    return market_info

"""
EVE Market Search!
At the moment it only searches Jita, but I plan on implementing
a more robust search feature in the future.
"""

import sys
import csv
import requests

def lookup_item_id(given_name):
    """Takes given item name and returns the item type_id"""
    csv_file = 'invTypes.csv'
    with open(csv_file, encoding="utf8") as r_file:
        reader = csv.reader(r_file)
        for row in reader:
            if str(given_name).upper() == row[2].upper():
                return (row[0], row[2])
        print('No items found by that name. Is it spelled correctly?')
        sys.exit()

def add_commas_to_number(number):
    """Add commas to large numbers for legibility"""
    return "{:,}".format(float(number))

def search_market(item_id, item_name):
    """Takes type_id and makes request to Fuzzwork market API"""
    # Request JSON data
    url = f'https://market.fuzzwork.co.uk/aggregates/?station=60003760&types={item_id}'
    r = requests.get(url)
    result = r.json()

    # Assign values
    max_buy = result[f'{item_id}']['buy']['max']
    min_sell = result[f'{item_id}']['sell']['min']
    buy_volume = result[f'{item_id}']['buy']['volume']
    sell_volume = result[f'{item_id}']['sell']['volume']
    title = f'====Jita Price: {item_name}===='

    return print_prices(title, min_sell, max_buy, sell_volume, buy_volume)

def print_prices(title, min_sell, max_buy, sell_volume, buy_volume):
    """Print the results"""
    print('')
    print(title)
    print(f'Min Sell: {add_commas_to_number(min_sell)} ISK')
    print(f'Units: {add_commas_to_number(sell_volume)}')
    print('')
    print(f'Max Buy: {add_commas_to_number(max_buy)} ISK')
    print(f'Units: {add_commas_to_number(buy_volume)}')
    print('=' * len(title))

def main():
    """Main function"""
    item_ids = []
    user_input = sys.argv[1:]
    for item in user_input:
        item_ids.append(lookup_item_id(item))
    for item_id, item_name in item_ids:
        search_market(item_id, item_name)

if __name__ == '__main__':
    main()

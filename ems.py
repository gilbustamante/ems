"""
EVE Market Search!
At the moment it only searches Jita, but I plan on implementing
a more robust search feature in the future.
"""

import sys
import csv
import argparse
import requests

def setup_argparse():
    """Setup argument parser"""
    # Initialize parser
    parser = argparse.ArgumentParser(description='Simple market search for EVE Online trade hubs.')

    # Add arguments
    parser.add_argument('-a',
                        '-amarr',
                        action='store_true',
                        help='Search the Amarr market hub')
    parser.add_argument('-r',
                        '-rens',
                        action='store_true',
                        help='Search the Rens market hub')
    parser.add_argument('-d',
                        '-dodixie',
                        action='store_true',
                        help='Search the Dodixie market hub')
    parser.add_argument('-hek',
                        action='store_true',
                        help='Search the Hek market hub')
    parser.add_argument('Query',
                        metavar='query',
                        nargs='+',
                        type=str,
                        help='Item to search for.')

    # Execute parse_args
    args = parser.parse_args()

    return args

def lookup_item_id(given_name):
    """Takes given item name and returns the item type_id"""
    csv_file = 'invTypes.csv'
    with open(csv_file, encoding="utf8") as r_file:
        reader = csv.reader(r_file)
        for row in reader:
            if str(given_name).upper() == row[2].upper():
                return row[0]
        return None

def add_commas_to_number(number):
    """Add commas to large numbers for legibility"""
    return "{:,}".format(float(number))

def determine_system(arg):
    """Decides hub to search based on given argument"""
    if arg.upper() == 'AMARR':
        system = 60008494
    elif arg.upper() == 'RENS':
        system = 60004588
    elif arg.upper() == 'DODIXIE':
        system = 60011866
    elif arg.upper() == 'HEK':
        system = 60005686
    elif arg.upper() == 'JITA':
        system = 60003760
    return system

def search_market(item_id, hub):
    """Takes type_id and makes request to Fuzzwork market API"""
    # Request JSON data
    url = f'https://market.fuzzwork.co.uk/aggregates/?station={hub}&types={item_id}'
    req = requests.get(url)
    result = req.json()

    # Assign values
    market_info = {}
    market_info['max_buy'] = add_commas_to_number(result[f'{item_id}']['buy']['max'])
    market_info['min_sell'] = add_commas_to_number(result[f'{item_id}']['sell']['min'])
    market_info['buy_orders'] = add_commas_to_number(result[f'{item_id}']['buy']['orderCount'])
    market_info['buy_volume'] = add_commas_to_number(result[f'{item_id}']['buy']['volume'])
    market_info['sell_orders'] = add_commas_to_number(result[f'{item_id}']['sell']['orderCount'])
    market_info['sell_volume'] = add_commas_to_number(result[f'{item_id}']['sell']['volume'])

    return market_info

# def print_prices(title, min_sell, max_buy, sell_volume, buy_volume):
#     """Print the results"""
#     print('')
#     print(title)
#     print(f'Min Sell: {add_commas_to_number(min_sell)} ISK')
#     print(f'Units: {add_commas_to_number(sell_volume)}')
#     print('')
#     print(f'Max Buy: {add_commas_to_number(max_buy)} ISK')
#     print(f'Units: {add_commas_to_number(buy_volume)}')
#     print('=' * len(title))

def main():
    """Main function"""
    query = setup_argparse()
    item_ids = []
    user_input = query.Query
    determine_system(query)
    for item in user_input:
        item_ids.append(lookup_item_id(item))
    for item_id, item_name in item_ids:
        search_market(item_id, item_name, query)

if __name__ == '__main__':
    main()

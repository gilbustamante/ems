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
                return (row[0], row[2])
        print('No items found by that name. Is it spelled correctly?')
        sys.exit()

def add_commas_to_number(number):
    """Add commas to large numbers for legibility"""
    return "{:,}".format(float(number))

def determine_system(arg):
    """Decides hub to search based on given argument"""
    if arg.a:
        system = 60008494
    elif arg.r:
        system = 60004588
    elif arg.d:
        system = 60011866
    elif arg.hek:
        system = 60005686
    else:
        system = 60003760
    return system

def search_market(item_id, item_name, given_args):
    """Takes type_id and makes request to Fuzzwork market API"""
    # Get system info
    system = determine_system(given_args)

    # Request JSON data
    url = f'https://market.fuzzwork.co.uk/aggregates/?station={system}&types={item_id}'
    req = requests.get(url)
    result = req.json()

    # Assign values
    max_buy = result[f'{item_id}']['buy']['max']
    min_sell = result[f'{item_id}']['sell']['min']
    buy_volume = result[f'{item_id}']['buy']['volume']
    sell_volume = result[f'{item_id}']['sell']['volume']
    if given_args.a:
        title = f'====Amarr Price: {item_name}===='
    elif given_args.r:
        title = f'====Rens Price: {item_name}===='
    elif given_args.d:
        title = f'====Dodixie Price: {item_name}===='
    elif given_args.hek:
        title = f'====Hek Price: {item_name}===='
    else:
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

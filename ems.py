#!/usr/bin/env python
"""
EVE Market Search!
"""
import argparse
from pathlib import Path
import requests
import sys
from helpers import add_commas, lookup_item_id, determine_system, print_info

# TODO: Add absolute path for saving invTypes.csv.bz2

def arguments():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", action="help",
                        help="Show this message and exit")

    parser.add_argument("-a", "--amarr", action="store_true",
                        help="Search Amarr 8 EFA")

    parser.add_argument("-d", "--dodixie", action="store_true",
                        help="Search Dodixie 9-20 FNAP")

    parser.add_argument("-h", "--hek", action="store_true",
                        help="Search Hek 8-12 BCF")

    parser.add_argument("-j", "--jita", action="store_true",
                        help="Search Jita 4-4 CNAP")

    parser.add_argument("-r", "--rens", action="store_true",
                        help="Search Rens 6-8 BTT")

    parser.add_argument("-u", "--update", action="store_true",
                        help="Download newest item ID list")

    parser.add_argument("item_name", type=str, nargs="?",
                        help="Item to search for")
    args = parser.parse_args()
    return args

def search_market(item_id, hub):
    """Takes type_id and makes request to Fuzzwork market API"""
    # Request JSON data
    url = f'https://market.fuzzwork.co.uk/aggregates/?station={hub}&types={item_id}'
    req = requests.get(url)
    result = req.json()

    # Assign values and add commas to numbers for readability
    market_info = {}
    try:
        market_info['max_buy'] = add_commas(result[item_id]['buy']['max'])
        market_info['min_sell'] = add_commas(result[item_id]['sell']['min'])
        market_info['buy_orders'] = add_commas(result[item_id]['buy']['orderCount'])
        market_info['buy_volume'] = add_commas(result[item_id]['buy']['volume'])
        market_info['sell_orders'] = add_commas(result[item_id]['sell']['orderCount'])
        market_info['sell_volume'] = add_commas(result[item_id]['sell']['volume'])
    except KeyError:
        print(f"Item does not exist (check spelling)")
        sys.exit()

    return market_info

def update_item_list():
    filename = 'invTypes.csv.bz2'
    url = 'https://www.fuzzwork.co.uk/dump/latest/invTypes.csv.bz2'
    file_abs_path = Path(filename).resolve()

    # Begin update
    answer = input(f"Do you want to download/update {filename}? (y/n): ")
    if answer.upper() in ['N', 'NO']:
        print("Aborting...")
        sys.exit()
    elif answer.upper() in ['Y', 'YES']:
        try:
            print(f"Downloading... ", end="")
            r = requests.get(url)
            print("OK.")
            with open(file_abs_path, 'wb') as f:
                f.write(r.content)
        except (ConnectionError, TimeoutError) as e:
            print(f"Error: {e}")

        # Make sure it's there now:
        print("Checking file... ", end="")
        if file_abs_path.is_file():
            print(f"OK.")
        else:
            print(f"ERROR: {filename} could not be found.")
    else:
        print(f"Invalid answer; exiting.")
        sys.exit()

if __name__ == '__main__':
    args = arguments()
    if args.update:
        update_item_list()
        sys.exit()
    id_ = lookup_item_id(args.item_name)
    for arg in vars(args):
        if getattr(args, arg) == True and arg != 'update':
            info = search_market(id_, determine_system(arg))
            print_info(arg.title(), args.item_name, info)

"""
EVE Market Search!
"""
import argparse
import requests
from helpers import add_commas, lookup_item_id, determine_system, print_info

def arguments():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", action="help", help="Show this message and exit")
    parser.add_argument("-a", "--amarr", action="store_true", help="Search Amarr 8 EFA")
    parser.add_argument("-d", "--dodixie", action="store_true", help="Search Dodixie 9-20 FNAP")
    parser.add_argument("-h", "--hek", action="store_true", help="Search Hek 8-12 BCF")
    parser.add_argument("-j", "--jita", action="store_true", help="Search Jita 4-4 CNAP")
    parser.add_argument("-r", "--rens", action="store_true", help="Search Rens 6-8 BTT")
    parser.add_argument("item_name", type=str, help="Item to search for")
    args = parser.parse_args()
    return args

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


if __name__ == '__main__':
    args = arguments()
    id_ = lookup_item_id(args.item_name)
    for arg in vars(args):
        if getattr(args, arg) == True:
            info = search_market(id_, determine_system(arg))
            print_info(arg.title(), args.item_name, info)

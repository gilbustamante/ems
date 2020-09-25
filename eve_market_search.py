"""EVE Market Search"""

import requests
import csv

def find_item_name(item_id):
    """Looks up item_id in csv file and returns the name"""
    csv_file = 'invTypes.csv'
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            if str(item_id) == row[0]:
                return row[2]
            else:
                continue

if __name__ == '__main__':
    item_id = '34'
    print(find_item_name(item_id))
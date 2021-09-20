"""Helper functions for EMS"""
import sys
import csv
import bz2

def lookup_item_id(given_name):
    """Takes given item name and returns the item type_id"""
    try:
        with bz2.open('invTypes.csv.bz2', 'rt', encoding="utf-8") as f:
            csv_content = csv.reader(f)
            for line in csv_content:
                if given_name.upper() == line[2].upper():
                    return line[0]
            return None
    except FileNotFoundError:
        print("Item list not found. Please run this script with the -u flag "
              "to update (python ems.py -u)")
        sys.exit()
    except AttributeError as e:
        print(f"Error: {e}")
        print("Did you forget to provide an item name?")
        sys.exit()


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
    return system_dict[arg.upper()]

def print_info(system_name, item_name, info_obj):
    print("===============================")
    print(f"System: {system_name}")
    print(f"Item: {item_name}\n")
    for k, v in info_obj.items():
        print(f"{k}: {v}")
    print("===============================")

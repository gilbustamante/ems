"""Helper functions for EMS"""
import sys
import csv
import bz2


def lookup_item_id(given_name):
    """Takes given item name and returns the item type_id"""
    try:
        with bz2.open('invTypes.csv.bz2', 'rt', encoding="utf-8") as f:
            csv_content = csv.reader(f)
            inc_results = create_match_list(given_name, csv_content)
            if len(inc_results) == 0:
                quit_with_msg("No results found.")
            elif len(inc_results) == 1:
                return inc_results[0]
            for idx, item_name in enumerate(inc_results):
                print(f"{idx}.", item_name[0])
            choice = input("\nEnter an item number: ")
            if choice.isdigit():
                return inc_results[int(choice)]
            else:
                quit_with_msg("Please enter a valid item number.")
    except FileNotFoundError:
        quit_with_msg("Item list not found. Please run this script with the -u "
                     "flag to update (python ems.py -u)")
    except KeyboardInterrupt:
        quit_with_msg("Aborting.")


def create_match_list(search_query, csv_object):
    """Returns a list of possible search matches"""
    search_results = []
    for line in csv_object:
        if search_query.upper() in line[2].upper():
            search_results.append((line[2], line[0]))
    return search_results


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
    """Prints collected output to stdout"""
    print("===============================")
    print(f"System: {system_name}")
    print(f"Item: {item_name}\n")
    for k, v in info_obj.items():
        print(f"{k}: {v}")
    print("===============================")

def quit_with_msg(msg="Quitting..."):
    """Prints a message and quits"""
    import sys
    print(msg)
    sys.exit()

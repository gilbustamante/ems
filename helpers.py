"""Helper functions for EMS"""

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

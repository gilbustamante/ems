# EVE Market Search

![](https://i.imgur.com/MHzJ3Ju.gif)

Basic CLI market search for EVE Online. EMS allows you to search any (or all) of the main trade hubs for a specific item and returns:

* The maximum buy order price.
* The minimum sell order price.
* Total buy/sell orders.
* Total buy/sell volume (how many individual items are ordered/listed).

...for each hub specified.

## Setup

EMS requires Python 3 or later.

1. This program uses the <code>requests</code> Python library (for API calls to the [Fuzzworks Market Data API](https://market.fuzzwork.co.uk/api/)). You can install `requests` with the following command: 

   `python -m pip install requests`

2. EMS finds item IDs by checking the user's query against a `.csv` file containing information about every item in the game. You can use the `-u` option to have EMS automatically download the correct file:

   `python ems.py -u`

   The file it downloads ([`invTypes.csv.bz2`](https://www.fuzzwork.co.uk/dump/latest/invNames.csv.bz2)) is about ~1.3 MB.

3. You're done!

## Usage

To search for an item:

`python ems.py <options> <item_name>`

The main trade hubs and the corresponding option to use:

| Option Flag | Trade Hub                                             |
| ----------- | ----------------------------------------------------- |
| `-a`        | Amarr VIII (Oris) - Emperor Family Academy            |
| `-d`        | Dodixie IX - Moon 20 - Federation Navy Assembly Plant |
| `-h`        | Hek VIII - Moon 12 - Boundless Creation Factory       |
| `-j`        | Jita IV - Moon 4 - Caldari Navy Assembly Plant        |
| `-r`        | Rens VI - Moon 8 - Brutor Tribe Treasury              |

### Examples

Searching the Jita trade hub for small faction projectile ammunition:

```shell
$ python ems.py -j "republic fleet emp s"
===============================
System: Jita
Item: Republic Fleet EMP S

max_buy: 473.2
min_sell: 545.9
buy_orders: 16.0
buy_volume: 6,056,248.0
sell_orders: 34.0
sell_volume: 3,731,995.0
===============================
```

Searching the Amarr and Dodixie trade hubs for a large "deadspace" afterburner:

```shell
$ python ems.py -ad "Gist X-Type 100MN Afterburner"
===============================
System: Amarr
Item: Gist X-Type 100MN Afterburner

max_buy: 67,410,000.0
min_sell: 168,900,000.0
buy_orders: 7.0
buy_volume: 5.0
sell_orders: 10.0
sell_volume: 17.0
===============================
===============================
System: Dodixie
Item: Gist X-Type 100MN Afterburner

max_buy: 116,500,000.0
min_sell: 189,800,000.0
buy_orders: 5.0
buy_volume: 6.0
sell_orders: 3.0
sell_volume: 4.0
===============================
```

You can search using partial strings and EMS will print a list of matching items:

```shell
$ python ems.py -j "scourge fury"
0. Scourge Fury Heavy Missile
1. Scourge Fury Heavy Missile Blueprint
2. Scourge Fury Light Missile
3. Scourge Fury Light Missile Blueprint
4. Scourge Fury Cruise Missile
5. Scourge Fury Cruise Missile Blueprint
6. Scourge Fury XL Cruise Missile
7. Scourge Fury XL Cruise Missile Blueprint

Please enter an item number: 4 # <-- Selecting "Scourge Fury Cruise Missile"
===============================
System: Jita
Item: Scourge Fury Cruise Missile

max_buy: 770.0
min_sell: 829.5
buy_orders: 32.0
buy_volume: 4,379,623.0
sell_orders: 24.0
sell_volume: 6,477,951.0
===============================
```

## Recent Updates

* A "search suggestion" feature has been added, eliminating the need for the user's query string to be an exact match.
* EMS now handles the downloading and updating of the item list (a `.csv` file EMS uses to look up an item's unique ID) with the `-u` flag, instead of requiring the user to download it themselves.

## License

[GPL v3.0](LICENSE)

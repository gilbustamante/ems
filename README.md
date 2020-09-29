# (CLI) EVE Market Search
Basic command-line market search for EVE Online.
## Installation
EMS requires the <code>requests</code> module (for API calls to the [Fuzzworks Market Data API](https://market.fuzzwork.co.uk/api/)). You can install it with the following command: <code>pip install requests</code>. For the moment, EMS is only compatible with Python 3 or later.  
## Usage
Basic search syntax: <code>python ems.py your_search_here</code>  
Using the above command with no options defaults the search to Jita 4-4. If you want to search one of the other major trade hubs, use the following options with your search:
* <code>-a</code>: Amarr VIII (Oris) - Emperor Family Academy
* <code>-d</code>: Dodixie IX - Moon 20 - Federation Navy Assembly Plant
* <code>-hek</code>: Hek VIII - Moon 12 - Boundless Creation Factory
* <code>-r</code>: Rens VI - Moon 8 - Brutor Tribe Treasury  
  
If the search query is more than one word (E.g. "Inertial Stabilizers II"), you must wrap it in quotes. The query <strong>must</strong> be an exact match (for now).  
#### Searching Multiple Items At Once
You can search for multiple items by separating them with a space. (E.g. <code>python ems.py Rifter "EMP S" "1MN Afterburner I"</code>)

## Examples  
#### Searching for one item
Input:  
```
python ems.py Gila
```
Output:  
```
====Jita Price: Gila====
Min Sell: 155,100,000.0 ISK
Units: 743.0

Max Buy: 135,000,000.0 ISK
Units: 6.0
========================
```
#### Searching for multiple items
Input:
```
python ems.py Thorax "Magnetic Field Stabilizer I" 
```
Output:  
```
====Jita Price: Thorax====
Min Sell: 13,440,000.0 ISK
Units: 158.0

Max Buy: 9,929,000.0 ISK
Units: 63.0
==========================

====Jita Price: Magnetic Field Stabilizer I====
Min Sell: 82,370.0 ISK
Units: 6,145.0

Max Buy: 60,000.0 ISK
Units: 2,426.0
===============================================
```
#### Searching a system other than Jita
Input:  
```
python ems.py -a Bhaalgorn
```
Output:
```
====Amarr Price: Bhaalgorn====
Min Sell: 416,900,000.0 ISK
Units: 20.0

Max Buy: 328,500,000.0 ISK
Units: 5.0
==============================

```
## To Do
* ~~Add ability to search multiple items~~ (Done!)
* ~~Add ability to search different stations/systems/regions~~ (Done!)
* Find a way to automatically pull updated list of <code>type_id</code>
* Implement partial-name/incomplete searches
* Add a UI?

# (CLI) EVE Market Search
Basic command-line market search for EVE Online.
## Installation
EMS requires the <code>requests</code> module (for API calls). You can install it with the following command: <code>pip install requests</code>. For the moment, EMS is only compatible with Python 3 or later.  
## Usage
Basic search syntax: <code>python ems.py your_search_here</code>  
If the search query is more than one word (E.g. "Inertial Stabilizers II"), you must wrap it in quotes. The query <strong>must</strong> be an exact match (for now).  
#### Searching Multiple Items At Once
You can search for multiple items by separating them with a space. (E.g. <code>python ems.py Rifter "EMP S" "1MN Afterburner I" "Gyrostabilizer I"</code>)

## Examples  
Input:  
```
python ems.py Gila
```
Output:  
```
====Jita 4-4 CNAP Price====
Min Sell: 155,100,000.0 ISK
Orders: 91.0 (743.0 units)

Max Buy: 135,000,000.0 ISK
Orders: 6.0 (6.0 units)
===========================
```
#### Searching for multiple items
Input:
```
python ems.py Thorax "Magnetic Field Stabilizer I" "Caldari Navy Antimatter Charge M"
```
Output:  
```
====Jita Price: Thorax====
Min Sell: 13,440,000.0 ISK
Orders: 26.0 (158.0 units)

Max Buy: 9,929,000.0 ISK
Orders: 9.0 (63.0 units)
==========================

====Jita Price: Magnetic Field Stabilizer I====
Min Sell: 82,370.0 ISK
Orders: 24.0 (6,145.0 units)

Max Buy: 60,000.0 ISK
Orders: 12.0 (2,426.0 units)
===============================================

====Jita Price: Caldari Navy Antimatter Charge M====
Min Sell: 716.5 ISK
Orders: 43.0 (7,472,089.0 units)

Max Buy: 646.1 ISK
Orders: 7.0 (836,485.0 units)
====================================================
```
## To Do
* Add ability to search different stations/systems/regions
* Find a way to automatically pull updated list of <code>type_id</code>s
* Implement partial-name/incomplete searches
* Add a UI?

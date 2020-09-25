# (CLI) EVE Market Search
Basic command-line market search for EVE Online.
## Instructions
Basic search syntax: <code>python ems.py your_search_here</code>  
If the search query is more than one word (E.g. "Inertial Stabilizers II"), you must wrap it in quotes. For the moment, EMS is only compatible with Python 3 or later.
## Examples  
Input:  
```
python ems.py Gila
```
Output:  
```
---Jita 4-4 CNAP Price---
Min Sell: 155,100,000.0 ISK
Orders: 91.0 (743.0 units)

Max Buy: 135,000,000.0 ISK
Orders: 6.0 (6.0 units)
```
#### Search query with spaces
Input:
```
python ems.py "Nanite Repair Paste"
```
Output:
```
---Jita 4-4 CNAP Price---
Min Sell: 23,690.0 ISK
Orders: 97.0 (1,701,562.0 units)

Max Buy: 21,530.0 ISK
Orders: 6.0 (15,696.0 units)
```

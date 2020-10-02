# EVE Market Search
![](https://i.imgur.com/aqnoXwy.gif)  
  
#### Basic market search for EVE Online.
## Installation
EMS requires the <code>requests</code> module (for API calls to the [Fuzzworks Market Data API](https://market.fuzzwork.co.uk/api/)). If you are using the source code, you can install <code>requests</code> with the following command: <code>pip install requests</code>. EMS is only compatible with Python 3 or later.  
## Usage
To run, use the command <code>python main.py</code> in the source directory (or use the executable).
The default market hub is Jita 4-4 CNAP. You can also choose four other major hubs:
* Amarr VIII (Oris) - Emperor Family Academy
* Dodixie IX - Moon 20 - Federation Navy Assembly Plant
* Hek VIII - Moon 12 - Boundless Creation Factory
* Rens VI - Moon 8 - Brutor Tribe Treasury  
  
For the moment, <strong>the search query must be an exact match</strong>.  
## To Do
* ~~Add ability to search different stations/systems/regions~~ (Done!)
* Find a way to automatically pull updated list of <code>type_id</code>
* Implement partial-name/incomplete searches
* ~~Add a UI~~ (Done!)

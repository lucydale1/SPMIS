# System APIs

### Working APIs
* [springer](#springer) (Success, Implemented)
	* Currently the only API which is supported by the system
	* Returns JSON
* [PLOS](#plos) (Success)
	* Similar in format to springer
	* Returns JSON
* [Arxiv](#arxiv) (Success)
	* Returns XML
* [Web Of Science](#webos) (Not working)
	* Work in progress

--
<span id="springer"/>
### Springer

Using the springer API <https://dev.springer.com/>.  The JSON file is retrieved and converted into a python dictionary

```python
import requests # Used to send HTTP requests to the API
import json     # Library to convert the JSON files sent back ---> python dictionary
from pprint import pprint # A library to display nicer looking data structures
from collections import OrderedDict

# Dictionary of the Querystring parameters and constraints (see website for details)
data = {'api_key': 'd094966bbd58635d6772e3c43a0df59a', 'q': 'keyword: fossil', 'p': '10'}

# Request data from server --> JSON file returned
response = requests.get("http://api.springer.com/metadata/json", data)

# Convert the response to a Python object
jr = response.json()
    
pprint(jr)
```

--
<span id="plos"/>
### PLOS

Useful links:

* Online examples: <http://api.plos.org/solr/examples/>
* Online python example: <https://web.archive.org/web/20150923233639/http://api.plos.org/search-examples/plos_search.py>
* Register for API: <http://api.plos.org/registration/>
* Lagotto API??? (not sure on purpose of this one: <http://alm.plos.org/api>
* Legal: <http://api.plos.org/api-display-policy/> **<-- legal information to be shown**
* Instructions on linking to the papers: <https://groups.google.com/forum/#!topic/plos-api-developers/Fkpx4CrJ5Hc <-- how to link to the entire paper>

```python
import json
import requests
from pprint import pprint
import urllib

searchUrl = 'http://api.plos.org/search?'

# Dictionary of the Querystring parameters and constraints (see website for details)
data = {'api_key': '5H4vWi_YHfbNDxdcur2B', 'wt': 'json', 'q': 'author: *', 'p': '10'}

# Request data from server --> JSON file returned
response = requests.get(searchUrl, data)

# Convert the response to a Python object
j = response.json()
pprint(j['response'])

```
--
<span id="arxiv"/>
### Arxiv
* returns response as XML :0


```python
import requests
from pprint import pprint

data = {'search_query' : 'all:electron',
        'start' : '0',
        'max_results' : '1'}

response = requests.get("http://export.arxiv.org/api/query?", data)

print(response.text)
```

--
<span id="webos"/>
### Web of Science
* Request example: <http://ipscience-help.thomsonreuters.com/LAMRService/WebServiceOperationsGroup/requestAPIWoS.html>
* I (Ollie) will buy a drink for whoever manages to first successfully query this API 🍺
* Possibly way of using: https://github.com/enricobacis/wos Uploaded to PyPl so we could use this library!!!

```python
import requests

#body = {'username':'CoplestonO@cardiff.ac.uk', 'password': 'Tess3bear!'}

data = open("test.xml")

response = requests.post("https://ws.isiknowledge.com/cps/xrpc", data)

print(response)
print(response.text)
```

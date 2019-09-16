# rss-parser (In progress)
Simple lightweight rss-parser built with python 3 exclusively using python3 standard library modules. 

Currently support these formats:
* RSS 2.0

Future supported formats (ordered by priority):
* Atom
* RDF
## Usage:
```
from rss_parser.rss_parser import rss_parser
rss = rss_parser("url_to_stream")
rss.prettyPrint()
````
Example output:
```
Output:
-----------------------------------------
Title: Will ships without sailors be the future of trade?
Published: Mon, 15 Jul 2019 23:44:50 GMT
Link: https://www.bbc.co.uk/news/business-48871452
guid: https://www.bbc.co.uk/news/business-48871452
 
May saw the world's first unmanned commercial shipping operation."
.
.
.
Next feed item:
```

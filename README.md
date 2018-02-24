# metaddok

A very simpler multiple addok frontend.

Can be used to query several addok geocoding API managing different address/POI databases with a single request.

The query is sent to each backend, then results are gathered, reorganized, sorted by descending score and finally returned to the client.

## Install

Requirements:
- python 3.5
```
git clone https://github.com/cquest/metaddok.git
cd metaddok
pip install -r requirements.txt
```
## Run using gunicorn

`gunicorn metaddok:app -b 0.0.0.0:7676 -w 8`

## Demo instances

You can query all.addok.xyz, which queries 4 addok backend running:
- BANO addresses
- BAN addresses
- OSM POI
- SIRENE POI

Examples:
- http://all.addok.xyz/search?q=Aeroport+roissy
- http://all.addok.xyz/search?q=39+quai+andre+citroen+paris
- http://all.addok.xyz/search?q=71+place+corneille+poissy

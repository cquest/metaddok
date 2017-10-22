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

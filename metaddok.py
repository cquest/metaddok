import falcon
import json
import grequests


class GeocodeResource(object):
    def on_get(self, req, resp):
        # original request
        q = req.relative_uri

        # async parallel queries to backends
        urls = ['http://localhost:7878'+q,
                'http://localhost:7979'+q,
                'http://localhost:7777'+q,
                'http://localhost:7575'+q]
        rs = (grequests.get(u) for u in urls)
        results = grequests.map(rs)

        # our global agregated result
        glob = []
        for result in results:
            features = json.loads(result.text)
            for feature in features['features']:
                feature['attribution']=features['attribution']
                glob.append(feature)

        # sort by ascending scores
        glob = sorted(glob, key=lambda k: k['properties'].get('score', 0),
                      reverse=True)

        # how many results are expected ?
        if "id" in req.params:
            limit = int(req.params["id"])
        else:
            limit = 5
        # limit number of results
        if len(glob)>5:
            glob = glob[0:5]

        # send back json to client
        resp.body = json.dumps(dict(type="FeatureCollection", features=glob,
                                    licence="ODbL 1.0", version="draft"))

        resp.set_header('X-Powered-By', 'metaddok')
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'X-Requested-With')
        resp.status = falcon.HTTP_200

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
geocode = GeocodeResource()

# things will handle all requests to the matching URL path
app.add_route('/search', geocode)

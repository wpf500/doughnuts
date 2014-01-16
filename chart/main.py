import requests, json
import chart
from flask import Flask, Response
app = Flask(__name__)
app.debug = True

data = 'http://192.168.2.250:3000/infographics/%s.json'

@app.route("/render/<data_id>")
def hello(data_id):
    r = requests.get(data % data_id)
    return Response(chart.render(json.loads(r.text)), mimetype='image/svg+xml')

if __name__ == "__main__":
    app.run()

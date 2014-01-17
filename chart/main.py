import requests, json
import chart
from flask import Flask, Response
app = Flask(__name__)

live_url = 'http://192.168.2.250:3000/infographics/%s.json'
example_url = '../examples/%s.json'

def render_chart(data):
    return Response(chart.render(json.loads(data)), mimetype='image/svg+xml')

@app.route("/render/<data_id>")
def render(data_id):
    r = requests.get(live_url % data_id)
    return render_chart(r.text)

@app.route('/example/<example_id>')
def example(example_id):
    with open(example_url % example_id) as f:
        return render_chart(f.read())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

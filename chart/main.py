import requests, json
import chart
from flask import Flask, Response
app = Flask(__name__)

live_url = 'http://127.0.0.1:3000/'

live_urls = {
    'pie': live_url + 'infographics/%s.json',
    'doughnut': live_url + 'infographics/%s.json',
    'line': live_url + 'line_charts/%s.json'
}

example_url = '../examples/%s.json'

def render_chart(data):
    return Response(chart.render(json.loads(data)), mimetype='image/svg+xml')

@app.route("/render/<type_>/<data_id>")
def render(type_, data_id):
    r = requests.get(live_urls[type_] % data_id)
    return render_chart(r.text)

@app.route('/example/<example_id>')
def example(example_id):
    with open(example_url % example_id) as f:
        return render_chart(f.read())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

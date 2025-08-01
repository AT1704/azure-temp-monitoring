from flask import Flask, Response
import requests

app = Flask(__name__)

CITY = "Tallinn"
URL = f"https://wttr.in/{CITY}?format=j1"

@app.route("/metrics")
def metrics():
    try:
        data = requests.get(URL).json()
        temp_c = float(data["current_condition"][0]["temp_C"])
        prometheus_metric = f'temperature_celsius{{location="{CITY}"}} {temp_c}\n'
    except Exception as e:
        prometheus_metric = f'# Error fetching temperature: {e}\n'
    return Response(prometheus_metric, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9100)
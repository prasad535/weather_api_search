from flask import Flask, render_template, jsonify, request
import requests


app = Flask(__name__)

# My first app
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route("/weather_app", methods=["POST", "GET"])
def get_weather_app():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q':request.form.get("city"),
        'units':request.form.get("units"),
        'appid':request.form.get('appid')
    }

    response = requests.get(url, params=param)
    data = response.json()

    return f"data: {data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

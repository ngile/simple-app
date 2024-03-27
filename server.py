import os
import argparse
from flask import Flask, render_template
from weather import get_current_weather
from waitress import serve


def create_app(city):
    app = Flask(__name__)

    @app.route("/")
    @app.route("/index")
    def index():
        weather_data = get_current_weather(city)

        if not weather_data["cod"] == 200:
            return render_template("404.html")

        return render_template(
            "index.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}",
        )

    return app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=False)
    args = parser.parse_args()

    if args.city:
        city = args.city
    elif os.getenv("CURRENT_CITY"):
        city = os.getenv("CURRENT_CITY")
    else:
        city = "NA"

    app = create_app(city)
    serve(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

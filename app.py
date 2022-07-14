from flask import Flask, render_template, request
import time
from datetime import datetime
import json

app = Flask(__name__)

markers = []


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "POST":
        if "lat" in request.form and "lon" in request.form and "time" in request.form:
            markers.append({
                "lat": request.form["lat"],
                "lon": request.form["lon"],
                "time": request.form["time"],
                "index": len(markers)
            })

        else:
            return "Invalid data sent"
    elif request.method == "GET":

        if "index" in request.args:
            index = int(
                request.args["index"]) if request.args["index"]. isdigit() else None

            if index < 0 or index == None:
                return "Invalid index"
            elif index >= len(markers):
                return "No new entries"
            else:
                return json.dumps(markers[index:])
        else:
            return "No index present"

    else:
        return "Method not supported"

    return "OK"


@app.route("/")
def root():
    return render_template("index.html", markers=markers)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

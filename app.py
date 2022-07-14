from flask import Flask, render_template, request, jsonify
import time
from datetime import datetime
import json

app = Flask(__name__)

markers = []


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "POST":

        print(str(request.data))

        json_data = jsonify(str(request.data))

        if "lat" in json_data and "lon" in json_data and "time" in json_data:
            markers.append({
                "lat": json_data["lat"],
                "lon": json_data["lon"],
                "time": json_data["time"],
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
    app.run(host="0.0.0.0", port=8080, debug=True)

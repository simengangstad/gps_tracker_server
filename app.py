from flask import Flask, render_template, request, jsonify
import json
from os import path, stat

DATAFILE = "data.json"

markers = []

app = Flask(__name__)


@app.route("/data", methods=["POST", "GET"])
def data():
    if request.method == "POST":
        json_data = {}

        try:
            json_data = json.loads(request.data.decode("utf8"))
        except:
            return "Error decoding JSON"

        if "lat" in json_data and "lon" in json_data and "time" in json_data:
            markers.append({
                "lat": json_data["lat"],
                "lon": json_data["lon"],
                "time": json_data["time"],
                "index": len(markers)
            })

            with open("data.json", "w") as file:
                json.dump(markers, file)
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

    if not path.isfile(DATAFILE):
        # Create the file
        open(DATAFILE, "x")

    with open("data.json", "r") as file:
        if stat(DATAFILE).st_size != 0:
            markers = json.load(file)

    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="localhost", port=8080, debug=True)

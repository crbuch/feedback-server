from flask import Flask, request
import time
import json

app = Flask(__name__)


feedbackArr:list = []


@app.route("/submit", methods=["POST"])
def submit():
    requestJson = request.get_json()
    feedbackArr.append(
        {
            "Feedback":requestJson["feedback"],
            "Time":time.time(), 
            "Username":requestJson["username"]
        }
    )
    return "Feedback Submitted Successfully"

@app.route("/get", methods=["GET"])
def get_feedback():
    #the amount of days back the feedback goes
    daysback = request.args.get("daysback")

    if daysback:
        newFeedback = []

        secondsback = int(daysback) * 24 * 60 * 60
        for i in reversed(feedbackArr):
            if time.time()- i["Time"] < secondsback:
                newFeedback.append(i)
            else:
                break
        return json.dumps(newFeedback)


    return json.dumps(feedbackArr)

@app.route("/" , methods=["GET", "POST"])
def index():
    return "null"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
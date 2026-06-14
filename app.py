from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.utils.common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline




app = Flask(__name__)
CORS(app)         # Allows the cross origin requests

class ClientApp:
    def __init__(self):
        self.filename = "inputImg.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("dvc repro")
    return "Training done successfully!!!!"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json["image"]
    decodeImage(image, cApp.filename)
    result = cApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    cApp = ClientApp()
    app.run(host="0.0.0.0", port=8000)
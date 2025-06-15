from flask import Flask, render_template, request
import os
import pickle

from utils.link_utils import extract_features

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "model", "phishing_model.pkl")
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    url = ""
    if request.method == "POST":
        url = request.form.get("url", "")
        if url:
            try:
                features = extract_features(url)
                pred = model.predict([features])[0]
                prediction = "Phishing Website" if pred == -1 else "Legitimate Website"
            except Exception as e:
                prediction = f"Error: {e}"
        else:
            prediction = "Please enter a URL."
    return render_template("index.html", prediction=prediction, url=url)

if __name__ == "__main__":
    app.run(debug=True)
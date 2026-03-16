from flask import Flask, render_template
import json
import os

app = Flask(__name__)

with open("memes.json") as f:
    memes = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", memes=memes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
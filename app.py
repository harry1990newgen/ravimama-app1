from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def harry_message():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", current_date=current_date)

@app.route('/health')
def health():
    return "Server is up and running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


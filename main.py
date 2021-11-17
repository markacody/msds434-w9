from flask import Flask, render_template


# Create the app and bootstrap instances
app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
@app.route("/welcome")
def index():
    return render_template("index.html")


@app.route("/done")
def done():
    return render_template("done.html")


# Start server and run app on host/port: python -m flask run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

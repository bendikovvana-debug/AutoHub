from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bmw")
def bmw():
    return render_template("bmw.html")

@app.route("/bmw/m5")
def bmw_m5():
    return render_template("m5.html")

@app.route("/bmw/x5")
def bmw_x5():
    return render_template("x5.html")

@app.route("/bmw/m3")
def bmw_m3():
    return render_template("m3.html")

@app.route("/volkswagen")
def volkswagen():
    return render_template("volkswagen.html")

@app.route("/volvo")
def volvo():
    return render_template("volvo.html")

if __name__ == "__main__":
    app.run(debug=True)
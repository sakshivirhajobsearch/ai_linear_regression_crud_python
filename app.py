from flask import Flask, render_template, request, redirect, url_for
import database
import model

app = Flask(__name__)
database.init_db()

@app.route("/")
def index():
    data = database.get_all_data()
    return render_template("index.html", dataset=data)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        x_value = float(request.form["x_value"])
        y_value = float(request.form["y_value"])
        database.add_data(x_value, y_value)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/update/<int:record_id>", methods=["GET", "POST"])
def update(record_id):
    record = database.get_data_by_id(record_id)
    if request.method == "POST":
        x_value = float(request.form["x_value"])
        y_value = float(request.form["y_value"])
        database.update_data(record_id, x_value, y_value)
        return redirect(url_for("index"))
    return render_template("update.html", record=record)

@app.route("/delete/<int:record_id>")
def delete(record_id):
    database.delete_data(record_id)
    return redirect(url_for("index"))

@app.route("/predict", methods=["POST"])
def predict():
    x_input = float(request.form["x_input"])
    prediction = model.predict_value(x_input)
    data = database.get_all_data()
    return render_template("index.html", dataset=data, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask("BaseBura")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Tipo_de_cuenta")
def cuentas():
    return render_template("cuenta.html")

if __name__ == "__main__":
    app.run(debug=True)

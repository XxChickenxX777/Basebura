from flask import Flask, render_template
from flask_font_awesome import FontAwesome

app = Flask(__name__)
font_awesome = FontAwesome(app)

app = Flask("BaseBura")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Tipo_de_cuenta")
def cuentas():
    return render_template("cuenta.html")

@app.route("/Administrador")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/f", methods=["GET", "POST"])
def admino():
    if request.method == "POST":
        email = request.form.get("email")
        #procesar datos de entrada
        return redirect(url_for("admincuentas", email= email))
    return render_template("admin.html")

@app.route("/Administrar_cuentas")
def admincuentas():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("admincuentas.html", email=email)

if __name__ == "__main__":
    app.run(debug=True)
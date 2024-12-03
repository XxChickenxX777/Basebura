from flask import Flask, render_template, request, redirect, url_for

app = Flask("BaseBura")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Tipo_de_cuenta")
def cuentas():
    return render_template("cuentas.html")

@app.route("/Administrador")
def admin():
    return render_template("admin.html")

@app.route("/f", methods=["GET", "POST"])
def admino():
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        print(email)
        print(contraseña)
        #procesar datos de entrada
        return redirect(url_for("admincuentas", email= email))
    return render_template("admin.html")

@app.route("/Menú_Administrador")
def admincuentas():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("admincuentas.html", email=email)

@app.route("/Crear_cuentas")
def ccuentas():
    return render_template("ccuentas.html")

@app.route("/cc", methods=["GET", "POST"])
def cuentano():
    if request.method == "POST":
        email = request.form.get("email")
        #procesar datos de entrada
        return redirect(url_for("cuentac", email= email))
    return render_template("ccuentas.html")

@app.route("/Cuenta_creada")
def cuentac():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("cuenta_c.html", email=email)

@app.route("/Editar_cuentas")
def ecuentas():
    return render_template("ecuentas.html")

@app.route("/Eliminar_cuentas")
def elcuentas():
    return render_template("elcuentas.html")

@app.route("/Representante")
def representante():
    return render_template("representante.html")

@app.route("/r", methods=["GET", "POST"])
def repro():
    if request.method == "POST":
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        print(email)
        print(contraseña)
        #procesar datos de entrada
        return redirect(url_for("srepre", email= email))
    return render_template("representante.html")

@app.route("/Menú_Representante")
def srepre():
    #obtener el parametro opcional
    email = request.args.get("email", "contraseña")
    return render_template("srepre.html", email=email)

@app.route("/Solicitar_Servicio")
def solicitars():
    return render_template("sservicio.html")

@app.route("/ss", methods=["GET", "POST"])
def solicitor():
    if request.method == "POST":
        email = request.form.get("email")
        tianguis = request.form.get("tianguis")
        print(email)
        print(tianguis)
        #procesar datos de entrada
        return redirect(url_for("servicios", email= email, tianguis=tianguis))
    return render_template("sservicio.html")

@app.route("/Servicio_Solicitado")
def servicios():
    #obtener el parametro opcional
    email = request.args.get("email")
    tianguis = request.args.get("tianguis")
    if tianguis == "Tianguis 1":
        return render_template("servicios1.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 2":
        return render_template("servicios2.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 3":
        return render_template("servicios3.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 4":
        return render_template("servicios4.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 5":
        return render_template("servicios5.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 6":
        return render_template("servicios6.html", email=email, tianguis=tianguis)
    if tianguis == "Tianguis 7":
        return render_template("servicios7.html", email=email, tianguis=tianguis)

if __name__ == "__main__":
    app.run(debug=True)
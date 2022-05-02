from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():	
	return render_template("index.html")

@app.route("/hello", methods=["POST"])
def login():
    name=request.form.get("nombre")
    apellido=request.form.get("apellido")
    cumple=request.form.get("cumple")
    email=request.form.get("email")
    numero=request.form.get("numero")
    sexo=request.form.get("sexo")
    pais=request.form.get("pais")
    return render_template(
		"profile.html", 
		name=name, 
		apellido=apellido, 
		cumple=cumple, 
		email=email, 
		numero=numero,
		sexo=sexo,
		pais=pais
		)

@app.route("/<string:name>")
def session(name):
	return render_template("profile.html",name=name,)

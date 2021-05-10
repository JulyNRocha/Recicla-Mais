import sqlite3
from flask import Flask, render_template, url_for
from flask_googlemaps import GoogleMaps, Map

# import mariadb

app = Flask(__name__, template_folder='templates')

# you can set key as config
#app.config['GOOGLEMAPS_KEY'] = "AIzaSyCPsMj18rQoptfuX-QhAfdHtQm-cCB6KMk"
# app.config['GOOGLEMAPS_KEY'] = "AIzaSyAyn0NghGcyvLU7BpiTmvBpTH_vN6TD87U"

# Initialize the extension
# GoogleMaps(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobrenos")
def sobrenos():
    return render_template('sobre-nos.html')

@app.route("/coletadelixo")
def coletadelixo():
    return render_template('coletadelixo.html')
    
@app.route("/catadores")
def catadores():
    return render_template('catadores.html')

@app.route("/buscarempresas")
def buscarempresas():

	data = ['Empresa1', 'empresa2', 'empresa3', 'empresa4']
	data2 = []
	empresas = []

	for x in data:
		empresa = 'Empresa@gmail.com | Endereço: Rua X, bairro Y, Serra/ES | Telefone: 0000-0000'
		empresas.append(empresa)

	return render_template('buscarempresas.html', quantidade = len(empresas), empresas = empresas)

	# cursor = conn.cursor()

	# try:
	# 	cursor.execute("SELECT * FROM EMPRESAS WHERE status = 1")
	# 	data = cursor.fetchall()

	# 	return render_template('buscarempresas.html', quantidade = len(empresas), empresas = data)

	# except sqlite3.Error as e:
	# 	print(e)

	# finally:
	# 	cursor.close()
	# 	conn.close()

if __name__ == "__main__":
    app.run(use_reloader = True, debug=True)
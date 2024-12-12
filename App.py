import os
from flask import*
from passlib.hash import sha256_crypt
from funciones import *
from login import inicio
import re


app = Flask(__name__)
app.secret_key = "Moltr3s_3l_Gu4jolot3_M4cías"

@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
@app.route("/")
def index():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        msg = ''
        return render_template('login.html', mensaje=msg)
    if request.method == 'POST':
        usuario = request.form['nombre']
        # No necesitamos la contraseña en absoluto si no vamos a verificarla
        c_usuario = comprobarUsuario()
        if usuario not in c_usuario:
            msg = 'El usuario no existe'
            return render_template('login.html', mensaje=msg)
        else:
            # Omitimos toda la lógica de verificación de contraseñas
            session['nombre'] = usuario
            session['logged_in'] = True
            if 'ruta' in session:
                ruta = session['ruta']
                session['ruta'] = None
                return redirect(ruta)
            else:
                return redirect("/")







@app.route('/registro', methods=['GET', 'POST'])
@app.route('/registro/', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        msg = ''
        return render_template('registro.html', mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'enviar':
            usuario = request.form['nombre']
            correo = request.form['correo']
            password = request.form['contraseña']
            status = request.form['status']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobarUsuario()
            if usuario not in c_usuario:
                guardarUsuario(usuario, correo, password_cryp, status)
                return redirect('/login')
            else:
                msg = 'El usuario ya existe'
                return render_template('registro.html', mensaje=msg)
        else:
            return render_template('registro.html', mensaje='Error en el registro')



@app.route('/bd', methods=['GET'])
@app.route('/bd/', methods=['GET'])
def bd():
    
    datos = getConceptos("BD")
    if request.method == 'GET':
        return render_template('bd.html', datos = datos)
    
@app.route('/ed', methods=['GET'])
@app.route('/ed/', methods=['GET'])
def ed():
    datos = getConceptos("ED")
    if request.method == 'GET':
        return render_template('ed.html', datos = datos)

@app.route('/electronica', methods=['GET','POST'])
@app.route('/electronica/', methods=['GET','POST'])
def elec():
    datos = getConceptos("elect")
    if request.method == 'GET':
        return render_template('electronica.html', datos = datos)

@app.route('/poo2', methods=['GET'])
@app.route('/poo2/', methods=['GET'])
def poo2():
    datos = getConceptos("Poo II")
    if request.method == 'GET':
        return render_template('poo2.html', datos = datos)

@app.route('/ident', methods=['GET'])
@app.route('/ident/', methods=['GET'])
def ident():
    if request.method == 'GET':
        return render_template('identificacion.html')
    
@app.route('/multi', methods=['GET'])
@app.route('/multi/', methods=['GET'])
def multi():
    if request.method == 'GET':
        return render_template('multiplexor.html')
    
@app.route('/demulti', methods=['GET'])
@app.route('/demulti/', methods=['GET'])
def demulti():
    if request.method == 'GET':
        return render_template('demultiplexor.html')
    
@app.route('/perfil', methods=['GET'])
@app.route('/perfil/', methods=['GET'])
def perfil():
    if request.method == 'GET':
        return render_template('perfil.html')
#Cerrar sesion
@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")

@app.route('/resultado', methods=['POST'])
def process_equation():
    ecuacion = request.form['equation']
    resultado = identificar_ecuacion(ecuacion)
    return jsonify(resultado)

@app.route('/ident', methods=['POST'])
def identify_equation():
    data = request.get_json()
    ecuacion = data.get('equation')
    def identificar(ecuacion):
        grado = 1
        orden = 1

        match_grado = re.findall(r'(?<![dx])\^(\d)', ecuacion)
        if match_grado:
            grado = max(map(int, match_grado))

        if "d^" in ecuacion:
            for i in range(2,8):
                if re.search(rf"d\^{i}(?![dx])", ecuacion):
                    orden = i
                    break
        
        return grado, orden
    
    grado, orden = identificar(ecuacion)
    results = {
        "grado": f"{grado}", 
        "orden": f"{orden}",  
        "linealidad": "Lineal" if "y" in ecuacion and "^" not in ecuacion else "No lineal",
        "tipo": "Ordinaria" if "∂" not in ecuacion else "Parcial" 
    }

    return jsonify(results)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
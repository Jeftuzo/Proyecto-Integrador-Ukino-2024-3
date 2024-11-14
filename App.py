import os
from flask import*
from passlib.hash import sha256_crypt
from funciones import *
from login import incio

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

@app.route('/login', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
#"""
    if request.method == 'GET':
        msg = ''
        return render_template('login.html',mensaje=msg)
    else:
        if request.method == 'POST':
            usuario = request.form['nombre']
            user = comprobarUsuario(usuario)
            c_usuario = comprobarUsuario()
            
            if usuario not in c_usuario:
                return redirect('/registro')
            else:
                if usuario == user:
                    password_db = getPassword(usuario) # password guardado
                    password_forma = request.form['contraseña'] #password presentado
                    verificado = sha256_crypt.verify(password_forma,password_db)
                    user_in_sesion = usuario
                    if (verificado == True):
                        session['nombre'] = usuario
                        session['logged_in'] = True
                        incio(user_in_sesion)
                        if 'ruta' in session:
                            ruta = session['ruta']
                            session['ruta'] = None
                            return redirect(ruta)
                        else:
                            return redirect("/")
                    else:
                        msg = f'La contraseña del {usuario} no corresponde'
                        return render_template('/login.html',mensaje=msg)

@app.route('/registro', methods=['GET','POST'])
@app.route('/registro/', methods=['GET','POST'])
def registro():
    if request.method == 'GET':
        msg = ''
        return render_template('registro.html',mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor == 'Enviar':
            usuario = request.form['usuario']
            password = request.form['contraseña']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobarUsuario()
            if usuario not in c_usuario:
                guardarUsuario(usuario, password_cryp)
            return redirect('/login')

@app.route('/bd', methods=['GET'])
@app.route('/bd/', methods=['GET'])
def bd():
    Pagina = request.form['matria']
    idPagina = getIDPagina(Pagina)
    datos = getConceptos(idPagina)
    if request.method == 'GET':
        return render_template('bd.html', datos = datos)

@app.route('/ed', methods=['GET'])
@app.route('/ed/', methods=['GET'])
def ed():
    Pagina = request.form['matria']
    idPagina = getIDPagina(Pagina)
    datos = getConceptos(idPagina)
    if request.method == 'GET':
        return render_template('ed.html', datos = datos)

@app.route('/electronica', methods=['GET','POST'])
@app.route('/electronica/', methods=['GET','POST'])
def elec():
    Pagina = request.form['matria']
    idPagina = getIDPagina(Pagina)
    datos = getConceptos(idPagina)
    if request.method == 'GET':
        return render_template('electronica.html', datos = datos)

@app.route('/poo2', methods=['GET'])
@app.route('/poo2/', methods=['GET'])
def poo2():
    Pagina = request.form['matria']
    idPagina = getIDPagina(Pagina)
    datos = getConceptos(idPagina)
    if request.method == 'GET':
        return render_template('poo2.html', datos = datos)

@app.route('/ident', methods=['GET'])
@app.route('/ident/', methods=['GET'])
def ident():
    if request.method == 'GET':
        return render_template('indetificacion.html')
    
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

if __name__ == '__main__':
    app.run(debug=True)
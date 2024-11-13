from flask import *
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = "Contraseña"

@app.context_processor
def handle_context():
    return dict(os=os)

@app.route("/")
@app.route("/")
def index():
    datos = get_peliculas()

    if request.method == 'GET':
        return render_template("index.html", datos = datos)


@app.route('/login', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
#"""
    if request.method == 'GET':
        msg = ''
        return render_template('login.html', mensaje=msg)
    else:
        if request.method == 'POST':
            usuario = request.form['usuario']
            user = get_usuario(usuario)
            c_usuario = comprobar_usuario()

            if usuario not in c_usuario:
                return redirect('/new_user')
            else:
                if usuario == user:
                    password_db = get_password(usuario) #password guardado
                    password_forma = request.form['password'] #password presentado
                    verificado = sha256_crypt.verify(password_forma,password_db)
                    user_in_session = usuario
                    if (verificado == True):
                        session['usuario'] = usuario
                        session['looged_in'] = True
                        inicio(user_in_session)
                        if 'ruta' in session:
                            ruta = session['ruta']
                            session['ruta'] = None
                            return redirect(ruta)
                        else:
                            return redirect("/")
                    else:
                        msg = f'La contraseña del {usuario} no corresponde'
                        return render_template('/login.html', mensaje=msg)

@app.route('/registro', methods=['GET', 'POST'])
@app.route('/registro', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        msg = ''
        return render_template('registro.html', mensaje=msg)
    if request.method == 'POST':
        valor = request.form['enviar']
        if valor=='Enviar':
            usuario=request.form['usuario']
            password=request.form['contraseña']
            password_cryp = sha256_crypt.hash(password)
            c_usuario = comprobar_usuario()
            if usuario not in c_usuario:
                save_user(usuario, password_cryp)
            return redirect('/login')
        
@app.route('/perfil', methods=['GET'])
@app.route('/perfil/', methods=['GET'])
def perfil():
    datos
    if request.method == 'GET':
        return render_template('perfil.html', datos = datos)


@app.route('/bd', methods=['GET'])
@app.route('/bd/', methods=['GET'])
def bd():
    datos
    if request.method == 'GET':
        return render_template('bd.html', datos = datos)
    
@app.route('/ed', methods=['GET'])
@app.route('/ed/', methods=['GET'])
def ed():
    datos
    if request.method == 'GET':
        return render_template('ed.html', datos = datos)

@app.route('/electronica', methods=['GET'])
@app.route('/electronica/', methods=['GET'])
def electronica():
    datos
    if request.method == 'GET':
        return render_template('electronica.html', datos = datos)

@app.route('/poo2', methods=['GET'])
@app.route('/poo2/', methods=['GET'])
def poo2():
    datos
    if request.method == 'GET':
        return render_template('poo2.html', datos = datos)
    




#Cerrar sesion
@app.route('/logout', methods=['GET'])
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")
    
if __name__ == '__main__':
    app.run(debug=True)
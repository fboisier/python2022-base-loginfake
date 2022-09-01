from flask import Flask, render_template, request, redirect,session, flash
app = Flask(__name__)
app.secret_key = 'cualquier cosa que sea secreta'

email='jajaja@jaja.com'
password= '12345'

@app.route('/')
def bienvenidos():

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    if (email==request.form['email'] 
        and password==request.form['password']):
        session['usuario']=email
        return redirect('/')
    else:
        flash('Correo o clave incorrecta.', 'error')
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__=="__main__":
    app.run(debug=True)  
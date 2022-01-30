
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Usuarios
from . import db
auth =  Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('email')
        contrasena = request.form.get('password')
        usuario = Usuarios.query.filter_by(correo=correo).first()
        if usuario:
            if check_password_hash(usuario.contrasena, contrasena):
                flash(f'Bienvenido {usuario}', category='success')
                login_user(usuario, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Contrasena incorrecta', category='error')
        else:
            flash('No Existe el correo', category='error')

    return render_template("login.html", usuario=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/registro',methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        correo = request.form.get('correo')
        usuario = request.form.get('usuario')
        contrasena1 = request.form.get('contrasena1')
        contrasena2 = request.form.get('contrasena2')
        correoexiste = Usuarios.query.filter_by(correo=correo).first()
        usuarioexiste = Usuarios.query.filter_by(usuario=usuario).first()

        if correoexiste:
            flash('Ya existe el correo.', category='error')
        elif usuarioexiste:
            flash('Ya existe el usuario.', category='error')
        elif len(correo) < 4:
            flash('El correo debe ser mayor a 4 caracteres', category='error')
        elif len(usuario) < 4:
            flash('El usuario debe ser mayor a 4 caracteres', category='error')
        elif contrasena1 != contrasena2:
            flash('Las contrasenas deben coincidir', category='error')
        elif len(contrasena1) < 7:
            flash('Las contrasenas deben tener al menos 7 caracteres', category='error')
        else:
            nuevo_usuario = Usuarios(correo=correo, usuario=usuario, password=generate_password_hash(contrasena1, method='sha256'))
            db.session.add(nuevo_usuario)
            db.session.commit()
            login_user(nuevo_usuario, remember=True)
            flash('Cuenta creada', category='success')
            return redirect(url_for('views.home'))

    return render_template("auth/registro.html", usuario=current_user)

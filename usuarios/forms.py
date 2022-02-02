from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class UsuariosForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre del usuario")])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired("Necesitas especificar el apellido paterno del usuario")])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired("Necesitas especificar el apellido materno del usuario")])
    email = StringField('Correo', validators=[DataRequired("Necesitas especificar el correo del usuario")])
    telefono = StringField('Telefono', validators=[DataRequired("Necesitas especificar el telefono del usuario")])
    direccion = StringField('Direccion', validators=[DataRequired("Necesitas especificar la direccion del usuario")])
    colonia = StringField('Colonia', validators=[DataRequired("Necesitas especificar la colonia del usuario")])
    cp = StringField('Codigo Postal', validators=[DataRequired("Necesitas especificar el cp del usuario")])
    foto_usuario = StringField('Foto del usuario', validators=[DataRequired("Necesitas especificar la foto  del usuario")])
    usuario = StringField('Usuario', validators=[DataRequired("Necesitas especificar el usuario")])
    contrasena = StringField('Contrasena', validators=[DataRequired("Necesitas especificar la contrasena del usuario")])
    pais = StringField('Pais', validators=[DataRequired("Necesitas especificar el pais del usuario")])
    entidad = StringField('Estado', validators=[DataRequired("Necesitas especificar la entidad del usuario")])
    municipio = StringField('Municipio', validators=[DataRequired("Necesitas especificar el municipio del usuario")])
    submit = SubmitField('Usuarios')


class Tipos_usuariosForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre del tipo de usuario")])
    nivel = StringField('Nivel', validators=[DataRequired("Necesitas especificar el nivel del tipo de usuario")])
    submit = SubmitField('Tipos_usuarios')


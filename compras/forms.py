from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ProveedoresForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    rfc = StringField('RFC', validators=[DataRequired()])
    razon_social = StringField('Razon social', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])
    email = StringField('Correo', validators=[DataRequired()])
    contacto = StringField('Contacto', validators=[DataRequired()])
    cp = StringField('C.P.', validators=[DataRequired()])
    colonia = StringField('Colonia', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    submit = SubmitField('Proveedores')

class ComprasForm(FlaskForm):
    fecha = StringField('Fecha', validators=[DataRequired()])
    subtotal = StringField('Subtotal', validators=[DataRequired()])
    iva = StringField('Iva', validators=[DataRequired()])
    total = StringField('Total', validators=[DataRequired()])
    submit = SubmitField('Compras')



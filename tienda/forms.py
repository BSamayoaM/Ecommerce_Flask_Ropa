from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PaisesForm(FlaskForm):
    nombre = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Paises')

class EstadosForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    pais = TextAreaField('Pais', validators=[DataRequired()])
    submit = SubmitField('Estados')

class MunicipiosForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    estado = TextAreaField('Estado', validators=[DataRequired()])
    submit = SubmitField('Municipios')

class PaqueteriasForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    rfc = TextAreaField('RFC', validators=[DataRequired()])
    razonsocial = TextAreaField('Razon social', validators=[DataRequired()])
    contacto = TextAreaField('Contacto', validators=[DataRequired()])
    submit = SubmitField('Paqueterias')



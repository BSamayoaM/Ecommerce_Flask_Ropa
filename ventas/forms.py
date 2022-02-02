from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class VentasForm(FlaskForm):
    fecha = StringField('Fecha', validators=[DataRequired("Necesitas especificar la fecha de la venta")])
    subtotal = TextAreaField('Subtotal', validators=[DataRequired("Necesitas especificar el subtotal de la venta")])
    iva = TextAreaField('IVA', validators=[DataRequired("Necesitas especificar el iva de la venta")])
    total = TextAreaField('Total', validators=[DataRequired("Necesitas especificar el total de la venta")])
    submit = SubmitField('Ventas')




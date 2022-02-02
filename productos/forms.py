from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Required



class ProductosForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar un nombre del producto")])
    descripcion = TextAreaField('Descripcion', validators=[DataRequired("Necesitas especificar una descripcio del producto")])
    existencia = TextAreaField('Existencia', validators=[DataRequired("Necesitas especificar la existencia del producto")])
    stock = TextAreaField('Stock', validators=[DataRequired("Necesitas especificar el stock del producto")])
    categoria = TextAreaField('Categoria', validators=[DataRequired("Necesitas especificar la categoria del producto")])
    marca = TextAreaField('Marca', validators=[DataRequired("Necesitas especificar la marca del producto")])
    modelo = TextAreaField('Modelo', validators=[DataRequired("Necesitas especificar el modelo del producto")])
    talla = TextAreaField('Talla', validators=[DataRequired("Necesitas especificar la talla del producto")])
    color = TextAreaField('Color', validators=[DataRequired("Necesitas especificar el color del producto")])
    submit = SubmitField('Productos')


class ModelosForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre del modelo")])
    submit = SubmitField('Modelos')

class MarcasForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre de la marca")])
    submit = SubmitField('Marcas')

class ColoresForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre del color")])
    submit = SubmitField('Colores')

class TallasForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre de la talla")])
    submit = SubmitField('Tallas')

class CategoriasForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Necesitas especificar el nombre de la categoria")])
    submit = SubmitField('Categorias')

class Fotos_productosForm(FlaskForm):
    foto = StringField('Nombre', validators=[DataRequired("Necesitas subir el archivo")])
    producto = StringField('Nombre', validators=[DataRequired("Necesitas especificar el producto")])
    submit = SubmitField('Fotos_productos')

class DescuentosForm(FlaskForm):
    cantidad = StringField('Title', validators=[DataRequired("Necesitas especificar la cantidad del descuento ")])
    fecha_fin = TextAreaField('Content', validators=[DataRequired("Necesitas especificar la fecha de finalizacion del descuento ")])
    fecha_inicio = TextAreaField('Content', validators=[DataRequired("Necesitas especificar la fecha de inicio del descuento ")])
    producto = TextAreaField('Content', validators=[DataRequired("Necesitas especificar el producto ")])
    submit = SubmitField('Descuentos')

class MermasForm(FlaskForm):
    fecha_merma = StringField('Fecha de la Merma', validators=[DataRequired("Necesitas especificar la fecha de la merma")])
    cantidad = TextAreaField('Cantidad de productos Mermados', validators=[DataRequired("Necesitas especificar la cantidad de los productos mermados")])
    producto = TextAreaField('Producto mermado', validators=[DataRequired("Necesitas especificar los productos mermados")])
    submit = SubmitField('Mermas')


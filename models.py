from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import *
from flask_appbuilder.models.mixins import ImageColumn

app = Flask(__name__)

app.config['SECRET_KEY']='1213456'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


class Usuarios(db.Model):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(30),unique=False,nullable=False)
    apellido_paterno=db.Column(db.String(30),unique=False,nullable=False)
    apellido_materno=db.Column(db.String(30),unique=False,nullable=False)
    email=db.Column(db.String(50),unique=False,nullable=False)
    telefono=db.Column(db.Integer,unique=False,nullable=False)
    direccion=db.Column(db.String(80),unique=False,nullable=False)
    colonia=db.Column(db.String(30),unique=False,nullable=False)
    cp=db.Column(db.Integer,unique=False,nullable=False)
    foto_usuario=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    pais=db.Column(db.Integer, db.ForeignKey('pais.id'))
    entidad=db.Column(db.Integer, db.ForeignKey('entidad.id'))
    municipio=db.Column(db.Integer, db.ForeignKey('municipio.id'))
    usuario=db.Column(db.String(30),unique=False,nullable=False)
    contrasena=db.Column(db.String(25),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Descuentos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad=db.Column(db.Integer,unique=False,nullable=False)
    fecha_inicio=db.Column(db.DateTime,unique=False,nullable=False)
    fecha_fin=db.Column(db.DateTime,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    
class Mermas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fecha_merma=db.Column(db.DateTime,unique=False,nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'))
    cantidad=db.Column(db.Integer,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Productos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    descripcion=db.Column(db.Text,unique=False,nullable=False)
    existencia=db.Column(db.Integer,unique=False,nullable=False)
    stock=db.Column(db.Integer,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'),
        nullable=False)    marca = db.Column(db.Integer, db.ForeignKey('marca.id'),
        nullable=False)
    modelo = db.Column(db.Integer, db.ForeignKey('modelo.id'),
        nullable=False)
    talla= db.Column(db.Integer, db.ForeignKey('talla.id'),
        nullable=False)
    color = db.Column(db.Integer, db.ForeignKey('color.id'),
        nullable=False)
class Modelos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Marcas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    foto_marca=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    status=db.Column(db.Boolean,unique=False,nullable=False)
class Tallas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)

    status=db.Column(db.Boolean,unique=False,nullable=False)
class Colores(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Categorias(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    descripcion=db.Column(db.Text,unique=False,nullable=False)
    foto_marca=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Fotos_productos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    foto=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Tipos_usuarios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(30),unique=False,nullable=False)
    nivel=db.Column(db.Integer,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Comentarios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    comentario=db.Column(db.Text,unique=False,nullable=False)
    usuario=db.Column(db.Integer, db.ForeignKey('usuario.id'),
        nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'),
        nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Calificaciones(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    puntuacion=db.Column(db.Integer,unique=False,nullable=False)
    usuario=db.Column(db.Integer, db.ForeignKey('usuario.id'),
        nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'),
        nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Proveedores(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50), primary_key=True)
    rfc=db.Column(db.String(25), primary_key=True)
    razon_social=db.Column(db.String(50), primary_key=True)
    direccion=db.Column(db.String(80), primary_key=True)
    email=db.Column(db.String(30), primary_key=True)
    contacto=db.Column(db.String(50), primary_key=True)
    cp=db.Column(db.Integer, primary_key=True)
    colonia=db.Column(db.String(30), primary_key=True)
    telefono=db.Column(db.Integer, primary_key=True)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Compras(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.DateTime,unique=False,nullable=False)
    subtotal=db.Column(db.Float,unique=False,nullable=False)
    iva=db.Column(db.Float,unique=False,nullable=False)
    total=db.Column(db.Float,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    proveedor=db.Column(db.String(20),unique=False,nullable=False)
class Ventas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.DateTime,unique=False,nullable=False)
    subtotal=db.Column(db.Float,unique=False,nullable=False)
    iva=db.Column(db.Float,unique=False,nullable=False)
    total=db.Column(db.Float,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    cliente=db.Column(db.String(20),unique=False,nullable=False)
class Paqueterias(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    rfc=db.Column(db.String(30),unique=False,nullable=False)
    razonsocial=db.Column(db.String(20),unique=False,nullable=False)
    contacto=db.Column(db.String(50),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Paises(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class Estados(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    pais=db.Column(db.Integer, db.ForeignKey('pais.id'),
        nullable=False)
class Municipios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    estado=db.Column(db.Integer, db.ForeignKey('estado.id'),
        nullable=False)
class DetalleVenta(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    cantidad=db.Column(db.String(20),unique=False,nullable=False)
    precio_compra=db.Column(db.String(20),unique=False,nullable=False)
    precio_venta=db.Column(db.String(20),unique=False,nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'),
        nullable=False)
    venta=db.Column(db.Integer, db.ForeignKey('venta.id'),
        nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
class DetalleCompra(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    cantidad=db.Column(db.String(20),unique=False,nullable=False)
    precio_compra=db.Column(db.String(20),unique=False,nullable=False)
    precio_venta=db.Column(db.String(20),unique=False,nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'),
        nullable=False)
    venta=db.Column(db.Integer, db.ForeignKey('venta.id'),
        nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)

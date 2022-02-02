from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from flask_appbuilder.models.mixins import ImageColumn

class Usuarios(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(150),unique=False,nullable=False)
    apellido_paterno=db.Column(db.String(30),unique=False,nullable=False)
    apellido_materno=db.Column(db.String(30),unique=False,nullable=False)
    email=db.Column(db.String(50),unique=False,nullable=False)
    telefono=db.Column(db.Integer,unique=False,nullable=False)
    direccion=db.Column(db.String(80),unique=False,nullable=False)
    colonia=db.Column(db.String(30),unique=False,nullable=False)
    cp=db.Column(db.Integer,unique=False,nullable=False)
    foto_usuario=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    usuario=db.Column(db.String(30),unique=False,nullable=False)
    contrasena=db.Column(db.String(25),unique=False,nullable=False)
    pais=db.Column(db.Integer, db.ForeignKey('pais.id'))
    entidad=db.Column(db.Integer, db.ForeignKey('entidad.id'))
    municipio=db.Column(db.Integer, db.ForeignKey('municipio.id'))
    comentarios = db.relationship('Comentarios', backref='comentarios_usuario', lazy=True)
    calificaciones = db.relationship('Calificaciones', backref='calificaciones_usuario', lazy=True)
    compras = db.relationship('Compras', backref='compras_usuario', lazy=True)

class Descuentos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    cantidad=db.Column(db.Integer,unique=False,nullable=False)
    fecha_fin=db.Column(db.DateTime,unique=False,nullable=False)
    fecha_inicio=db.Column(db.DateTime(timezone=True),unique=False,nullable=False,default=func.now())
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'))

class Mermas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fecha_merma=db.Column(db.DateTime,unique=False,nullable=False)
    cantidad=db.Column(db.Integer,unique=False,nullable=False)
    producto_id=db.Column(db.Integer, db.ForeignKey('producto.id'))

class Productos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    descripcion=db.Column(db.Text,unique=False,nullable=False)
    existencia=db.Column(db.Integer,unique=False,nullable=False)
    stock=db.Column(db.Integer,unique=False,nullable=False)
    status=db.Column(db.Boolean,unique=False,nullable=False)
    categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'),nullable=False)
    marca = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    modelo = db.Column(db.Integer, db.ForeignKey('modelo.id'),nullable=False)
    talla= db.Column(db.Integer, db.ForeignKey('talla.id'),nullable=False)
    color = db.Column(db.Integer, db.ForeignKey('color.id'),nullable=False)
    mermas = db.relationship('Mermas', backref='mermas_producto', lazy=True)
    descuentos = db.relationship('Descuentos', backref='descuentos_producto', lazy=True)
    comentarios = db.relationship('Comentarios', backref='comentarios_producto', lazy=True)
    calificaciones = db.relationship('Calificaciones', backref='calificaciones_producto', lazy=True)

class Modelos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    productos = db.relationship('Productos', backref='productos_modelo', lazy=True)

class Marcas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    foto_marca=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    productos = db.relationship('Productos', backref='productos_marca', lazy=True)

class Tallas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    productos = db.relationship('Productos', backref='productos_talla', lazy=True)

class Colores(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    productos = db.relationship('Productos', backref='productos_color', lazy=True)
class Categorias(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    descripcion=db.Column(db.Text,unique=False,nullable=False)
    foto_marca=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    productos = db.relationship('Productos', backref='productos_categoria', lazy=True)
class Fotos_productos(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    foto=db.Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    producto = db.Column(db.Integer, db.ForeignKey('producto.id'),nullable=False)
class Tipos_usuarios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(30),unique=False,nullable=False)
    nivel=db.Column(db.Integer,unique=False,nullable=False)
    usuarios = db.relationship('Usuarios', backref='usuarios_tiposusuarios', lazy=True)
class Comentarios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    comentario=db.Column(db.Text,unique=False,nullable=False)
    usuario=db.Column(db.Integer, db.ForeignKey('usuario.id'),nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'),nullable=False)

class Calificaciones(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    puntuacion=db.Column(db.Integer,unique=False,nullable=False)
    usuario=db.Column(db.Integer, db.ForeignKey('usuario.id'),nullable=False)
    producto=db.Column(db.Integer, db.ForeignKey('producto.id'),nullable=False)

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
    compras = db.relationship('Compras', backref='compras_proveedor', lazy=True)

class Compras(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.DateTime,unique=False,nullable=False)
    subtotal=db.Column(db.Float,unique=False,nullable=False)
    iva=db.Column(db.Float,unique=False,nullable=False)
    total=db.Column(db.Float,unique=False,nullable=False)
    proveedor=db.Column(db.Integer, db.ForeignKey('proveedor.id'),nullable=False)

class Ventas(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fecha=db.Column(db.DateTime,unique=False,nullable=False)
    subtotal=db.Column(db.Float,unique=False,nullable=False)
    iva=db.Column(db.Float,unique=False,nullable=False)
    total=db.Column(db.Float,unique=False,nullable=False)
    cliente=db.Column(db.Integer, db.ForeignKey('usuario.id'),nullable=False)

class Paqueterias(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),unique=False,nullable=False)
    rfc=db.Column(db.String(30),unique=False,nullable=False)
    razonsocial=db.Column(db.String(20),unique=False,nullable=False)
    contacto=db.Column(db.String(50),unique=False,nullable=False)

class Paises(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    estados = db.relationship('Estados', backref='estados_pais', lazy=True)

class Estados(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    pais=db.Column(db.Integer, db.ForeignKey('pais.id'),nullable=False)
    municipios = db.relationship('Municipios', backref='municipios_estado', lazy=True)

class Municipios(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(20),unique=False,nullable=False)
    estado=db.Column(db.Integer, db.ForeignKey('estado.id'),nullable=False)




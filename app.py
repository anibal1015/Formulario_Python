from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime 
from flask_bootstrap import Bootstrap

#Creacion y configuracion 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3308/flask-shopy-2687365' 
app.config["SECRET_KEY"] = "@dmin"
bootstrap = Bootstrap(app)

#crear los objetos de SQLAlchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app ,db)
#modelos 
class Cliente(db.Model):
    __tablename__ ="clientes"
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100) , unique=True)
    email = db.Column(db.String(120) , unique=True)
    password = db.Column(db.String(128) )
    
class Producto(db.Model):
    __tablename__ ="productos"
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision= 10, scale=2))
    imagen = db.Column(db.String(100))
    
    
        
class Venta(db.Model):
    __tablename__ ="ventas"
    id = db.Column(db.Integer, primary_key =True)
    fecha = db.Column(db.DateTime ,default=datetime.utcnow)
    cliente_id = db.Column(db.Integer , db.ForeignKey ('clientes.id'))
    
    
class Detalle(db.Model):
    __tablename__ ="detalles"
    id = db.Column(db.Integer, primary_key =True)
    producto_id = db.Column(db.Integer , db.ForeignKey ('productos.id'))
    venta_id = db.Column(db.Integer , db.ForeignKey ('ventas.id'))
    cantidad = db.Column(db.Integer) 
    
#definir form registro de productos

class NuevoProductoForm(FlaskForm):
    
    username = StringField("Nombre de producto")
    precio = StringField("Precio del producto")
    submit = SubmitField("Registrar")
    
    
    
@app.route("/registrar_producto", methods=['GET','POST'])
def registrar():
    p = Producto()
    form = NuevoProductoForm()
    if form.validate_on_submit():
       #registrar producto en bd
       form.populate_obj(p)
       db.session.add(p)
       db.session.commit()
       return "producto registrado" 
    return render_template("registrar.html",
                           form = form )
    

   
  
    
    
    
    
   

      
 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100),nullable=False)
    precio = db.Column(db.Integer,nullable=False)


with app.app_context():
    db.create_all()


#Get
@app.route('api/productos',methods=['GET'])
def getProducto():
    producto = Producto.query.all()
    return jsonify([{'id':p.id,'nombre ':p.nombre,'precio ':p.precio} for p in producto])   


#Get for Id
@app.route('/productos/<int:id>',methods=['GET'])
def getIdProducto(id):
    producto = Producto.query.get(id)
    if producto:
        return jsonify ({'id':producto.id, 'nombre':producto.nombre,'precio': producto.precio})
    else:
        return jsonify({"Error producto no encontrados"}), 404


#Post
@app.route('api/productos/post',methods=['POST'])
def postProducto():
    data = request.get_json()
    new_producto = Producto(nombre=data['nombre'],precio=data['precio'])
    db.session.add(new_producto)
    db.session.commit()

    return jsonify({'id':new_producto.id}),201J


#Delete
@app.route('api/productos/delete/<int:id>',methods=['DELETE'])
def deleteProducto(id):
    producto = Producto.query.get(id)

    if not producto:
        return jsonify({'Error producto no encontrado'}), 404
    
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'Producto eliminado con exito'}), 201


#Path
@app.route('api/productos/edit/<int:id>',methods=['PATCH'])
def editProducto(id):
    prod = Producto.query.get(id)

    if not prod:
        return jsonify({'Error producto no encontrado'}), 404

    data = request.get_json()

    if 'nombre' in data:
        prod.nombre = data['nombre']
    if 'precio' in data:
        prod.precio = data['precio']

    db.session.commit()

    return jsonify({'id': prod.id,'nombre':prod.nombre,'precio':prod.precio})





if __name__  == '__main__':
    app.run(debug=True,port=8080)


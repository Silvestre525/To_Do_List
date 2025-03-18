from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100),nullable=False)
    precio = db.Column(db.Float,nullable=False)


with app.app_context():
    db.create_all()


#Get
@app.route('/api/productos',methods=['GET'])
def getProducto():
    productos = Producto.query.all()
    return jsonify([{'id':p.id,'nombre ':p.nombre,'precio ':p.precio} for p in productos])   


#Get for Id
@app.route('/api/productos/<int:id>',methods=['GET'])
def getIdProducto(id):
    producto = db.session.get(Producto,id)
    if producto:
        return jsonify ({'id':producto.id, 'nombre':producto.nombre,'precio': producto.precio})
    else:
        return jsonify({"error":"Producto no encontrado"}), 404


#Post
@app.route('/api/productos/add',methods=['POST'])
def postProducto():
    data = request.get_json()
    if not data or 'nombre' not in data or 'precio' not in data:
        return jsonify({"error": "Datos incompletos"}), 400

    new_producto = Producto(nombre=data['nombre'], precio=data['precio'])
    db.session.add(new_producto)
    db.session.commit()

    return jsonify({'id': new_producto.id}), 201



#Delete
@app.route('/api/productos/delete/<int:id>',methods=['DELETE'])
def deleteProducto(id):
    producto = db.session.get(Producto,id)

    if not producto:
        return jsonify({'error':'Error producto no encontrado'}), 404
    
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'msg':'Producto eliminado con exito'}), 201


#Path
@app.route('/api/productos/edit/<int:id>',methods=['PATCH'])
def editProducto(id):
    prod = db.session.get(Producto,id)
    
    if not prod:
        return jsonify({'error':'Producto no encontrado'}), 404

    data = request.get_json()

    if 'nombre' in data:
        prod.nombre = data['nombre']
    if 'precio' in data:
        prod.precio = data['precio']

    db.session.commit()

    return jsonify({'id': prod.id,'nombre':prod.nombre,'precio':prod.precio})





if __name__  == '__main__':
    app.run(debug=True,port=8080)


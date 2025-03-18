# CRUD de Productos con Flask, JSONify y SQLAlchemy

¡Bienvenido a mi repositorio! Este proyecto es una aplicación CRUD (Crear, Leer, Actualizar y Eliminar) de productos desarrollada con Flask, JSONify y SQLAlchemy. Su objetivo es practicar el desarrollo de APIs RESTful con Flask y la integración con bases de datos mediante SQLAlchemy.

## Características

- **Crear productos**: Agrega nuevos productos con nombre y precio.
- **Ver productos**: Obtén una lista de todos los productos disponibles.
- **Actualizar productos**: Modifica los datos de un producto existente.
- **Eliminar productos**: Borra productos de la base de datos.
- **Persistencia de datos**: Se utiliza una base de datos SQLite mediante SQLAlchemy.
- **API RESTful**: La aplicación expone endpoints JSON para interactuar con los productos.

## Tecnologías Utilizadas

- **Flask**: Framework web ligero para Python.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para interactuar con la base de datos.
- **JSONify**: Convertir respuestas de Flask a formato JSON.
- **SQLite**: Base de datos ligera utilizada para almacenar los productos.

## 📌 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio




| Método | Endpoint                             | Descripción                             |
|--------|--------------------------------------|-----------------------------------------|
| `GET`  | `/api/productos`                     | Obtiene todos los productos.            |
| `GET`  | `/api/productos/<int:id>`            | Obtiene un producto por ID.             |
| `POST` | `/api/productos/add`                 | Crea un nuevo producto.                 |
| `DELETE` | `/api/productos/delete/<int:id>`   | Elimina un producto por ID.             |
| `PATCH` | `/api/productos/edit/<int:id>`      | Actualiza un producto por ID.           |

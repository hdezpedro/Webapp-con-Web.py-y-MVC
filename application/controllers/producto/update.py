import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id_producto): 
        producto = config.model_producto.select_producto(id_producto) # Selecciona el registro que coincida con id
        return config.render.update(producto) # Envia el registro y renderiza update.html
    
    def POST(self, id_producto, nombre_producto, marca, cantidad, telefono):
        formulario= web.input() # almacena los datos del formulario
        id_producto=formulario['id_producto'] # almacena el nombre escrito en el input
        nombre_producto= formulario['nombre_producto'] # almacena el nombre escrito en el input
        marca= formulario['marca'] # almacena el marca en el imput
        cantidad= formulario['cantidad'] # almacena el cantidad en el input
        telefono= formulario['telefono'] # almacena el telefono en el input
        config.model_producto.update_producto(id_producto, nombre_producto, marca, cantidad, telefono) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index

import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario= web.input() # almacena los datos del formulario
        nombre_producto= formulario['nombre_producto']
        marca= formulario['marca'] 
        cantidad= formulario['cantidad'] 
        telefono= formulario['telefono'] # almacena el telefono en el input
        config.model_producto.insert_producto(nombre_producto, marca, cantidad, telefono) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html

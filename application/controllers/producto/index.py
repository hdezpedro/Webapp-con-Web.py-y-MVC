import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        producto= config.model_producto.select_producto().list() # Selecciona todos los registros de clientes
        return config.render.index(producto) # Envia todos los registros y renderiza index.html

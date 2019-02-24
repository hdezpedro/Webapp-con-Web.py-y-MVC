import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, id_cliente):  
        producto = config.model_producto.select_nombre(id_producto) # Selecciona el registro que coincida con id
        return config.render.view(producto) # Envia el registro y renderiza view.html

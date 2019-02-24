import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, id_producto: 
        producto = config.model_producto.select_ptoducto(id_producto) # Selecciona el registro que coincida con id_cliente
        return config.render.delete(producto) # Envia el registro y renderiza delete.html
    
    def POST(self, id_producto):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        id_producto = formulario['id_producto'] # Obtine el id_producto almacenado en el formulario
        config.model_producto.delete_producto(id_producto) # Borra el registro del id_producto seleccionado
        raise web.seeother('/') # Redirecciona a raiz

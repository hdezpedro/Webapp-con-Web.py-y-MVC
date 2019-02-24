import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla producto
'''
def select_producto():
    try:
        return db.select('producto') # Selecciona todos los registros de la tabla producto
    except Exception as e:
        print "Model select_producto Error {}".format(e.args)
        print "Model select_producto Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el id
'''
def select_producto(id_producto:
    try:
        return db.select('producto',where='id_producto=$id_producto', vars=locals())[0] # selecciona el primer registro que coincida con el id
    except Exception as e:
        print "Model select_producto Error {}".format(e.args)
        print "Model select_producto Message {}".format(e.message)
        return None

def insert_producto(nombre_producto, marca, cantidad, telefono):
    try:
        return db.insert('producto', nombre_producto=nombre_producto, marca=marca, cantidad=cantidad, telefono=telefono) # inserta un registro en producto
    except Exception as e:
        print "Model insert_producto Error {}".format(e.args)
        print "Model insert_producto Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id
'''
def delete_producto(id_producto):
    try:
        return db.delete('producto', where='id_producto=$id_producto',vars=locals()) # borra un registro de producto
    except Exception as e:
        print "Model delete_producto Error {}".format(e.args)
        print "Model delete_producto Message {}".format(e.message)
        return None

def update_producto(id_producto, nombre_producto, marca, cantidad, telefono): # actualiza datos que coincidan con el id
    try:
        return db.update('producto', nombre_producto=nombre_producto, marca=marca, cantidad=cantidad, telefono=telefono,  
            where='id_producto=$id_producto',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error {}".format(e.args)
        print "Model update_producto Message {}".format(e.message)
        return None

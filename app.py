import web
        
urls = (
    '/', 'application.controllers.producto.index.Index',
    '/insert', 'application.controllers.producto.insert.Insert',
    '/update/(.*)', 'application.controllers.producto.update.Update',
    '/delete/(.*)', 'application.controllers.producto.delete.Delete',
    '/view/(.*)', 'application.controllers.producto.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()

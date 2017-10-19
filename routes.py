from views import index, Telega


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_route('*', '/telega', Telega, name='telega')

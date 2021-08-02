from .controllers.SystemController import SystemController

def main(global_config, **settings):
    app = SystemController()
    return app.prepare_server(global_config, settings)
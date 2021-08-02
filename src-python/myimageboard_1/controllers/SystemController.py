from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

class SystemController:

    def prepare_server(self, global_config, settings):
        my_session_factory = SignedCookieSessionFactory('myimageboardsessionsecret')
        config = Configurator(settings=settings,
                              session_factory=my_session_factory)
        config.include('pyramid_chameleon')
        config.add_route('home', '/')
        config.add_route('sysinit', '/sysinit')
        config.add_route('login', '/login')
        config.add_route('signin', '/signin')
        config.add_route('rest_v1', '/rest/v1/{model}/{method}')
        config.add_route('reactadmin', '/react-admin-app-v100')
        config.add_route('rest_v1_react_admin', '/rest/v1-react-admin/{entitys}')
        config.add_route('post', '/post/{post_url}')
        config.add_static_view(name='assets', path='myimageboard_1:views/assets')
        config.scan('.HomeController')
        config.scan('.LoginController')
        config.scan('.SysInitController')
        config.scan('.RestController')
        config.scan('.SingleController')
        config.scan('.ReactAdminController')
        config.scan('.RestReactAdminV1Controller')
        return config.make_wsgi_app()
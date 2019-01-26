

def test_login(app):
    app.session.login('shanterrr@yandex.ru', 'zxcasdqwe123')
    assert app.session.is_logged_in()

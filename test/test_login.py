
def test_logins(app):
    assert app.soap.can_login('administrator', 'root')

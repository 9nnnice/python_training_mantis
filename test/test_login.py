
def test_logins(app):
    app.session.login('administrator', 'root')
    assert app.session.is_logged_in_as('administrator')


import pytest
import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['web']['baseUrl'], config=web_config)
    fixture.session.ensure_login(username=web_config['webadmin']['username'],
                                 password=web_config['webadmin']['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']

    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)

    return dbfixture

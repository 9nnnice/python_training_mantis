from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, base_url, config):
        print('application create')
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url
        self.soap = SoapHelper(self)
        self.config = config

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def open_project_page(self):
        self.wd.get(self.base_url + '/manage_proj_page.php')

    def destroy(self):
        self.wd.quit()

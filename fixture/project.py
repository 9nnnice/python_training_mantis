import time

from selenium.webdriver.common.by import By


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_new_project(self, project):
        self.app.open_project_page()
        wd = self.app.wd
        time.sleep(1)
        wd.find_element(By.XPATH, "//*[contains(text(), 'Create New Project')]").click()
        wd.find_element(By.ID, 'project-name').send_keys(project.name)
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()

    def delete_project(self, project):
        self.app.open_project_page()
        wd = self.app.wd
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, "td>a[href*=project_id\=" + str(project.id) + "]").click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        time.sleep(1)
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()



from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client('http://localhost/mantisbt/api/soap/mantisconnect.php?wsdl')

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_user_accessible_projects(self):
        try:
            _list = []
            projects = self.client.service.mc_projects_get_user_accessible('administrator', 'root')

            for project in projects:
                _list.append(Project(id=project.id, name=project.name))

            return _list
        except WebFault:
            return []

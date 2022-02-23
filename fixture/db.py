import pymysql
from model.project import Project


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_projects(self):
        list = []
        cursor = self.connection.cursor()
        query = "select id, name from mantis_project_table"
        try:
            cursor.execute(query)
            for row in cursor:
                (id, name) = row
                list.append(Project(id=id, name=name))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

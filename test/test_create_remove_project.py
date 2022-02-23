import random
import time
from model.project import Project


def test_create_project(app, db):
    # Получаем список проектов
    old_projects = db.get_projects()

    # Создаём новый проект
    app.project.create_new_project(Project(name='Some new project'))

    # Работа скрипта может продолжиться до завершения запроса
    time.sleep(1)

    # Получаем список проектов после создания
    new_projects = db.get_projects()

    # Если проходит, значит проект создан
    assert len(old_projects) + 1 == len(new_projects)


def test_remove_project(app, db):
    # Получаем список проектов
    old_projects = db.get_projects()

    # Удаляем проект
    project = random.choice(old_projects)
    app.project.delete_project(project)

    # Получаем список проектов после удаления
    new_projects = db.get_projects()

    # Если проходит, значит проект удален
    assert len(old_projects) - 1 == len(new_projects)

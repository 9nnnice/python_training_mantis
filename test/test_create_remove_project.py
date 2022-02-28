import random
import time
from model.project import Project


def test_create_project(app, db):
    # Получаем список проектов
    old_projects = db.get_projects()

    # Создаём новый проект
    project = Project(name='Mega super new awesome project')
    app.project.create_new_project(project)

    # Работа скрипта может продолжиться до завершения запроса
    time.sleep(1)

    # Получаем список проектов после создания
    new_projects = app.soap.get_user_accessible_projects()

    # Если проходит, значит проект создан
    assert len(old_projects) + 1 == len(new_projects)

    old_projects.append(project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_remove_project(app, db):
    # Получаем список проектов
    old_projects = db.get_projects()

    # Удаляем проект
    project = random.choice(old_projects)
    app.project.delete_project(project)

    # Получаем список проектов после удаления
    new_projects = app.soap.get_user_accessible_projects()

    # Если проходит, значит проект удален
    assert len(old_projects) - 1 == len(new_projects)

    old_projects.remove(project)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
import sys
import os
import pytest

# Добавляем текущую директорию в путь, чтобы импорты работали
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from service import TaskService


class FakeRepository:
    """Имитационный репозиторий без подключения к PostgreSQL."""

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add(self, task):
        task.id = self._next_id
        self._next_id += 1
        self.tasks.append(task)
        return task

    def get_all(self):
        return list(self.tasks)

    def update_status(self, task_id, status):
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                return


@pytest.fixture
def service():
    return TaskService(FakeRepository())


def test_successful_add_task(service):
    """Успешное добавление задачи."""
    task = service.add_task("Сделать отчёт")
    assert task.id == 1
    assert task.title == "Сделать отчёт"
    assert task.status == "Новая"
    assert len(service.get_all_tasks()) == 1


def test_empty_title_raises_value_error(service):
    """ValueError при пустом названии задачи."""
    with pytest.raises(ValueError):
        service.add_task("")

    with pytest.raises(ValueError):
        service.add_task("   ")


def test_invalid_status_raises_value_error(service):
    """ValueError при передаче недопустимого статуса."""
    task = service.add_task("Тестовая задача")
    with pytest.raises(ValueError):
        service.update_status(task.id, "В работе")

    with pytest.raises(ValueError):
        service.update_status(task.id, "Отменена")
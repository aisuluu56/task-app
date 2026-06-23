from models import Task


VALID_STATUSES = ("Новая", "Выполнена")


class TaskService:
    """Бизнес-логика работы с задачами."""

    def __init__(self, repository):
        self.repository = repository

    def add_task(self, title):
        """Создание новой задачи. При пустом названии — ValueError."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название задачи не может быть пустым")

        task = Task(task_id=None, title=title.strip(), status="Новая")
        return self.repository.add(task)

    def get_all_tasks(self):
        """Получение списка всех задач."""
        return self.repository.get_all()

    def mark_done(self, task_id):
        """Отметить задачу как выполненную."""
        self.repository.update_status(task_id, "Выполнена")

    def update_status(self, task_id, status):
        """Изменение статуса с проверкой допустимости."""
        if status not in VALID_STATUSES:
            raise ValueError(
                f"Недопустимый статус: {status!r}. "
                f"Разрешены только: {', '.join(VALID_STATUSES)}"
            )
        self.repository.update_status(task_id, status)
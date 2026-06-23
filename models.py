class Task:
    """Модель задачи. Не содержит SQL-запросов."""

    def __init__(self, task_id, title, status):
        self.id = task_id
        self.title = title
        self.status = status

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title!r}, status={self.status!r})"
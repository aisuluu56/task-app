from models import Task


class TaskRepository:
    """Работает с таблицей tasks через psycopg2-курсор."""

    def __init__(self, connection):
        self.connection = connection

    def add(self, task):
        """Добавление задачи. Возвращает Task с присвоенным id."""
        query = """
            INSERT INTO tasks (title, status)
            VALUES (%s, %s)
            RETURNING id
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (task.title, task.status))
            new_id = cursor.fetchone()[0]
        self.connection.commit()
        task.id = new_id
        return task

    def get_all(self):
        """Получение всех задач."""
        query = "SELECT id, title, status FROM tasks ORDER BY id"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
        return [Task(row[0], row[1], row[2]) for row in rows]

    def update_status(self, task_id, status):
        """Изменение статуса задачи по id."""
        query = "UPDATE tasks SET status = %s WHERE id = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(query, (status, task_id))
        self.connection.commit()
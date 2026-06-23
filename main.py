import os
import tkinter as tk
import psycopg2

from repository import TaskRepository
from service import TaskService
from ui import TaskApp


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "task_app"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
    )


def main():
    connection = get_connection()
    try:
        repository = TaskRepository(connection)
        service = TaskService(repository)

        root = tk.Tk()
        app = TaskApp(root, service)
        root.mainloop()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
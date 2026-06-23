import tkinter as tk
from tkinter import ttk, messagebox


class TaskApp:
    """Главное окно приложения. Работает с данными только через сервис."""

    def __init__(self, root, task_service):
        self.root = root
        self.task_service = task_service
        self.root.title("Учёт задач")
        self.root.geometry("600x400")

        self._build_ui()
        self.refresh_tasks()

    def _build_ui(self):
        # Верхняя панель — добавление задачи
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Название задачи:").pack(side="left")
        self.title_var = tk.StringVar()
        self.title_entry = ttk.Entry(top_frame, textvariable=self.title_var, width=30)
        self.title_entry.pack(side="left", padx=5)

        self.add_btn = ttk.Button(top_frame, text="Добавить", command=self.on_add)
        self.add_btn.pack(side="left")

        # Список задач
        columns = ("id", "title", "status")
        self.tree = ttk.Treeview(
            self.root, columns=columns, show="headings", height=12
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Название")
        self.tree.heading("status", text="Статус")
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("title", width=350)
        self.tree.column("status", width=150, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Нижняя панель — действия
        bottom_frame = ttk.Frame(self.root, padding=10)
        bottom_frame.pack(fill="x")

        self.done_btn = ttk.Button(
            bottom_frame, text="Отметить выполненной", command=self.on_mark_done
        )
        self.done_btn.pack(side="left", padx=5)

        self.refresh_btn = ttk.Button(
            bottom_frame, text="Обновить список", command=self.refresh_tasks
        )
        self.refresh_btn.pack(side="left", padx=5)

    def refresh_tasks(self):
        """Обновление таблицы задач."""
        for row_id in self.tree.get_children():
            self.tree.delete(row_id)
        try:
            tasks = self.task_service.get_all_tasks()
            for task in tasks:
                self.tree.insert("", "end", values=(task.id, task.title, task.status))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить задачи:\n{e}")

    def on_add(self):
        """Обработчик кнопки «Добавить»."""
        title = self.title_var.get()
        try:
            self.task_service.add_task(title)
            self.title_var.set("")
            self.refresh_tasks()
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def on_mark_done(self):
        """Обработчик кнопки «Отметить выполненной»."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите задачу в списке")
            return

        row_id = selected[0]
        values = self.tree.item(row_id, "values")
        task_id = int(values[0])

        try:
            self.task_service.mark_done(task_id)
            self.refresh_tasks()
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
class Task:
    def __init__(self, description, deadline, status="не выполнено"):
        """
        Конструктор задачи.
        :param description: Описание задачи.
        :param deadline: Срок выполнения задачи.
        :param status: Статус задачи (по умолчанию "не выполнено").
        """
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_done(self):
        """Отметить задачу как выполненную."""
        self.status = "выполнено"

    def __str__(self):
        """Возвращает строковое представление задачи."""
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {self.status}"


class TaskManager:
    def __init__(self):
        """Конструктор менеджера задач."""
        self.tasks = []

    def add_task(self, description, deadline):
        """Добавить новую задачу."""
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Задача добавлена: {task}")

    def mark_task_done(self, description):
        """Отметить задачу как выполненную по её описанию."""
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                print(f"Задача выполнена: {task}")
                return
        print(f"Задача с описанием '{description}' не найдена.")

    def show_current_tasks(self):
        """Показать список текущих (не выполненных) задач."""
        print("Текущие задачи:")
        for task in self.tasks:
            if task.status == "не выполнено":
                print(task)


# Пример использования
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Купить молоко", "09.01.2025")
task_manager.add_task("Сделать домашку", "09.01.2025")
task_manager.add_task("Позвонить другу", "10.01.2025")

# Показываем текущие задачи
task_manager.show_current_tasks()

# Отмечаем задачу как выполненную
task_manager.mark_task_done("Купить молоко")

# Показываем текущие задачи после выполнения одной из них
task_manager.show_current_tasks()

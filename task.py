class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, 'status': "не выполнено"})

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполнено"
                print(f"Задача '{description}' выполнена")
                return
        print(f"Задача '{description}' не найдена")

    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

# Пример использования
t = Task()
t.add_task(deadline="10.01.2025", description="Прочитать книгу")
t.add_task(deadline="09.01.2025", description="Пойти в магазин")
t.add_task(deadline="10.01.2025", description="Отправить отчет")
t.show_tasks()
t.complete_task("Прочитать книгу2")
t.complete_task("Прочитать книгу")
t.show_tasks()

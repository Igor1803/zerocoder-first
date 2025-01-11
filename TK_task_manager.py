import tkinter as tk

# Создание основного окна приложения
root = tk.Tk()
root.title("Task list")
root.configure(background="HotPink")

# Создание и позиционирование надписи для ввода задачи
text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink")
text1.pack(pady=5)

# Создание поля для ввода задачи
task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

# Создание кнопки для добавления задачи
add_task_button = tk.Button(root, text="Добавить задачу")
add_task_button.pack(pady=5)

# Создание кнопки для удаления задачи
delete_button = tk.Button(root, text="Удалить задачу")
delete_button.pack(pady=5)

# Создание кнопки для отметки задачи выполненной
mark_button = tk.Button(root, text="Отметить выполненную задачу")
mark_button.pack(pady=5)

# Создание и позиционирование надписи для списка задач
text2 = tk.Label(root, text="Список задач:", bg="HotPink")
text2.pack(pady=5)

# Создание списка задач
task_listBox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listBox.pack(pady=10)

# Функция для добавления задачи
def add_task():
    task = task_entry.get()  # Получаем текст из поля ввода
    if task:
        task_listBox.insert(tk.END, task)  # Добавляем задачу в конец списка
        task_entry.delete(0, tk.END)  # Очищаем поле ввода

# Привязка функции добавления задачи к кнопке
add_task_button.config(command=add_task)

# Функция для удаления задачи
def delete_task():
    selected_task = task_listBox.curselection()  # Получаем индекс выбранной задачи
    if selected_task:
        task_listBox.delete(selected_task)  # Удаляем выбранную задачу

# Привязка функции удаления задачи к кнопке
delete_button.config(command=delete_task)

# Функция для отметки задачи выполненной
def mark_task():
    selected_task = task_listBox.curselection()  # Получаем индекс выбранной задачи
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue")  # Меняем цвет задачи

# Привязка функции отметки задачи к кнопке
mark_button.config(command=mark_task)

# Запуск основного цикла приложения
root.mainloop()






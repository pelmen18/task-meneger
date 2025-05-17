def search_task(task):
    results = [task for task in TaskList if task.lower()]
    if results:
        print(f"{task}")
    else:
        print(f"{task} не знайдено.")

todo_list = [
    {"назва": "Купити хліб", "складність": "легка"},
    {"назва": "Написати звіт", "складність": "середня"},
    {"назва": "Вивчити Python", "складність": "складна"},
    {"назва": "Полити квіти", "складність": "легка"},
    {"назва": "Зробити домашнє завдання", "складність": "середня"}
]

def show_tasks_by_difficulty(level):
    """Виводить задачі певної складності"""
    filtered_tasks = [task for task in todo_list if task["складність"] == level.lower()]
    
    if filtered_tasks:
        print(f"\nСправи зі складністю '{level}':")
        for i, task in enumerate(filtered_tasks, 1):
            print(f"{i}. {task['назва']}")
    else:
        print(f"\nНемає справ зі складністю '{level}'.")

# --- Приклад використання ---
user_input = input("Оберіть складність (легка / середня / складна): ").strip().lower()
show_tasks_by_difficulty(user_input)
def search_task(task):
    results = [task for task in TaskList if task.lower()]
    if results:
        print(f"{task}")
    else:
        print(f"{task} не знайдено.")

def chose_difficulty(level):

    dificult_tasks = [task for task in TaskList if task["складність"] == level.lower()]

    if dificult_tasks:
        print(f"\nСправи зі складністю '{level}':")
        for i, task in enumerate(dificult_tasks, 1):
            print(f"{i}. {task['назва']}")
    else:
        print(f"\nНемає справ зі складністю '{level}'.")

_input = input("Оберіть складність (легка / середня / складна): ").strip().lower()
chose_difficulty(_input)


def add_task():
    name = input("Введіть назву справи: ").strip()
    difficulty = input("Введіть складність (легка / середня / складна): ").strip().lower()
    
    if difficulty not in ["легка", "середня", "складна"]:
        print("Такої складності немає")
        return

    task = {"назва": name, "складність": difficulty}
    TaskList.append(task)

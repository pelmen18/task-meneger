import json
from uuid import uuid4


class Task:
    last_id = 0

    def __init__(
        self, name, status=False, priority=3, deadline=None, uid=None, difficulty=None
    ):
        self.name = name
        self.status = status
        self.priority = priority
        self.deadline = deadline
        self.difficulty = difficulty
        if uid is not None:
            self.id = uid
        else:
            # self.id = str(uuid4())
            self.id = Task.last_id
            Task.last_id += 1
            print(Task.last_id)

    def __repr__(self):
        return f'Task(id={self.id}, name="{self.name}", status="{self.status}", priority="{self.priority}", deadline="{self.deadline}")'

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "priority": self.priority,
            "deadline": self.deadline,
            "difficulty": self.difficulty,
        }

    @classmethod
    def from_json(cls, task_dict):
        return cls(
            uid=task_dict["id"],
            name=task_dict["name"],
            status=task_dict["status"],
            priority=task_dict["priority"],
            deadline=task_dict["deadline"],
            difficulty=task_dict["difficulty"],
        )


class TaskList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [
                    Task.from_json(task_dict) for task_dict in data.get("tasks", [])
                ]
                Task.last_id = data.get("lastId", 0)
                print(Task.last_id)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "lastId": Task.last_id,
                    "tasks": [task.to_json() for task in self.tasks],
                },
                file,
                ensure_ascii=False,
                indent=2,
            )

    def search_task(self, task_name):
        results = [task for task in self.tasks if task_name in task.name.lower()]
        for task in results:
            print(f"{task}")
        if not results:
            print(f"{task_name} не знайдено.")

    def chose_difficulty(self, level):
        # dificult_tasks = [task for task in self.tasks if task["складність"] == level.lower()]
        dificult_tasks = []
        for task in self.tasks:
            if task.difficulty == level.lower():
                dificult_tasks.append(task)

        if dificult_tasks:
            print(f"\nСправи зі складністю '{level}':")
            for i, task in enumerate(dificult_tasks, 1):
                print(f"{i}. {task}")
        else:
            print(f"\nНемає справ зі складністю '{level}'.")

    def add_task(self):
        name = input("Введіть назву справи: ").strip()
        difficulty = (
            input("Введіть складність (легка / середня / складна): ").strip().lower()
        )

        if difficulty not in ["легка", "середня", "складна"]:
            print("Такої складності немає")
            return

    def delete_task(self):
        if not self.tasks:
            print("Список справ порожній.")
            return

        print("\nСписок справ:")
        for task in self.tasks:
            print(f"- {task}")

        name = input("Введіть назву справи, яку хочете видалити: ").strip()

        # if name in self.tasks:
        #     self.tasks.remove(name)
        #     print(f"Справу '{name}' видалено.")
        # else:
        #     print(f"Справу з назвою '{name}' незнайдено.")


new_task = Task("hello world", deadline="07.06.2025")

# print(new_task)
task_list = TaskList("file_storage.json")
task_list.load_tasks()
task_list.tasks.append(new_task)
task_list.search_task("привіт")
task_list.save_tasks()
task_list.chose_difficulty("складна")
task_list.delete_task()

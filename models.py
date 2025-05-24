import json
from uuid import uuid4


class Task:
    # last_id = 0

    def __init__(self, name, status=False, priority=3, deadline=None, id=None, difficulty=None):
        self.name = name
        self.status = status
        self.priority = priority
        self.deadline = deadline
        self.difficulty = difficulty
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid4())
            # self.id = Task.last_id
            # Task.last_id += 1

    def __repr__(self):
        return f'Task(id={self.id}, name="{self.name}", status="{self.status}", priority="{self.priority}", deadline="{self.deadline}", difficulty="{self.difficulty}")'

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
            id=task_dict["id"],
            name=task_dict["name"],
            status=task_dict["status"],
            priority=task_dict["priority"],
            deadline=task_dict["deadline"],
            difficulty=task_dict["difficulty"]
        )


class TaskList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.tasks = [Task.from_json(task_dict) for task_dict in data]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_json() for task in self.tasks],
                file,
                ensure_ascii=False,
                indent=2,
            )

    def search_task(self, task):
        results = [task for task in self.tasks if task.lower()]
        if results:
            print(f"{task}")
        else:
            print(f"{task} не знайдено.")


    def chose_difficulty(self, level):
        dificult_tasks = [task for task in self.tasks if task["складність"] == level.lower()]

        if dificult_tasks:
            print(f"\nСправи зі складністю '{level}':")
            for i, task in enumerate(dificult_tasks, 1):
                print(f"{i}. {task['назва']}")
        else:
            print(f"\nНемає справ зі складністю '{level}'.")

    def add_task(self):
        name = input("Введіть назву справи: ").strip()
        difficulty = input("Введіть складність (легка / середня / складна): ").strip().lower()
        
        if difficulty not in ["легка", "середня", "складна"]:
            print("Такої складності немає")
            return

        task = Task(name, priority=difficulty)
        self.tasks.append(task)


new_task = Task(
    "створити метод додавання завдання для классу TaskList", deadline="2.05.2025"
)

print(new_task)
task_list = TaskList("file_storage.json")
task_list.load_tasks()
task_list.tasks.append(new_task)
task_list.save_tasks()

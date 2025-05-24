import json
from uuid import uuid4


class Task:
    # last_id = 0

    def __init__(self, name, status=False, priority=3, deadline=None, id=None):
        self.name = name
        self.status = status
        self.priority = priority
        self.deadline = deadline
        if id is not None:
            self.id = id
        else:
            self.id = str(uuid4())
            # self.id = Task.last_id
            # Task.last_id += 1

    def __repr__(self):
        return f'Task(id={self.id}, name="{self.name}", status="{self.status}", priority="{self.priority}", deadline="{self.deadline}")'

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "priority": self.priority,
            "deadline": self.deadline,
        }

    @classmethod
    def from_json(cls, task_dict):
        return cls(
            id=task_dict["id"],
            name=task_dict["name"],
            status=task_dict["status"],
            priority=task_dict["priority"],
            deadline=task_dict["deadline"],
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


new_task = Task(
    "створити метод додавання завдання для классу TaskList", deadline="2.05.2025"
)

print(new_task)
task_list = TaskList("file_storage.json")
task_list.load_tasks()
task_list.tasks.append(new_task)
task_list.save_tasks()

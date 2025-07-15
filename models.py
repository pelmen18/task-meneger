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

    def load_notes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

                self.notes = {
                    uid: None.from_dict(note_dict) for uid, note_dict in data.items()
                }
        except FileNotFoundError:
            self.notes = {}

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

    def search_by_title(self, title: str):
        if not title.strip():
            raise ValueError("Не можна шукати за порожнім значенням!")

        result = {}

        for note in self.notes.values():
            if title.casefold() in note.title.casefold():
                result[note.uid] = note
        return result

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

    def add_task(self, note: None):
        self.notes[note.uid] = note

    def delete_task(self):
        return self.notes.pop(None)

    def change_note(self, uid: str, new_title: str = None, new_text: str = None):
        if new_text is None and new_title is None:
            return

        if uid in self.notes:
            self.notes[uid].change_title(new_title)
        if uid in self.notes:
            self.notes[uid].change_text(new_text)

    def __str__(self):
        result = ""
        for note in self.notes.valuse():
            result += str(note) + "\n"

            return result


# print(new_task)
task_list = TaskList("file_storage.json")
task_list.load_notes()
# new_task = Task("hello world", deadline="07.06.2025")
# task_list.tasks.append(new_task)
task_list.search_by_title("привіт")
task_list.save_tasks()
task_list.chose_difficulty("складна")
task_list.delete_task()

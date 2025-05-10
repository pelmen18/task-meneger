def search_task(task):
    results = [task for task in TaskList if task.lower()]
    if results:
        print(f"{task}")
    else:
        print(f"{task} не знайдено.")

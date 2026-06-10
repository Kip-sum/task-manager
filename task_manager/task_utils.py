from datetime import datetime

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")


def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]

    if not pending_tasks:
        print("No pending tasks.")
        return

    for task in pending_tasks:
        print(
            f"Title: {task['title']}, "
            f"Description: {task['description']}, "
            f"Due Date: {task['due_date']}"
        )


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    progress = (completed_tasks / len(tasks)) * 100

    return progress
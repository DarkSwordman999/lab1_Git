tasks = []


def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{number}. {status} {task['title']}")


def add_task(title):
    tasks.append({"title": title, "done": False})
    print("Задача добавлена.")


def complete_task(number):
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print("Задача выполнена.")
    else:
        print("Неверный номер задачи.")


def delete_task(number):
    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        print("Задача удалена.")
    else:
        print("Неверный номер задачи.")


while True:
    print("\n1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Выполнить задачу")
    print("4 - Удалить задачу")
    print("5 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        title = input("Введите задачу: ")
        add_task(title)
    elif choice == "3":
        number = int(input("Введите номер задачи: "))
        complete_task(number)
    elif choice == "4":
        number = int(input("Введите номер задачи: "))
        delete_task(number)
    elif choice == "5":
        break
    else:
        print("Неизвестная команда.")
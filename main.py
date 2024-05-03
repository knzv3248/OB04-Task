# Менеджер задач
# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и
# вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, name, description, time_limit, status):
        self.name = name
        self.description = description
        self.time_limit = time_limit
        self.status = status

    def info(self):
        print(f"Название задачи: {self.name}")
        print(f"Описание задачи: {self.description}")
        print(f"Срок выполнения задачи: {self.time_limit}")
        print(f"Статус задачи: {self.status}")


def add_task():     # добавление новой задачи
    n = len(task_list)  # размер списка задач
    name_new_task = input("Ведите имя новой задачи: ")
    description_new_task = input("Ведите описание новой задачи: ")
    time_limit_new_task = input("Ведите срока выполнения новой задачи: ")
    taski = Task(name = name_new_task, time_limit = time_limit_new_task,
                 status = "Не выполнена", description = description_new_task
                 )
    task_list.append(taski)

def time_limit():   # назначение/изменение срока выполнения задачи
    n = len(task_list)  # размер списка задач
    print('\n'"Сейчас будем изменять срок выполнения новой задачи")
    print(f"Сейчас для неё установлен срок выполнения задачи: {task_list[n - 1].time_limit}")
    time_limit_new = input("Ведите новый срок выполнения задачи :")
    taski = task_list[n - 1]
    name_i = taski.name
    status_i = taski.status
    description_i = taski.description
    task_list[n - 1] = Task(name=name_i, time_limit=time_limit_new, status=status_i,
                            description=description_i
                            )

def status():       # назначение/изменение статуса задачи (Выполнена, Не выполнена)
    n = len(task_list)  # размер списка задач
    print('\n'"Сейчас будем изменять статус новой задачи")
    print(f"Сейчас статус новой задачи: {task_list[n - 1].status}")
    status_i = input('Ведите новый срок выполнения задачи ("Выполнена" или "Не выполнена"): ')
    taski = task_list[n - 1]
    name_i = taski.name
    time_limit_i = taski.time_limit
    description_i = taski.description
    task_list[n - 1] = Task(name=name_i, time_limit=time_limit_i, status=status_i,
                            description=description_i
                            )

def print_continue():    # печать текущих (не законченных) задач
    print('\n''В настоящее время статус "Не выполнена" имеют следующие задачи:')
    for taski in task_list:
        if taski.status == "Не выполнена":
            print()
            taski.info()

task_list = []

task1  = Task(name = "Выпить воды", time_limit = "24.04.2024", status = "Выполнена",
              description = "Выпить стакан воды по установленному расписанию"
              )
task_list.append(task1)
task2  = Task(name = "Ликвидировать отставание", time_limit = "12.05.2024", status = "Не выполнена",
              description = "Ликвидировать отставание в обучении в Zerocoder"
              )
task_list.append(task2)

add_task()
print('\n'"Добавлена новая задача")
n = len(task_list)  # размер списка задач
task_list[n - 1].info()

time_limit_old = task_list[n-1].time_limit
time_limit()
print('\n'f"Для новой задачи срок исполнения изменён с {time_limit_old} "
      f"на {task_list[n-1].time_limit}")

status_old = task_list[n-1].status
status()
print(f"Для новой задачи срок исполнения изменён с {status_old} "
      f"на {task_list[n-1].status}")

print_continue()

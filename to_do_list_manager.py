task_list = []

task_txt = "todo_list.txt"


task_count = int(input("how many tasks you want to add: "))
i = 1
j = 1
while i <= task_count:

    task = input(f"Enter task{i}:")
    task_list.append((i, task))
    i = i+1

with open(task_txt, "w") as file:
    for task_number, task in task_list:
        file.write(f"{task_number}: {task} \n")
print()
print("Task list:")
with open(task_txt, 'r') as file:
    for x in file:
        print(x)

try:
    task_to_delete = int(
        input("Enter the task number to delete(press 'E' if None): "))
    if 1 <= task_to_delete <= len(task_list):
        removed_task = task_list.pop(task_to_delete - 1)
        print(f"Task '{removed_task[1]}' has been removed.")

except ValueError:
    print("To do list updated!")
    exit()

with open(task_txt, "w") as file:
    for task_number, task in task_list:
        file.write(f"{task_number}. {task}\n")
print("To do list updated")

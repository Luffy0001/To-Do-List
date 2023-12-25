class TO_DO_LIST:
    def __init__(self):
        self.list = []

    def add_to_list(self):
        print("Add tasks to your to-do-list and to exit just press enter after typing nothing.")
        while True:
            task = input("Add a task: ")
            if not task:
                break
            self.list.append(task)

    def remove_from_list(self):
        print("Current tasks in to-do-list: ")
        self.display_list()
        task_to_remove = input("Enter task to remove from list: ")
        if task_to_remove in self.list:
            self.list.remove(task_to_remove)
        else:
            print("Task does not exist.")

    def display_list(self):
        print("TO DO LIST:")
        for task in self.list:
            print(task)

to_do_list = TO_DO_LIST()
to_do_list.add_to_list()
to_do_list.display_list()

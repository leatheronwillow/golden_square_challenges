

class ToDo():
    def __init__(self):
        self.tasks = []
        pass

    def add_task(self, task):
        self.tasks.append(task)
        return None

    def see_tasks(self):
        return self.tasks

    def mark_complete(self, task):
        



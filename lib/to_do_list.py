

class ToDo():
    def __init__(self):
        self.tasks = []
        pass

    def add_task(self, task):
        task = task[0].upper() + task[1:].lower()
        if task not in self.tasks:
            self.tasks.append(task)
        else:
            raise Exception("This task already exists")
        
        return None

    def see_tasks(self):
        return self.tasks

    def mark_complete(self, task):
        task = task[0].upper() + task[1:].lower()
        try:
            self.tasks.remove(task)
        except ValueError:
            raise Exception("This task is not in the list")
        return None
    
        
        



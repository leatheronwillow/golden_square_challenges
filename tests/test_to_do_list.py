from lib.to_do_list import *

# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

def test_add_task():
    to_do =ToDo()
    to_do.add_task("hoover kitchen")
    assert to_do.see_tasks() == ["hoover kitchen"]
    to_do.add_task("laundry")
    assert to_do.see_tasks() == ["hoover kitchen", "laundry"]

def test_mark_complete():
    to_do =ToDo()
    to_do.add_task("hoover kitchen")
    to_do.add_task("clean chopping board")
    to_do.add_task("laundry")
    assert to_do.mark_complete("clean chopping board") == ["hoover kitchen", "laundry"]
    
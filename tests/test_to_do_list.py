from lib.to_do_list import *

# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

import pytest

def test_add_task():
    to_do =ToDo()
    to_do.add_task("hoover kitchen")
    assert to_do.see_tasks() == ["Hoover kitchen"]
    to_do.add_task("laundry")
    assert to_do.see_tasks() == ["Hoover kitchen", "Laundry"]
    to_do.add_task("GET THE TABLES")
    assert to_do.see_tasks() == ["Hoover kitchen", "Laundry", "Get the tables"]

def test_add_task_repeat():
    to_do =ToDo()
    to_do.add_task("hoover kitchen")
    to_do.add_task("laundry")
    with pytest.raises(Exception) as e:
        to_do.add_task("laundry")
    assert str(e.value) == "This task already exists"

def test_mark_complete():
    to_do =ToDo()
    to_do.add_task("hoover kitchen")
    to_do.add_task("clean chopping board")
    to_do.add_task("laundry")
    to_do.mark_complete("clean chopping board")
    assert to_do.see_tasks() == ["Hoover kitchen", "Laundry"]

def test_mark_complete_error():
    to_do =ToDo()
    to_do.add_task("hoover kitchen")
    to_do.add_task("clean chopping board")
    to_do.add_task("laundry")
    with pytest.raises(Exception) as e:
        to_do.mark_complete("execute order 66")
    error_message = str(e.value)
    assert error_message == "This task is not in the list"
    
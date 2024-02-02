from lib.todo import *

def test_to_do_init():
    task = Todo("laundry")
    assert task.task == "laundry"
    task2 = Todo("dishes")
    assert task2.task == "dishes"
    assert task.complete == False

def test_mark_complete():
    task = Todo("laundry")
    assert task.task == "laundry"
    task2 = Todo("dishes")
    assert task2.task == "dishes"
    task.mark_complete()
    assert task.complete == True
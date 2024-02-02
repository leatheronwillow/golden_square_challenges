from lib.todo import *
from lib.todo_list import *

def test_todo_list_init():
    todo_list = TodoList()
    assert type(todo_list) == type(TodoList())


def test_todo_list_add():
    todo_list = TodoList()
    laundry = Todo("laundry")
    dishes = Todo("dishes")
    todo_list.add(laundry)
    todo_list.add(dishes)
    assert todo_list.tasks == [laundry, dishes]

def test_todo_list_complete():
    todo_list = TodoList()
    laundry = Todo("laundry")
    dishes = Todo("dishes")
    hoover = Todo("hoover")
    todo_list.add(laundry)
    todo_list.add(dishes)
    todo_list.add(hoover)
    laundry.mark_complete()
    assert todo_list.complete() == [laundry]
    dishes.mark_complete()
    assert todo_list.complete() == [laundry, dishes]

def test_todo_list_incomplete():
    todo_list = TodoList()
    laundry = Todo("laundry")
    dishes = Todo("dishes")
    hoover = Todo("hoover")
    todo_list.add(laundry)
    todo_list.add(dishes)
    todo_list.add(hoover)
    assert todo_list.incomplete() == [laundry, dishes, hoover]
    laundry.mark_complete()
    assert todo_list.incomplete() == [dishes, hoover]
    dishes.mark_complete()
    assert todo_list.incomplete() == [hoover]
    hoover.mark_complete()
    assert todo_list.incomplete() == []
    
def test_give_up():
    todo_list = TodoList()
    laundry = Todo("laundry")
    dishes = Todo("dishes")
    hoover = Todo("hoover")
    todo_list.add(laundry)
    todo_list.add(dishes)
    todo_list.add(hoover)
    todo_list.give_up()
    assert todo_list.complete() == [laundry, dishes, hoover]
    assert todo_list.incomplete() == []
    


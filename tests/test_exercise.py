import pytest
from src.item import Item

def test_exercise():
    item = Item("My name")

    assert item.get_name() == "My name"
